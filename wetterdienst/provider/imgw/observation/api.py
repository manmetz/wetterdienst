from datetime import datetime
from enum import Enum
from typing import Optional, Union

import pandas as pd
from pyoscar import OSCARClient

from wetterdienst import Kind, Period, Provider, Resolution
from wetterdienst.core.scalar.request import ScalarRequestCore
from wetterdienst.metadata.columns import Columns
from wetterdienst.metadata.datarange import DataRange
from wetterdienst.metadata.period import PeriodType
from wetterdienst.metadata.resolution import ResolutionType
from wetterdienst.metadata.timezone import Timezone
from wetterdienst.metadata.unit import OriginUnit, SIUnit
from wetterdienst.util.cache import CacheExpiry
from wetterdienst.util.network import download_file
from wetterdienst.util.parameter import DatasetTreeCore


class ImgwObservationParameter(DatasetTreeCore):
    class DAILY(DatasetTreeCore):
        class DAILY(Enum):
            TEMPERATURE_AIR_MAX_200 = "Maksymalna temperatura dobowa [°C]"

        TEMPERATURE_AIR_MAX_200 = DAILY.TEMPERATURE_AIR_MAX_200


class ImgwObservationUnit(DatasetTreeCore):
    class DAILY(DatasetTreeCore):
        class DAILY(Enum):
            TEMPERATURE_AIR_MAX_200 = OriginUnit.DEGREE_CELSIUS.value, SIUnit.DEGREE_KELVIN.value


class ImgwObservationDataset(Enum):
    DAILY = "daily"


class ImgwObservationResolution(Enum):
    DAILY = "dobowe"


class ImgwObservationPeriod(Enum):
    HISTORICAL = Period.HISTORICAL


class ImgwObservationRequest(ScalarRequestCore):
    provider = Provider.IMGW
    kind = Kind.OBSERVATION
    _tz = Timezone.POLAND

    _parameter_base = ImgwObservationParameter
    _unit_tree = ImgwObservationUnit

    _has_datasets = True
    _has_tidy_data = False
    _unique_dataset = True
    _dataset_base = ImgwObservationDataset

    _data_range = DataRange.FIXED

    _resolution_base = ImgwObservationResolution
    _resolution_type = ResolutionType.MULTI
    _period_type = PeriodType.FIXED
    _period_base = ImgwObservationPeriod

    _values = None

    _endpoint = "https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/wykaz_stacji.csv"
    _endpoint2 = "https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/mapa_zawartosci_synop.pdf"

    _pyosclient = OSCARClient()

    def __init__(
        self,
        parameter,
        resolution,
        start_date: Optional[Union[str, datetime, pd.Timestamp]] = None,
        end_date: Optional[Union[str, datetime, pd.Timestamp]] = None,
    ):
        super(ImgwObservationRequest, self).__init__(
            parameter=parameter,
            resolution=resolution,
            start_date=start_date,
            end_date=end_date,
            period=Period.HISTORICAL,
        )

    def _all(self) -> pd.DataFrame:
        payload = download_file(self._endpoint, CacheExpiry.METAINDEX)

        df = pd.read_csv(payload, encoding="latin-1", header=None)

        df.columns = [Columns.STATION_ID.value, Columns.NAME.value, None]

        print(df)

        wmo_stations = self._pyosclient.get_stations(country="POL")

        df_wmo = pd.DataFrame.from_records(wmo_stations["stationSearchResults"]).loc[:, ["name"]].rename(columns={"name": "wmo"})

        print(df_wmo)

        df_merged = df.merge(df_wmo, left_on="name", right_on="wmo", how="outer")

        df_merged.to_csv("stations_comparison.csv", index=False)

        exit()

        # df = df.loc[df.iloc[:, 0].notna(), :]
        #
        # if df.columns[0] == "Kod METEO Nazwa stacji":
        #     kodmet_nazwa = df.pop("Kod METEO Nazwa stacji")
        #     kodmet_nazwa = kodmet_nazwa.map(lambda x: (x[:x.index(" ")], x[x.index(" "):]))

        # df.loc[:, ["meteocode", Columns.NAME.value]] = kodmet_nazwa.tolist()


        print(df)

        return df


if __name__ == "__main__":
    request = ImgwObservationRequest(
        parameter=ImgwObservationParameter.DAILY.TEMPERATURE_AIR_MAX_200, resolution=ImgwObservationResolution.DAILY
    ).all()

    print(request.df)

