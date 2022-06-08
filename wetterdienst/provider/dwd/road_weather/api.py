# -*- coding: utf-8 -*-
# Copyright (c) 2018-2022, earthobservations developers.
# Distributed under the MIT License. See LICENSE for more info.
import logging
from datetime import datetime
from enum import Enum
from functools import reduce
from io import BytesIO
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import List, Tuple
from urllib.parse import urljoin

import pandas as pd
import pdbufr

from wetterdienst import Kind, Period, Provider, Resolution
from wetterdienst.core.scalar.request import ScalarRequestCore
from wetterdienst.core.scalar.values import ScalarValuesCore
from wetterdienst.metadata.columns import Columns
from wetterdienst.metadata.datarange import DataRange
from wetterdienst.metadata.period import PeriodType
from wetterdienst.metadata.resolution import ResolutionType
from wetterdienst.metadata.timezone import Timezone
from wetterdienst.metadata.unit import OriginUnit, SIUnit, UnitEnum
from wetterdienst.provider.dwd.index import _list_remote_files_as_dataframe
from wetterdienst.provider.dwd.metadata.constants import (
    DWD_ROAD_WEATHER_REPORTS,
    DWD_SERVER,
)
from wetterdienst.util.cache import CacheExpiry
from wetterdienst.util.network import download_file
from wetterdienst.util.parameter import DatasetTreeCore

log = logging.getLogger(__name__)

DATE_REGEX = r"(?<!\d)(\d{10,})(?!\d)"
metadata_columns = (
    "stationOrSiteName",
    "shortStationName",
    "stateOrFederalStateIdentifier",
    "latitude",
    "longitude",
    "heightOfStationGroundAboveMeanSeaLevel",
    "typeOfRoad",
    "typeOfConstruction",
)
TIME_COLUMNS = ("year", "month", "day", "hour", "minute")
TMP_BUFR_FILE_PATH = Path("/", "tmp", "bufr_temp.bufr")
DEFAULT_TIME_PERIOD = -1
DEFAULT_SENSOR_HEIGHT = 0
DEFAULT_SENSOR_POSITION = 99


class DwdRoadWeatherObservationParameter(DatasetTreeCore):
    """
    enumeration for different parameter/variables
    measured by dwd road weather stations
    """

    class MINUTE_10(Enum):
        # class ROAD_WEATHER(Enum):
        ROAD_SURFACE_TEMPERATURE = "roadSurfaceTemperature"
        TEMPERATURE_AIR = "airTemperature"
        ROAD_SURFACE_CONDITION = "roadSurfaceCondition"
        WATER_FILM_THICKNESS = "waterFilmThickness"
        WIND_EXTREME = "maximumWindGustSpeed"
        WIND_EXTREME_DIRECTION = "maximumWindGustDirection"
        WIND_DIRECTION = "windDirection"
        WIND = "windSpeed"
        DEW_POINT = "dewpointTemperature"
        RELATIVE_HUMIDITY = "relativeHumidity"
        TEMPERATURE_SOIL = "soil_temperature"
        VISIBILITY_RANGE = "visibility"
        PRECIPITATION_TYPE = "precipitationType"
        TOTAL_PRECIPITATION = "totalPrecipitationOrTotalWaterEquivalent"
        INTENSITY_OF_PRECIPITATION = "intensityOfPrecipitation"
        INTENSITY_OF_PHENOMENA = "intensityOfPhenomena"
        HORIZONTAL_VISIBILITY = "horizontalVisibility"


COLUMNS_FILTER_MAPPING = {
    DwdRoadWeatherObservationParameter.MINUTE_10.ROAD_SURFACE_TEMPERATURE: {
        "filters": {},
        "columns": ("shortStationName", "positionOfRoadSensors"),
    },
    DwdRoadWeatherObservationParameter.MINUTE_10.ROAD_SURFACE_CONDITION: {
        "filters": {},
        "columns": ("shortStationName", "timePeriod", "positionOfRoadSensors"),
    },
    DwdRoadWeatherObservationParameter.MINUTE_10.WATER_FILM_THICKNESS: {
        "filters": {},
        "columns": ("shortStationName", "timePeriod"),
    },
    DwdRoadWeatherObservationParameter.MINUTE_10.TEMPERATURE_AIR: {
        "filters": {},
        "columns": (
            "shortStationName",
            "heightOfSensorAboveLocalGroundOrDeckOfMarinePlatform",
        ),
    },
    DwdRoadWeatherObservationParameter.MINUTE_10.DEW_POINT: {
        "filters": {},
        "columns": (
            "shortStationName",
            "heightOfSensorAboveLocalGroundOrDeckOfMarinePlatform",
        ),
    },
    DwdRoadWeatherObservationParameter.MINUTE_10.RELATIVE_HUMIDITY: {
        "filters": {},
        "columns": (
            "shortStationName",
            "heightOfSensorAboveLocalGroundOrDeckOfMarinePlatform",
        ),
    },
    DwdRoadWeatherObservationParameter.MINUTE_10.WIND_DIRECTION: {
        "filters": {},
        "columns": (
            "shortStationName",
            "heightOfSensorAboveLocalGroundOrDeckOfMarinePlatform",
        ),
    },
    DwdRoadWeatherObservationParameter.MINUTE_10.WIND: {
        "filters": {},
        "columns": (
            "shortStationName",
            "heightOfSensorAboveLocalGroundOrDeckOfMarinePlatform",
        ),
    },
    DwdRoadWeatherObservationParameter.MINUTE_10.WIND_EXTREME: {
        "filters": {},
        "columns": (
            "shortStationName",
            "timePeriod",
            "heightOfSensorAboveLocalGroundOrDeckOfMarinePlatform",
        ),
    },
    DwdRoadWeatherObservationParameter.MINUTE_10.WIND_EXTREME_DIRECTION: {
        "filters": {},
        "columns": (
            "shortStationName",
            "timePeriod",
            "heightOfSensorAboveLocalGroundOrDeckOfMarinePlatform",
        ),
    },
    DwdRoadWeatherObservationParameter.MINUTE_10.PRECIPITATION_TYPE: {
        "filters": {},
        "columns": ("shortStationName", "timePeriod"),
    },
    DwdRoadWeatherObservationParameter.MINUTE_10.TOTAL_PRECIPITATION: {
        "filters": {},
        "columns": ("shortStationName", "timePeriod"),
    },
    DwdRoadWeatherObservationParameter.MINUTE_10.INTENSITY_OF_PRECIPITATION: {
        "filters": {},
        "columns": ("shortStationName", "timePeriod"),
    },
    DwdRoadWeatherObservationParameter.MINUTE_10.INTENSITY_OF_PHENOMENA: {
        "filters": {},
        "columns": ("shortStationName", "timePeriod"),
    },
    DwdRoadWeatherObservationParameter.MINUTE_10.HORIZONTAL_VISIBILITY: {
        "filters": {},
        "columns": ("shortStationName",),
    },
}


class DwdRoadWeatherObservationUnit(DatasetTreeCore):
    """
    enumeration for different parameter/variables
    measured by dwd road weather stations
    """

    class MINUTE_10(UnitEnum):
        ROAD_SURFACE_TEMPERATURE = OriginUnit.DEGREE_CELSIUS.value, SIUnit.DEGREE_KELVIN.value
        TEMPERATURE_AIR = OriginUnit.DEGREE_CELSIUS.value, SIUnit.DEGREE_KELVIN.value
        ROAD_SURFACE_CONDITION = OriginUnit.DIMENSIONLESS.value, OriginUnit.DIMENSIONLESS.value
        WATER_FILM_THICKNESS = OriginUnit.CENTIMETER.value, SIUnit.METER.value
        WIND_EXTREME = OriginUnit.METER_PER_SECOND.value, SIUnit.METER_PER_SECOND.value
        WIND_EXTREME_DIRECTION = OriginUnit.DEGREE.value, SIUnit.DEGREE.value
        WIND_DIRECTION = OriginUnit.DEGREE.value, SIUnit.DEGREE.value
        WIND = OriginUnit.METER_PER_SECOND.value, SIUnit.METER_PER_SECOND.value
        DEW_POINT = OriginUnit.DEGREE_CELSIUS.value, SIUnit.DEGREE_KELVIN.value
        RELATIVE_HUMIDITY = OriginUnit.PERCENT.value, SIUnit.PERCENT.value
        TEMPERATURE_SOIL = OriginUnit.DEGREE_CELSIUS.value, SIUnit.DEGREE_KELVIN.value
        VISIBILITY_RANGE = OriginUnit.KILOMETER.value, SIUnit.METER.value
        PRECIPITATION_TYPE = OriginUnit.DIMENSIONLESS.value, OriginUnit.DIMENSIONLESS.value
        TOTAL_PRECIPITATION = OriginUnit.MILLIMETER.value, SIUnit.KILOGRAM_PER_SQUARE_METER.value
        INTENSITY_OF_PRECIPITATION = OriginUnit.MILLIMETER_PER_HOUR.value, SIUnit.MILLIMETER_PER_HOUR.value
        INTENSITY_OF_PHENOMENA = OriginUnit.DIMENSIONLESS.value, OriginUnit.DIMENSIONLESS.value
        HORIZONTAL_VISIBILITY = OriginUnit.KILOMETER.value, SIUnit.METER.value


class DwdRoadWeatherObservationResolution(Enum):
    MINUTE_10 = Resolution.MINUTE_10.value


class DwdRoadWeatherObservationPeriod(Enum):
    HISTORICAL = Period.HISTORICAL.value


class DwdRoadWeatherObservationDataset(Enum):
    MINUTE_10 = Resolution.MINUTE_10.value


class DwdObservationRoadWeatherStationGroup(Enum):
    """
    enumeration for road weather subset groups
    """

    DD = "DD"
    DF = "DF"
    ER = "ER"
    FN = "FN"
    HJ = "HJ"
    HL = "HL"
    HS = "HS"
    HV = "HV"
    JA = "JA"
    KK = "KK"
    KM = "KM"
    KO = "KO"
    LF = "LF"
    LH = "LH"
    LW = "LW"
    MC = "MC"
    NC = "NC"
    ND = "ND"
    RB = "RB"
    RH = "RH"
    SF = "SF"
    SP = "SP"
    WW = "WW"
    XX = "XX"


def parse_dwd_road_weather_data(
    filenames_and_files: List[Tuple[str, BytesIO]],
) -> pd.DataFrame:
    """
    This function is used to read the road weather station data from given bytes object.
    The filename is required to defined if and where an error happened.

    Args:
        filenames_and_files: list of tuples of a filename and its local stored file
        that should be read

    Returns:
        pandas.DataFrame with requested data, for different station ids the data is
        still put into one DataFrame
    """
    return pd.concat([_parse_dwd_road_weather_data(filename_and_file) for filename_and_file in filenames_and_files])


def _parse_dwd_road_weather_data(
    filename_and_file: Tuple[str, BytesIO],
) -> pd.DataFrame:
    """
    A wrapping function that only handles data for one station id. The files passed to
    it are thus related to this id. This is important for storing the data locally as
    the DataFrame that is stored should obviously only handle one station at a time.
    Args:
        filename_and_file: the files belonging to one station
        resolution: enumeration of time resolution used to correctly parse the
        date field
    Returns:
        pandas.DataFrame with data from that station, acn be empty if no data is
        provided or local file is not found or has no data in it
    """
    _, bytes_file = filename_and_file

    with TemporaryDirectory() as tempdir:

        tempfile = Path(tempdir) / "bufr_temp.bufr"

        tempfile.parent.mkdir(exist_ok=True)

        tempfile.write_bytes(bytes_file.read())

        data = {}
        for key, item in COLUMNS_FILTER_MAPPING.items():
            if item["filters"]:
                for filter_for_arg, arguments in item["filters"].items():
                    for arg in arguments:
                        data[f"{key.value}_{filter_for_arg}_{arg}"] = pdbufr.read_bufr(
                            tempfile,
                            columns=item["columns"] + TIME_COLUMNS + (key.value,),
                            filters={filter_for_arg: arg},
                        )
            else:
                data[key.value] = pdbufr.read_bufr(
                    tempfile,
                    columns=item["columns"] + TIME_COLUMNS + (key.value,),
                )

        tempfile.unlink()

    return pd.concat(
        [_adding_multiindex_and_drop_unused_columns(item) for _, item in data.items() if not item.empty],
        axis=1,
    )


def _adding_multiindex_and_drop_unused_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    """helping function to restructure data from bufr files"""

    dataframe.index = pd.MultiIndex.from_tuples(
        [
            (
                datetime(row["year"], row["month"], row["day"], row["hour"], row["minute"]),
                row["shortStationName"],
                row["timePeriod"]
                if "timePeriod" in row.index and row["timePeriod"] is not None
                else DEFAULT_TIME_PERIOD,
                row["heightOfSensorAboveLocalGroundOrDeckOfMarinePlatform"]
                if "heightOfSensorAboveLocalGroundOrDeckOfMarinePlatform" in row.index
                and row["heightOfSensorAboveLocalGroundOrDeckOfMarinePlatform"] is not None
                else DEFAULT_SENSOR_HEIGHT,
                row["positionOfRoadSensors"]
                if "positionOfRoadSensors" in row.index and row["positionOfRoadSensors"] is not None
                else DEFAULT_SENSOR_POSITION,
            )
            for idx, row in dataframe.iterrows()
        ],
        names=[
            "timestamp",
            "shortStationName",
            "timePeriod",
            "sensorHeight",
            "sensorPosition",
        ],
    )
    dataframe.sort_index(inplace=True)
    dataframe.drop(
        ["year", "month", "day", "hour", "minute", "shortStationName"],
        axis=1,
        inplace=True,
    )
    if "timePeriod" in dataframe.columns:
        dataframe.drop(["timePeriod"], axis=1, inplace=True)
    if "heightOfSensorAboveLocalGroundOrDeckOfMarinePlatform" in dataframe.columns:
        dataframe.drop(
            ["heightOfSensorAboveLocalGroundOrDeckOfMarinePlatform"],
            axis=1,
            inplace=True,
        )
    if "positionOfRoadSensors" in dataframe.columns:
        dataframe.drop(["positionOfRoadSensors"], axis=1, inplace=True)
    return dataframe.loc[~dataframe.index.duplicated(keep="first")]


def create_file_index_for_dwd_road_weather_station(
    road_weather_station_group: "DwdObservationRoadWeatherStationGroup",
) -> pd.DataFrame:
    """
    Creates a file_index DataFrame from RoadWeather Station directory
    """

    df = _list_remote_files_as_dataframe(
        reduce(
            urljoin,
            [DWD_SERVER, DWD_ROAD_WEATHER_REPORTS, road_weather_station_group.value],
        )
    )

    df[Columns.DATE.value] = df[Columns.FILENAME.value].str.extract(DATE_REGEX)

    df[Columns.DATE.value] = pd.to_datetime(df[Columns.DATE.value], format="%y%m%d%H%S", utc=True)

    return df


def download_road_weather_observations_parallel(
    remote_files: List[str],
) -> List[Tuple[str, BytesIO]]:
    """
    Wrapper for ``_download_dwd_data`` to provide a multiprocessing feature.
    :param remote_files:    List of requested files
    :return:                List of downloaded files
    """
    files_in_bytes = []
    for file in remote_files:
        files_in_bytes.append(download_file(file, CacheExpiry.TWELVE_HOURS))

    return list(zip(remote_files, files_in_bytes))


class DwdRoadWeatherObservationValues(ScalarValuesCore):
    """
    The DwdRoadWeatherObservationValues class represents a request for
    observation data from road weather stations as provided by the DWD service.
    """

    _tz = Timezone.GERMANY
    _data_tz = Timezone.UTC

    _date_parameters = ()
    _irregular_parameters = ()
    _string_parameters = ()

    def _collect_station_parameter(self, station_id: str, parameter: Enum, dataset: Enum) -> pd.DataFrame:
        """Takes station_name to download and parse RoadWeather Station data"""
        station_group = self.sr.df.loc[
            self.sr.df[Columns.STATION_ID.value] == station_id, Columns.STATION_GROUP.value
        ].item()

        station_group = DwdObservationRoadWeatherStationGroup(station_group)

        try:
            road_weather_station_data = self._collect_data_by_station_group(station_group)
        except ValueError:
            return pd.DataFrame()

        road_weather_station_data = road_weather_station_data.reset_index()

        road_weather_station_data = road_weather_station_data.rename(
            columns={"timestamp": Columns.DATE.value, "shortStationName": Columns.STATION_ID.value}
        )

        road_weather_station_data = road_weather_station_data.drop(
            columns=["timePeriod", "sensorHeight", "sensorPosition"]
        ).rename(columns=str.lower)

        return (
            road_weather_station_data.loc[road_weather_station_data[Columns.STATION_ID.value] == station_id]
            .groupby(Columns.DATE.value)
            .take([0]).reset_index()
        )

    def _collect_data_by_station_group(
        self,
        road_weather_station_group: DwdObservationRoadWeatherStationGroup,
    ) -> pd.DataFrame:
        """
        Method to collect data for one specified parameter. Manages restoring,
        collection and storing of data, transformation and combination of different
        periods.

        Args:
            road_weather_station_group: subset id for which parameter is collected

        Returns:
            pandas.DataFrame for given parameter of station
        """
        remote_files = create_file_index_for_dwd_road_weather_station(road_weather_station_group)

        if self.sr.start_date:
            remote_files = remote_files.loc[
                (remote_files[Columns.DATE.value] >= self.sr.start_date)
                & (remote_files[Columns.DATE.value] <= self.sr.end_date),
                :,
            ]

        remote_files = remote_files[Columns.FILENAME.value].tolist()

        filenames_and_files = download_road_weather_observations_parallel(remote_files)

        return parse_dwd_road_weather_data(filenames_and_files)

    def _tidy_up_df(self, df: pd.DataFrame, dataset) -> pd.DataFrame:
        return df.melt(
            id_vars=[Columns.DATE.value, Columns.STATION_ID.value],
            var_name=Columns.PARAMETER.value,
            value_name=Columns.VALUE.value,
        ).reset_index(drop=True)


class DwdRoadWeatherObservationRequest(ScalarRequestCore):

    provider = Provider.DWD
    kind = Kind.OBSERVATION

    _tz = Timezone.GERMANY

    _values = DwdRoadWeatherObservationValues

    _has_tidy_data = False

    _has_datasets = True
    _unique_dataset = True

    _data_range = DataRange.FIXED

    _parameter_base = DwdRoadWeatherObservationParameter
    _unit_tree = DwdRoadWeatherObservationUnit

    _resolution_base = DwdRoadWeatherObservationResolution
    _resolution_type = ResolutionType.FIXED

    _period_base = DwdRoadWeatherObservationPeriod
    _period_type = PeriodType.FIXED

    _dataset_base = DwdRoadWeatherObservationDataset

    _base_columns = list(ScalarRequestCore._base_columns)
    _base_columns.extend(
        (
            Columns.STATION_GROUP.value,
            Columns.ROAD_NAME.value,
            Columns.ROAD_SECTOR.value,
            Columns.ROAD_TYPE.value,
            Columns.ROAD_SURFACE_TYPE.value,
            Columns.ROAD_SURROUNDINGS_TYPE.value,
        )
    )

    _endpoint = (
        "https://www.dwd.de/DE/leistungen/opendata/help/stationen/sws_stations_xls.xlsx?__blob=publicationFile&v=11"
    )

    def __init__(self, parameter, start_date=None, end_date=None):
        super(DwdRoadWeatherObservationRequest, self).__init__(
            parameter=parameter,
            resolution=Resolution.MINUTE_10,
            period=Period.HISTORICAL,
            start_date=start_date,
            end_date=end_date,
        )

    def _all(self) -> pd.DataFrame:
        payload = download_file(self._endpoint, CacheExpiry.METAINDEX)

        df = pd.read_excel(payload)

        df = df.rename(
            columns={
                "Kennung": Columns.STATION_ID.value,
                "GMA-Name": Columns.NAME.value,
                "Bundesland  ": Columns.STATE.value,
                "Straße / Fahrtrichtung": Columns.ROAD_NAME.value,
                "Strecken-kilometer 100 m": Columns.ROAD_SECTOR.value,
                'Streckenlage (Register "Typen")': Columns.ROAD_SURROUNDINGS_TYPE.value,
                'Streckenbelag (Register "Typen")': Columns.ROAD_SURFACE_TYPE.value,
                "Breite (Dezimalangabe)": Columns.LATITUDE.value,
                "Länge (Dezimalangabe)": Columns.LONGITUDE.value,
                "Höhe in m über NN": Columns.HEIGHT.value,
                "GDS-Verzeichnis": Columns.STATION_GROUP.value,
                "außer Betrieb (gemeldet)": Columns.HAS_FILE.value,
            }
        )

        df = df.loc[df[Columns.HAS_FILE.value].isna() & df[Columns.STATION_GROUP.value] != 0, :]

        df[Columns.LONGITUDE.value] = df[Columns.LONGITUDE.value].replace(",", ".", regex=True).astype(float)
        df[Columns.LATITUDE.value] = df[Columns.LATITUDE.value].replace(",", ".", regex=True).astype(float)

        return df

    def filter_by_station_group(self):
        pass


if __name__ == "__main__":
    request = DwdRoadWeatherObservationRequest(
        "airTemperature", start_date="2022-10-09", end_date="2022-10-10"
    ).filter_by_station_id("A006")
    print(
        request.df,
    )
    values = request.values.all()
    print(values.df)
