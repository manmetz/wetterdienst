# -*- coding: utf-8 -*-
# Copyright (C) 2018-2021, earthobservations developers.
# Distributed under the MIT License. See LICENSE for more info.
from enum import Enum


class Parameter(Enum):
    """Parameter enum with fixed names of parameters being used in the entire library.

    Groups are:
        - Clouds
        - Evapotranspiration / Evaporation
        - Fog
        - Humidity
        - Ice
        - Precipitation
        - Pressure
        - Radiation
        - Snow
        - Soil
        - Solar
        - Special
            - special parameters which may not be sorted elsewhere
        - Temperature
        - Visibility
        - Water equivalent
        - Weather / Weather phenomena
        - Wind

    Subgroups are:
        - averaged
        - aggregated
        - instant
        - duration
        - type
        - distance/length
        - probability
        - percentage/frequency
        - error (model related e.g. Mosmix)
        - count
        - time

    """

    # Clouds
    # ---- averaged ----
    # total
    CLOUD_COVER_TOTAL = "CLOUD_COVER_TOTAL"
    CLOUD_COVER_TOTAL_MIDNIGHT_TO_MIDNIGHT = "CLOUD_COVER_TOTAL_MIDNIGHT_TO_MIDNIGHT"
    CLOUD_COVER_TOTAL_MIDNIGHT_TO_MIDNIGHT_MANUAL = "CLOUD_COVER_TOTAL_MIDNIGHT_TO_MIDNIGHT_MANUAL"
    CLOUD_COVER_TOTAL_SUNRISE_TO_SUNSET = "CLOUD_COVER_TOTAL_SUNRISE_TO_SUNSET"
    CLOUD_COVER_TOTAL_SUNRISE_TO_SUNSET_MANUAL = "CLOUD_COVER_TOTAL_SUNRISE_TO_SUNSET_MANUAL"
    CLOUD_COVER_EFFECTIVE = "CLOUD_COVER_EFFECTIVE"
    # layers
    CLOUD_COVER_LAYER1 = "CLOUD_COVER_LAYER1"
    CLOUD_COVER_LAYER2 = "CLOUD_COVER_LAYER2"
    CLOUD_COVER_LAYER3 = "CLOUD_COVER_LAYER3"
    CLOUD_COVER_LAYER4 = "CLOUD_COVER_LAYER4"
    # below - above
    CLOUD_COVER_BELOW_500_FT = "CLOUD_COVER_BELOW_500_FT"
    CLOUD_COVER_BELOW_1000_FT = "CLOUD_COVER_BELOW_1000_FT"
    CLOUD_COVER_BETWEEN_2_TO_7_KM = "CLOUD_COVER_BETWEEN_2_TO_7_KM"
    CLOUD_COVER_BELOW_7_KM = "CLOUD_COVER_BELOW_7_KM"
    CLOUD_COVER_ABOVE_7_KM = "CLOUD_COVER_ABOVE_7_KM"
    # density
    CLOUD_DENSITY = "CLOUD_DENSITY"
    # ---- type ----
    CLOUD_TYPE_LAYER1 = "CLOUD_TYPE_LAYER1"
    CLOUD_TYPE_LAYER2 = "CLOUD_TYPE_LAYER2"
    CLOUD_TYPE_LAYER3 = "CLOUD_TYPE_LAYER3"
    CLOUD_TYPE_LAYER4 = "CLOUD_TYPE_LAYER4"
    CLOUD_COVER_TOTAL_INDEX = "CLOUD_COVER_TOTAL_INDEX"
    # ---- distance ----
    CLOUD_HEIGHT_LAYER1 = "CLOUD_HEIGHT_LAYER1"
    CLOUD_HEIGHT_LAYER2 = "CLOUD_HEIGHT_LAYER2"
    CLOUD_HEIGHT_LAYER3 = "CLOUD_HEIGHT_LAYER3"
    CLOUD_HEIGHT_LAYER4 = "CLOUD_HEIGHT_LAYER4"
    # cloud base height
    CLOUD_BASE_CONVECTIVE = "CLOUD_BASE_CONVECTIVE"
    # ---- abbreviation ----
    CLOUD_TYPE_LAYER1_ABBREVIATION = "CLOUD_TYPE_LAYER1_ABBREVIATION"
    CLOUD_TYPE_LAYER2_ABBREVIATION = "CLOUD_TYPE_LAYER2_ABBREVIATION"
    CLOUD_TYPE_LAYER3_ABBREVIATION = "CLOUD_TYPE_LAYER3_ABBREVIATION"
    CLOUD_TYPE_LAYER4_ABBREVIATION = "CLOUD_TYPE_LAYER4_ABBREVIATION"

    # Evapotranspiration
    # ---- aggregated ----
    EVAPOTRANSPIRATION_POTENTIAL_LAST_24H = "EVAPOTRANSPIRATION_POTENTIAL_LAST_24H"
    EVAPORATION_HEIGHT = "EVAPORATION_HEIGHT"
    EVAPORATION_HEIGHT_MULTIDAY = "EVAPORATION_HEIGHT_MULTIDAY"
    # ---- count ----
    # Number of days included in the multiday evaporation total
    COUNT_DAYS_MULTIDAY_EVAPORATION = "COUNT_DAYS_MULTIDAY_EVAPORATION"

    # Fog
    # ---- probability ----
    PROBABILITY_FOG_LAST_1H = "PROBABILITY_FOG_LAST_1H"
    PROBABILITY_FOG_LAST_6H = "PROBABILITY_FOG_LAST_6H"
    PROBABILITY_FOG_LAST_12H = "PROBABILITY_FOG_LAST_12H"
    PROBABILITY_FOG_LAST_24H = "PROBABILITY_FOG_LAST_24H"

    # Humidity
    # ---- averaged ----
    HUMIDITY = "HUMIDITY"
    HUMIDITY_ABSOLUTE = "HUMIDITY_ABSOLUTE"
    # ECCC special parameter
    HUMIDEX = "HUMIDEX"

    # Ice
    # ---- length ----
    ICE_ON_WATER_THICKNESS = "THICKNESS_OF_ICE_ON_WATER"

    # Precipitation
    # ---- aggregated ----
    PRECIPITATION_HEIGHT = "PRECIPITATION_HEIGHT"
    PRECIPITATION_HEIGHT_LIQUID = "PRECIPITATION_HEIGHT_LIQUID"
    PRECIPITATION_HEIGHT_DROPLET = "PRECIPITATION_HEIGHT_DROPLET"
    PRECIPITATION_HEIGHT_ROCKER = "PRECIPITATION_HEIGHT_ROCKER"
    PRECIPITATION_HEIGHT_LAST_1H = "PRECIPITATION_HEIGHT_LAST_1H"
    PRECIPITATION_HEIGHT_LAST_3H = "PRECIPITATION_HEIGHT_LAST_3H"
    PRECIPITATION_HEIGHT_LAST_6H = "PRECIPITATION_HEIGHT_LAST_6H"
    PRECIPITATION_HEIGHT_LAST_12H = "PRECIPITATION_HEIGHT_LAST_12H"
    PRECIPITATION_HEIGHT_LAST_24H = "PRECIPITATION_HEIGHT_LAST_24H"
    PRECIPITATION_HEIGHT_MULTIDAY = "PRECIPITATION_HEIGHT_MULTIDAY"
    # precipitation height consistent with significant weather
    PRECIPITATION_HEIGHT_SIGNIFICANT_WEATHER_LAST_1H = "PRECIPITATION_HEIGHT_SIGNIFICANT_WEATHER_LAST_1H"
    PRECIPITATION_HEIGHT_SIGNIFICANT_WEATHER_LAST_3H = "PRECIPITATION_HEIGHT_SIGNIFICANT_WEATHER_LAST_3H"
    PRECIPITATION_HEIGHT_SIGNIFICANT_WEATHER_LAST_6H = "PRECIPITATION_HEIGHT_SIGNIFICANT_WEATHER_LAST_6H"
    PRECIPITATION_HEIGHT_SIGNIFICANT_WEATHER_LAST_12H = "PRECIPITATION_HEIGHT_SIGNIFICANT_WEATHER_LAST_12H"
    PRECIPITATION_HEIGHT_SIGNIFICANT_WEATHER_LAST_24H = "PRECIPITATION_HEIGHT_SIGNIFICANT_WEATHER_LAST_24H"
    PRECIPITATION_HEIGHT_LIQUID_SIGNIFICANT_WEATHER_LAST_1H = "PRECIPITATION_HEIGHT_LIQUID_SIGNIFICANT_WEATHER_LAST_1H"
    # ---- extremes ----
    PRECIPITATION_HEIGHT_MAX = "PRECIPITATION_HEIGHT_MAX"
    PRECIPITATION_HEIGHT_LIQUID_MAX = "PRECIPITATION_HEIGHT_LIQUID_MAX"
    # ---- type ----
    PRECIPITATION_FORM = "PRECIPITATION_FORM"  # what type of precipitation, snow, ice?
    PRECIPITATION_INDEX = "PRECIPITATION_INDEX"  # True or False
    # ---- duration ----
    PRECIPITATION_DURATION = "PRECIPITATION_DURATION"
    # ---- probability ----
    # greater 0
    PROBABILITY_PRECIPITATION_HEIGHT_GT_0_0_MM_LAST_6H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_0_0_MM_LAST_6H"
    PROBABILITY_PRECIPITATION_HEIGHT_GT_0_0_MM_LAST_12H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_0_0_MM_LAST_12H"
    PROBABILITY_PRECIPITATION_HEIGHT_GT_0_0_MM_LAST_24H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_0_0_MM_LAST_24H"
    # greater 0.1
    PROBABILITY_PRECIPITATION_HEIGHT_GT_0_1_MM_LAST_1H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_0_1_MM_LAST_1H"
    # greater 0.2
    PROBABILITY_PRECIPITATION_HEIGHT_GT_0_2_MM_LAST_1H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_0_2_MM_LAST_1H"
    PROBABILITY_PRECIPITATION_HEIGHT_GT_0_2_MM_LAST_6H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_0_2_MM_LAST_6H"
    PROBABILITY_PRECIPITATION_HEIGHT_GT_0_2_MM_LAST_12H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_0_2_MM_LAST_12H"
    PROBABILITY_PRECIPITATION_HEIGHT_GT_0_2_MM_LAST_24H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_0_2_MM_LAST_24H"
    # greater 0.3
    PROBABILITY_PRECIPITATION_HEIGHT_GT_0_3_MM_LAST_1H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_0_3_MM_LAST_1H"
    # greater 0.5
    PROBABILITY_PRECIPITATION_HEIGHT_GT_0_5_MM_LAST_1H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_0_5_MM_LAST_1H"
    # greater 0.7
    PROBABILITY_PRECIPITATION_HEIGHT_GT_0_7_MM_LAST_1H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_0_7_MM_LAST_1H"
    # greater 1.0
    PROBABILITY_PRECIPITATION_HEIGHT_GT_1_0_MM_LAST_1H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_1_0_MM_LAST_1H"
    PROBABILITY_PRECIPITATION_HEIGHT_GT_1_0_MM_LAST_6H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_1_0_MM_LAST_6H"
    PROBABILITY_PRECIPITATION_HEIGHT_GT_1_0_MM_LAST_12H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_1_0_MM_LAST_12H"
    PROBABILITY_PRECIPITATION_HEIGHT_GT_1_0_MM_LAST_24H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_1_0_MM_LAST_24H"
    # greater 2.0
    PROBABILITY_PRECIPITATION_HEIGHT_GT_2_0_MM_LAST_1H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_2_0_MM_LAST_1H"
    # greater 3.0
    PROBABILITY_PRECIPITATION_HEIGHT_GT_3_0_MM_LAST_1H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_3_0_MM_LAST_1H"
    # greater 5.0
    PROBABILITY_PRECIPITATION_HEIGHT_GT_5_0_MM_LAST_1H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_5_0_MM_LAST_1H"
    PROBABILITY_PRECIPITATION_HEIGHT_GT_5_0_MM_LAST_6H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_5_0_MM_LAST_6H"
    PROBABILITY_PRECIPITATION_HEIGHT_GT_5_0_MM_LAST_12H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_5_0_MM_LAST_12H"
    PROBABILITY_PRECIPITATION_HEIGHT_GT_5_0_MM_LAST_24H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_5_0_MM_LAST_24H"
    # greater 10.0
    PROBABILITY_PRECIPITATION_HEIGHT_GT_10_0_MM_LAST_1H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_10_0_MM_LAST_1H"
    # greater 15.0
    PROBABILITY_PRECIPITATION_HEIGHT_GT_15_0_MM_LAST_1H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_15_0_MM_LAST_1H"
    PROBABILITY_PRECIPITATION_HEIGHT_GT_25_0_MM_LAST_1H = "PROBABILITY_PRECIPITATION_HEIGHT_GT_25_0_MM_LAST_1H"

    PROBABILITY_PRECIPITATION_LAST_1H = "PROBABILITY_PRECIPITATION_LAST_1H"
    PROBABILITY_PRECIPITATION_LAST_6H = "PROBABILITY_PRECIPITATION_LAST_6H"
    PROBABILITY_PRECIPITATION_LAST_12H = "PROBABILITY_PRECIPITATION_LAST_12H"
    PROBABILITY_PRECIPITATION_LAST_24H = "PROBABILITY_PRECIPITATION_LAST_24H"

    PROBABILITY_DRIZZLE_LAST_1H = "PROBABILITY_DRIZZLE_LAST_1H"
    PROBABILITY_DRIZZLE_LAST_6H = "PROBABILITY_DRIZZLE_LAST_6H"
    PROBABILITY_DRIZZLE_LAST_12H = "PROBABILITY_DRIZZLE_LAST_12H"

    PROBABILITY_PRECIPITATION_STRATIFORM_LAST_1H = "PROBABILITY_PRECIPITATION_STRATIFORM_LAST_1H"
    PROBABILITY_PRECIPITATION_STRATIFORM_LAST_6H = "PROBABILITY_PRECIPITATION_STRATIFORM_LAST_6H"
    PROBABILITY_PRECIPITATION_STRATIFORM_LAST_12H = "PROBABILITY_PRECIPITATION_STRATIFORM_LAST_12H"

    PROBABILITY_PRECIPITATION_CONVECTIVE_LAST_1H = "PROBABILITY_PRECIPITATION_CONVECTIVE_LAST_1H"
    PROBABILITY_PRECIPITATION_CONVECTIVE_LAST_6H = "PROBABILITY_PRECIPITATION_CONVECTIVE_LAST_6H"
    PROBABILITY_PRECIPITATION_CONVECTIVE_LAST_12H = "PROBABILITY_PRECIPITATION_CONVECTIVE_LAST_12H"

    PROBABILITY_PRECIPITATION_LIQUID_LAST_1H = "PROBABILITY_PRECIPITATION_LIQUID_LAST_1H"
    PROBABILITY_PRECIPITATION_LIQUID_LAST_6H = "PROBABILITY_PRECIPITATION_LIQUID_LAST_6H"
    PROBABILITY_PRECIPITATION_LIQUID_LAST_12H = "PROBABILITY_PRECIPITATION_LIQUID_LAST_12H"

    PROBABILITY_PRECIPITATION_SOLID_LAST_1H = "PROBABILITY_PRECIPITATION_SOLID_LAST_1H"
    PROBABILITY_PRECIPITATION_SOLID_LAST_6H = "PROBABILITY_PRECIPITATION_SOLID_LAST_6H"
    PROBABILITY_PRECIPITATION_SOLID_LAST_12H = "PROBABILITY_PRECIPITATION_SOLID_LAST_12H"

    PROBABILITY_PRECIPITATION_FREEZING_LAST_1H = "PROBABILITY_PRECIPITATION_FREEZING_LAST_1H"
    PROBABILITY_PRECIPITATION_FREEZING_LAST_6H = "PROBABILITY_PRECIPITATION_FREEZING_LAST_6H"
    PROBABILITY_PRECIPITATION_FREEZING_LAST_12H = "PROBABILITY_PRECIPITATION_FREEZING_LAST_12H"
    # ---- frequency ----
    PRECIPITATION_FREQUENCY = "PRECIPITATION_FREQUENCY"
    # ---- count ----
    # Number of days included in the multiday precipitation total
    COUNT_DAYS_MULTIDAY_PRECIPITATION = "COUNT_DAYS_MULTIDAY_PRECIPITATION"
    # Number of days with non-zero precipitation included in multiday precipitation total
    COUNT_DAYS_MULTIDAY_PRECIPITATION_HEIGHT_GT_0 = "COUNT_DAYS_MULTIDAY_PRECIPITATION_HEIGHT_GT_0"

    # PRESSURE
    # ---- averaged ----
    # TODO: should we add _MEAN here?
    PRESSURE_AIR_SITE = "PRESSURE_AIR_SITE"  # air pressure at station height [SH]
    PRESSURE_AIR_SITE_MAX = "PRESSURE_AIR_SITE_MAX"
    PRESSURE_AIR_SITE_MIN = "PRESSURE_AIR_SITE_MIN"
    PRESSURE_AIR_SITE_REDUCED = "PRESSURE_AIR_SITE_REDUCED"
    PRESSURE_AIR_SEA_LEVEL = "PRESSURE_AIR_SEA_LEVEL"  # air pressure at sea level [SL]
    PRESSURE_VAPOR = "PRESSURE_VAPOR"
    # ---- error ----
    ERROR_ABSOLUTE_PRESSURE_AIR_SITE = "ERROR_ABSOLUTE_PRESSURE_AIR_SITE"

    # RADIATION
    # ---- averaged ----
    RADIATION_SKY_SHORT_WAVE_DIFFUSE = "RADIATION_SKY_SHORT_WAVE_DIFFUSE"
    RADIATION_SKY_SHORT_WAVE_DIRECT = "RADIATION_SKY_SHORT_WAVE_DIRECT"
    # sum of short wave radiation a.k.a. RADIATION_SKY_SHORT_WAVE_TOTAL
    RADIATION_GLOBAL = "RADIATION_GLOBAL"
    RADIATION_GLOBAL_LAST_3H = "RADIATION_GLOBAL_LAST_3H"
    RADIATION_SKY_LONG_WAVE = "RADIATION_SKY_LONG_WAVE"
    RADIATION_SKY_LONG_WAVE_LAST_3H = "RADIATION_SKY_LONG_WAVE_LAST_3H"
    # ---- probability ----
    PROBABILITY_RADIATION_GLOBAL_LAST_1H = "PROBABILITY_RADIATION_GLOBAL_LAST_1H"

    # SNOW
    # ---- distance ----
    SNOW_DEPTH = "SNOW_DEPTH"
    SNOW_DEPTH_NEW = "SNOW_DEPTH_NEW"  # difference to previous snow depth
    SNOW_DEPTH_EXCELLED = "SNOW_DEPTH_EXCELLED"  # with spade or some device
    SNOW_DEPTH_NEW_MULTIDAY = "SNOW_DEPTH_NEW_MULTIDAY"
    # ---- extremes ----
    SNOW_DEPTH_NEW_MAX = "SNOW_DEPTH_NEW_MAX"
    SNOW_DEPTH_MAX = "SNOW_DEPTH_MAX"
    # ---- count ----
    # Number of days included in the multiday snowfall total
    # TODO: maybe this should be COUNT_DAYS_MULTIDAY_SNOW_DEPTH instead
    COUNT_DAYS_MULTIDAY_SNOW_DEPTH_NEW = "COUNT_DAYS_MULTIDAY_SNOW_DEPTH"

    # SOIL
    FROZEN_GROUND_LAYER_BASE = "FROZEN_GROUND_LAYER_BASE"
    FROZEN_GROUND_LAYER_TOP = "FROZEN_GROUND_LAYER_TOP"
    FROZEN_GROUND_LAYER_THICKNESS = "FROZEN_GROUND_LAYER_THICKNESS"

    # SOLAR
    # ---- duration ----
    SUNSHINE_DURATION = "SUNSHINE_DURATION"
    SUNSHINE_DURATION_LAST_3H = "SUNSHINE_DURATION_LAST_3H"
    SUNSHINE_DURATION_YESTERDAY = "SUNSHINE_DURATION_YESTERDAY"
    # ---- angle ----
    SUN_ZENITH_ANGLE = "SUN_ZENITH_ANGLE"
    # ---- probability ----
    PROBABILITY_SUNSHINE_DURATION_RELATIVE_GT_0_PCT_LAST_24H = (
        "PROBABILITY_SUNSHINE_DURATION_RELATIVE_GT_0_PCT_LAST_24H"
    )
    PROBABILITY_SUNSHINE_DURATION_RELATIVE_GT_30_PCT_LAST_24H = (
        "PROBABILITY_SUNSHINE_DURATION_RELATIVE_GT_30_PCT_LAST_24H"
    )
    PROBABILITY_SUNSHINE_DURATION_RELATIVE_GT_60_PCT_LAST_24H = (
        "PROBABILITY_SUNSHINE_DURATION_RELATIVE_GT_60_PCT_LAST_24H"
    )
    # ---- percentage ----
    SUNSHINE_DURATION_RELATIVE = "SUNSHINE_DURATION_RELATIVE"
    SUNSHINE_DURATION_RELATIVE_LAST_24H = "SUNSHINE_DURATION_RELATIVE_LAST_24H"
    # ---- time ----
    TRUE_LOCAL_TIME = "TRUE_LOCAL_TIME"  # alt name: mean solar time

    # SPECIAL
    # ---- time ----
    END_OF_INTERVAL = "END_OF_INTERVAL"  # time based
    # ---- distance ----
    DISTANCE_RIVER_GAUGE_HEIGHT = "DIFFERENCE_RIVER_GAUGE_HEIGHT"

    # TEMPERATURE
    # ---- instant ----
    TEMPERATURE_AIR_200 = "TEMPERATURE_AIR_200"
    # ----- averaged ----
    TEMPERATURE_AIR_MEAN_005 = "TEMPERATURE_AIR_MEAN_005"
    TEMPERATURE_AIR_MEAN_200 = "TEMPERATURE_AIR_MEAN_200"
    TEMPERATURE_AIR_MEAN_200_LAST_24H = "TEMPERATURE_AIR_MEAN_200_LAST_24H"
    TEMPERATURE_AIR_MAX_200_LAST_24H = "TEMPERATURE_AIR_MAX_200_LAST_24H"
    TEMPERATURE_AIR_MIN_200_LAST_24H = "TEMPERATURE_AIR_MIN_200_LAST_24H"
    TEMPERATURE_AIR_MAX_200_MEAN = "TEMPERATURE_AIR_MAX_200_MEAN"
    TEMPERATURE_AIR_MIN_200_MEAN = "TEMPERATURE_AIR_MIN_200_MEAN"

    TEMPERATURE_DEW_POINT_MEAN_200 = "TEMPERATURE_DEW_POINT_MEAN_200"
    # wind chill temperature by NWS (https://www.weather.gov/gjt/windchill)
    TEMPERATURE_WIND_CHILL = "TEMPERATURE_WIND_CHILL"

    TEMPERATURE_SOIL_MEAN_002 = "TEMPERATURE_SOIL_MEAN_002"
    TEMPERATURE_SOIL_MEAN_005 = "TEMPERATURE_SOIL_MEAN_005"
    TEMPERATURE_SOIL_MEAN_010 = "TEMPERATURE_SOIL_MEAN_010"
    TEMPERATURE_SOIL_MEAN_020 = "TEMPERATURE_SOIL_MEAN_020"
    TEMPERATURE_SOIL_MEAN_050 = "TEMPERATURE_SOIL_MEAN_050"
    TEMPERATURE_SOIL_MEAN_100 = "TEMPERATURE_SOIL_MEAN_100"
    TEMPERATURE_SOIL_MEAN_200 = "TEMPERATURE_SOIL_MEAN_200"

    TEMPERATURE_WET_MEAN_200 = "TEMPERATURE_WET_MEAN_200"
    # ---- extremes ----
    TEMPERATURE_AIR_MAX_200 = "TEMPERATURE_AIR_MAX_200"
    TEMPERATURE_AIR_MAX_005 = "TEMPERATURE_AIR_MAX_005"
    TEMPERATURE_AIR_MIN_200 = "TEMPERATURE_AIR_MIN_200"
    TEMPERATURE_AIR_MIN_005 = "TEMPERATURE_AIR_MIN_005"

    TEMPERATURE_AIR_MIN_005_LAST_12H = "TEMPERATURE_AIR_MIN_005_LAST_12H"
    TEMPERATURE_AIR_MIN_200_MULTIDAY = "TEMPERATURE_AIR_MIN_200_MULTIDAY"
    TEMPERATURE_AIR_MAX_200_MULTIDAY = "TEMPERATURE_AIR_MAX_200_MULTIDAY"

    TEMPERATURE_WATER_EVAPORATION_PAN_MIN = "TEMPERATURE_WATER_EVAPORATION_PAN_MIN"
    TEMPERATURE_WATER_EVAPORATION_PAN_MAX = "TEMPERATURE_WATER_EVAPORATION_PAN_MAX"

    TEMPERATURE_SOIL_MIN_010 = "TEMPERATURE_SOIL_MIN_010"
    TEMPERATURE_SOIL_MIN_020 = "TEMPERATURE_SOIL_MIN_020"
    TEMPERATURE_SOIL_MIN_050 = "TEMPERATURE_SOIL_MIN_050"
    TEMPERATURE_SOIL_MIN_100 = "TEMPERATURE_SOIL_MIN_100"
    TEMPERATURE_SOIL_MIN_200 = "TEMPERATURE_SOIL_MIN_200"

    TEMPERATURE_SOIL_MAX_010 = "TEMPERATURE_SOIL_MAX_010"
    TEMPERATURE_SOIL_MAX_020 = "TEMPERATURE_SOIL_MAX_020"
    TEMPERATURE_SOIL_MAX_050 = "TEMPERATURE_SOIL_MAX_050"
    TEMPERATURE_SOIL_MAX_100 = "TEMPERATURE_SOIL_MAX_100"
    TEMPERATURE_SOIL_MAX_200 = "TEMPERATURE_SOIL_MAX_200"

    TEMPERATURE_SOIL_MIN_UNKNOWN_005 = "TEMPERATURE_SOIL_MIN_UNKNOWN_005"
    TEMPERATURE_SOIL_MIN_UNKNOWN_010 = "TEMPERATURE_SOIL_MIN_UNKNOWN_010"
    TEMPERATURE_SOIL_MIN_UNKNOWN_020 = "TEMPERATURE_SOIL_MIN_UNKNOWN_020"
    TEMPERATURE_SOIL_MIN_UNKNOWN_050 = "TEMPERATURE_SOIL_MIN_UNKNOWN_050"
    TEMPERATURE_SOIL_MIN_UNKNOWN_100 = "TEMPERATURE_SOIL_MIN_UNKNOWN_100"
    TEMPERATURE_SOIL_MIN_UNKNOWN_150 = "TEMPERATURE_SOIL_MIN_UNKNOWN_150"
    TEMPERATURE_SOIL_MIN_UNKNOWN_180 = "TEMPERATURE_SOIL_MIN_UNKNOWN_180"

    TEMPERATURE_SOIL_MAX_UNKNOWN_005 = "TEMPERATURE_SOIL_MAX_UNKNOWN_005"
    TEMPERATURE_SOIL_MAX_UNKNOWN_010 = "TEMPERATURE_SOIL_MAX_UNKNOWN_010"
    TEMPERATURE_SOIL_MAX_UNKNOWN_020 = "TEMPERATURE_SOIL_MAX_UNKNOWN_020"
    TEMPERATURE_SOIL_MAX_UNKNOWN_050 = "TEMPERATURE_SOIL_MAX_UNKNOWN_050"
    TEMPERATURE_SOIL_MAX_UNKNOWN_100 = "TEMPERATURE_SOIL_MAX_UNKNOWN_100"
    TEMPERATURE_SOIL_MAX_UNKNOWN_150 = "TEMPERATURE_SOIL_MAX_UNKNOWN_150"
    TEMPERATURE_SOIL_MAX_UNKNOWN_180 = "TEMPERATURE_SOIL_MAX_UNKNOWN_180"

    # 1 - grass
    TEMPERATURE_SOIL_MIN_GRASS_005 = "TEMPERATURE_SOIL_MIN_GRASS_005"
    TEMPERATURE_SOIL_MIN_GRASS_010 = "TEMPERATURE_SOIL_MIN_GRASS_010"
    TEMPERATURE_SOIL_MIN_GRASS_020 = "TEMPERATURE_SOIL_MIN_GRASS_020"
    TEMPERATURE_SOIL_MIN_GRASS_050 = "TEMPERATURE_SOIL_MIN_GRASS_050"
    TEMPERATURE_SOIL_MIN_GRASS_100 = "TEMPERATURE_SOIL_MIN_GRASS_100"
    TEMPERATURE_SOIL_MIN_GRASS_150 = "TEMPERATURE_SOIL_MIN_GRASS_150"
    TEMPERATURE_SOIL_MIN_GRASS_180 = "TEMPERATURE_SOIL_MIN_GRASS_180"

    TEMPERATURE_SOIL_MAX_GRASS_005 = "TEMPERATURE_SOIL_MAX_GRASS_005"
    TEMPERATURE_SOIL_MAX_GRASS_010 = "TEMPERATURE_SOIL_MAX_GRASS_010"
    TEMPERATURE_SOIL_MAX_GRASS_020 = "TEMPERATURE_SOIL_MAX_GRASS_020"
    TEMPERATURE_SOIL_MAX_GRASS_050 = "TEMPERATURE_SOIL_MAX_GRASS_050"
    TEMPERATURE_SOIL_MAX_GRASS_100 = "TEMPERATURE_SOIL_MAX_GRASS_100"
    TEMPERATURE_SOIL_MAX_GRASS_150 = "TEMPERATURE_SOIL_MAX_GRASS_150"
    TEMPERATURE_SOIL_MAX_GRASS_180 = "TEMPERATURE_SOIL_MAX_GRASS_180"

    # 2 - fallow
    TEMPERATURE_SOIL_MIN_FALLOW_005 = "TEMPERATURE_SOIL_MIN_FALLOW_005"
    TEMPERATURE_SOIL_MIN_FALLOW_010 = "TEMPERATURE_SOIL_MIN_FALLOW_010"
    TEMPERATURE_SOIL_MIN_FALLOW_020 = "TEMPERATURE_SOIL_MIN_FALLOW_020"
    TEMPERATURE_SOIL_MIN_FALLOW_050 = "TEMPERATURE_SOIL_MIN_FALLOW_050"
    TEMPERATURE_SOIL_MIN_FALLOW_100 = "TEMPERATURE_SOIL_MIN_FALLOW_100"
    TEMPERATURE_SOIL_MIN_FALLOW_150 = "TEMPERATURE_SOIL_MIN_FALLOW_150"
    TEMPERATURE_SOIL_MIN_FALLOW_180 = "TEMPERATURE_SOIL_MIN_FALLOW_180"

    TEMPERATURE_SOIL_MAX_FALLOW_005 = "TEMPERATURE_SOIL_MAX_FALLOW_005"
    TEMPERATURE_SOIL_MAX_FALLOW_010 = "TEMPERATURE_SOIL_MAX_FALLOW_010"
    TEMPERATURE_SOIL_MAX_FALLOW_020 = "TEMPERATURE_SOIL_MAX_FALLOW_020"
    TEMPERATURE_SOIL_MAX_FALLOW_050 = "TEMPERATURE_SOIL_MAX_FALLOW_050"
    TEMPERATURE_SOIL_MAX_FALLOW_100 = "TEMPERATURE_SOIL_MAX_FALLOW_100"
    TEMPERATURE_SOIL_MAX_FALLOW_150 = "TEMPERATURE_SOIL_MAX_FALLOW_150"
    TEMPERATURE_SOIL_MAX_FALLOW_180 = "TEMPERATURE_SOIL_MAX_FALLOW_180"

    # 3 - bare ground
    TEMPERATURE_SOIL_MIN_BARE_GROUND_005 = "TEMPERATURE_SOIL_MIN_BARE_GROUND_005"
    TEMPERATURE_SOIL_MIN_BARE_GROUND_010 = "TEMPERATURE_SOIL_MIN_BARE_GROUND_010"
    TEMPERATURE_SOIL_MIN_BARE_GROUND_020 = "TEMPERATURE_SOIL_MIN_BARE_GROUND_020"
    TEMPERATURE_SOIL_MIN_BARE_GROUND_050 = "TEMPERATURE_SOIL_MIN_BARE_GROUND_050"
    TEMPERATURE_SOIL_MIN_BARE_GROUND_100 = "TEMPERATURE_SOIL_MIN_BARE_GROUND_100"
    TEMPERATURE_SOIL_MIN_BARE_GROUND_150 = "TEMPERATURE_SOIL_MIN_BARE_GROUND_150"
    TEMPERATURE_SOIL_MIN_BARE_GROUND_180 = "TEMPERATURE_SOIL_MIN_BARE_GROUND_180"

    TEMPERATURE_SOIL_MAX_BARE_GROUND_005 = "TEMPERATURE_SOIL_MAX_BARE_GROUND_005"
    TEMPERATURE_SOIL_MAX_BARE_GROUND_010 = "TEMPERATURE_SOIL_MAX_BARE_GROUND_010"
    TEMPERATURE_SOIL_MAX_BARE_GROUND_020 = "TEMPERATURE_SOIL_MAX_BARE_GROUND_020"
    TEMPERATURE_SOIL_MAX_BARE_GROUND_050 = "TEMPERATURE_SOIL_MAX_BARE_GROUND_050"
    TEMPERATURE_SOIL_MAX_BARE_GROUND_100 = "TEMPERATURE_SOIL_MAX_BARE_GROUND_100"
    TEMPERATURE_SOIL_MAX_BARE_GROUND_150 = "TEMPERATURE_SOIL_MAX_BARE_GROUND_150"
    TEMPERATURE_SOIL_MAX_BARE_GROUND_180 = "TEMPERATURE_SOIL_MAX_BARE_GROUND_180"

    # 4 - brome grass
    TEMPERATURE_SOIL_MIN_BROME_GRASS_005 = "TEMPERATURE_SOIL_MIN_BROME_GRASS_005"
    TEMPERATURE_SOIL_MIN_BROME_GRASS_010 = "TEMPERATURE_SOIL_MIN_BROME_GRASS_010"
    TEMPERATURE_SOIL_MIN_BROME_GRASS_020 = "TEMPERATURE_SOIL_MIN_BROME_GRASS_020"
    TEMPERATURE_SOIL_MIN_BROME_GRASS_050 = "TEMPERATURE_SOIL_MIN_BROME_GRASS_050"
    TEMPERATURE_SOIL_MIN_BROME_GRASS_100 = "TEMPERATURE_SOIL_MIN_BROME_GRASS_100"
    TEMPERATURE_SOIL_MIN_BROME_GRASS_150 = "TEMPERATURE_SOIL_MIN_BROME_GRASS_150"
    TEMPERATURE_SOIL_MIN_BROME_GRASS_180 = "TEMPERATURE_SOIL_MIN_BROME_GRASS_180"

    TEMPERATURE_SOIL_MAX_BROME_GRASS_005 = "TEMPERATURE_SOIL_MAX_BROME_GRASS_005"
    TEMPERATURE_SOIL_MAX_BROME_GRASS_010 = "TEMPERATURE_SOIL_MAX_BROME_GRASS_010"
    TEMPERATURE_SOIL_MAX_BROME_GRASS_020 = "TEMPERATURE_SOIL_MAX_BROME_GRASS_020"
    TEMPERATURE_SOIL_MAX_BROME_GRASS_050 = "TEMPERATURE_SOIL_MAX_BROME_GRASS_050"
    TEMPERATURE_SOIL_MAX_BROME_GRASS_100 = "TEMPERATURE_SOIL_MAX_BROME_GRASS_100"
    TEMPERATURE_SOIL_MAX_BROME_GRASS_150 = "TEMPERATURE_SOIL_MAX_BROME_GRASS_150"
    TEMPERATURE_SOIL_MAX_BROME_GRASS_180 = "TEMPERATURE_SOIL_MAX_BROME_GRASS_180"

    # 5 - sod
    TEMPERATURE_SOIL_MIN_SOD_005 = "TEMPERATURE_SOIL_MIN_SOD_005"
    TEMPERATURE_SOIL_MIN_SOD_010 = "TEMPERATURE_SOIL_MIN_SOD_010"
    TEMPERATURE_SOIL_MIN_SOD_020 = "TEMPERATURE_SOIL_MIN_SOD_020"
    TEMPERATURE_SOIL_MIN_SOD_050 = "TEMPERATURE_SOIL_MIN_SOD_050"
    TEMPERATURE_SOIL_MIN_SOD_100 = "TEMPERATURE_SOIL_MIN_SOD_100"
    TEMPERATURE_SOIL_MIN_SOD_150 = "TEMPERATURE_SOIL_MIN_SOD_150"
    TEMPERATURE_SOIL_MIN_SOD_180 = "TEMPERATURE_SOIL_MIN_SOD_180"

    TEMPERATURE_SOIL_MAX_SOD_005 = "TEMPERATURE_SOIL_MAX_SOD_005"
    TEMPERATURE_SOIL_MAX_SOD_010 = "TEMPERATURE_SOIL_MAX_SOD_010"
    TEMPERATURE_SOIL_MAX_SOD_020 = "TEMPERATURE_SOIL_MAX_SOD_020"
    TEMPERATURE_SOIL_MAX_SOD_050 = "TEMPERATURE_SOIL_MAX_SOD_050"
    TEMPERATURE_SOIL_MAX_SOD_100 = "TEMPERATURE_SOIL_MAX_SOD_100"
    TEMPERATURE_SOIL_MAX_SOD_150 = "TEMPERATURE_SOIL_MAX_SOD_150"
    TEMPERATURE_SOIL_MAX_SOD_180 = "TEMPERATURE_SOIL_MAX_SOD_180"

    # 6 - straw mulch
    TEMPERATURE_SOIL_MIN_STRAW_MULCH_005 = "TEMPERATURE_SOIL_MIN_STRAW_MULCH_005"
    TEMPERATURE_SOIL_MIN_STRAW_MULCH_010 = "TEMPERATURE_SOIL_MIN_STRAW_MULCH_010"
    TEMPERATURE_SOIL_MIN_STRAW_MULCH_020 = "TEMPERATURE_SOIL_MIN_STRAW_MULCH_020"
    TEMPERATURE_SOIL_MIN_STRAW_MULCH_050 = "TEMPERATURE_SOIL_MIN_STRAW_MULCH_050"
    TEMPERATURE_SOIL_MIN_STRAW_MULCH_100 = "TEMPERATURE_SOIL_MIN_STRAW_MULCH_100"
    TEMPERATURE_SOIL_MIN_STRAW_MULCH_150 = "TEMPERATURE_SOIL_MIN_STRAW_MULCH_150"
    TEMPERATURE_SOIL_MIN_STRAW_MULCH_180 = "TEMPERATURE_SOIL_MIN_STRAW_MULCH_180"

    TEMPERATURE_SOIL_MAX_STRAW_MULCH_005 = "TEMPERATURE_SOIL_MAX_STRAW_MULCH_005"
    TEMPERATURE_SOIL_MAX_STRAW_MULCH_010 = "TEMPERATURE_SOIL_MAX_STRAW_MULCH_010"
    TEMPERATURE_SOIL_MAX_STRAW_MULCH_020 = "TEMPERATURE_SOIL_MAX_STRAW_MULCH_020"
    TEMPERATURE_SOIL_MAX_STRAW_MULCH_050 = "TEMPERATURE_SOIL_MAX_STRAW_MULCH_050"
    TEMPERATURE_SOIL_MAX_STRAW_MULCH_100 = "TEMPERATURE_SOIL_MAX_STRAW_MULCH_100"
    TEMPERATURE_SOIL_MAX_STRAW_MULCH_150 = "TEMPERATURE_SOIL_MAX_STRAW_MULCH_150"
    TEMPERATURE_SOIL_MAX_STRAW_MULCH_180 = "TEMPERATURE_SOIL_MAX_STRAW_MULCH_180"

    # 7 - grass muck
    TEMPERATURE_SOIL_MIN_GRASS_MUCK_005 = "TEMPERATURE_SOIL_MIN_GRASS_MUCK_005"
    TEMPERATURE_SOIL_MIN_GRASS_MUCK_010 = "TEMPERATURE_SOIL_MIN_GRASS_MUCK_010"
    TEMPERATURE_SOIL_MIN_GRASS_MUCK_020 = "TEMPERATURE_SOIL_MIN_GRASS_MUCK_020"
    TEMPERATURE_SOIL_MIN_GRASS_MUCK_050 = "TEMPERATURE_SOIL_MIN_GRASS_MUCK_050"
    TEMPERATURE_SOIL_MIN_GRASS_MUCK_100 = "TEMPERATURE_SOIL_MIN_GRASS_MUCK_100"
    TEMPERATURE_SOIL_MIN_GRASS_MUCK_150 = "TEMPERATURE_SOIL_MIN_GRASS_MUCK_150"
    TEMPERATURE_SOIL_MIN_GRASS_MUCK_180 = "TEMPERATURE_SOIL_MIN_GRASS_MUCK_180"

    TEMPERATURE_SOIL_MAX_GRASS_MUCK_005 = "TEMPERATURE_SOIL_MAX_GRASS_MUCK_005"
    TEMPERATURE_SOIL_MAX_GRASS_MUCK_010 = "TEMPERATURE_SOIL_MAX_GRASS_MUCK_010"
    TEMPERATURE_SOIL_MAX_GRASS_MUCK_020 = "TEMPERATURE_SOIL_MAX_GRASS_MUCK_020"
    TEMPERATURE_SOIL_MAX_GRASS_MUCK_050 = "TEMPERATURE_SOIL_MAX_GRASS_MUCK_050"
    TEMPERATURE_SOIL_MAX_GRASS_MUCK_100 = "TEMPERATURE_SOIL_MAX_GRASS_MUCK_100"
    TEMPERATURE_SOIL_MAX_GRASS_MUCK_150 = "TEMPERATURE_SOIL_MAX_GRASS_MUCK_150"
    TEMPERATURE_SOIL_MAX_GRASS_MUCK_180 = "TEMPERATURE_SOIL_MAX_GRASS_MUCK_180"

    # 8 - bare muck
    TEMPERATURE_SOIL_MIN_BARE_MUCK_005 = "TEMPERATURE_SOIL_MIN_BARE_MUCK_005"
    TEMPERATURE_SOIL_MIN_BARE_MUCK_010 = "TEMPERATURE_SOIL_MIN_BARE_MUCK_010"
    TEMPERATURE_SOIL_MIN_BARE_MUCK_020 = "TEMPERATURE_SOIL_MIN_BARE_MUCK_020"
    TEMPERATURE_SOIL_MIN_BARE_MUCK_050 = "TEMPERATURE_SOIL_MIN_BARE_MUCK_050"
    TEMPERATURE_SOIL_MIN_BARE_MUCK_100 = "TEMPERATURE_SOIL_MIN_BARE_MUCK_100"
    TEMPERATURE_SOIL_MIN_BARE_MUCK_150 = "TEMPERATURE_SOIL_MIN_BARE_MUCK_150"
    TEMPERATURE_SOIL_MIN_BARE_MUCK_180 = "TEMPERATURE_SOIL_MIN_BARE_MUCK_180"

    TEMPERATURE_SOIL_MAX_BARE_MUCK_005 = "TEMPERATURE_SOIL_MAX_BARE_MUCK_005"
    TEMPERATURE_SOIL_MAX_BARE_MUCK_010 = "TEMPERATURE_SOIL_MAX_BARE_MUCK_010"
    TEMPERATURE_SOIL_MAX_BARE_MUCK_020 = "TEMPERATURE_SOIL_MAX_BARE_MUCK_020"
    TEMPERATURE_SOIL_MAX_BARE_MUCK_050 = "TEMPERATURE_SOIL_MAX_BARE_MUCK_050"
    TEMPERATURE_SOIL_MAX_BARE_MUCK_100 = "TEMPERATURE_SOIL_MAX_BARE_MUCK_100"
    TEMPERATURE_SOIL_MAX_BARE_MUCK_150 = "TEMPERATURE_SOIL_MAX_BARE_MUCK_150"
    TEMPERATURE_SOIL_MAX_BARE_MUCK_180 = "TEMPERATURE_SOIL_MAX_BARE_MUCK_180"
    # ---- count ----
    COUNT_DAYS_HEATING_DEGREE = "COUNT_DAYS_HEATING_DEGREE"
    COUNT_DAYS_COOLING_DEGREE = "COUNT_DAYS_COOLING_DEGREE"
    # Number of days included in the multiday minimum temperature
    COUNT_DAYS_MULTIDAY_TEMPERATURE_AIR_MIN_200 = "COUNT_DAYS_MULTIDAY_TEMPERATURE_AIR_MIN_200"
    # Number of days included in the multiday maximum temperature
    COUNT_DAYS_MULTIDAY_TEMPERATURE_AIR_MAX_200 = "COUNT_DAYS_MULTIDAY_TEMPERATURE_AIR_MAX_200"
    # ---- error ----
    ERROR_ABSOLUTE_TEMPERATURE_AIR_MEAN_200 = "ERROR_ABSOLUTE_TEMPERATURE_AIR_MEAN_200"
    ERROR_ABSOLUTE_TEMPERATURE_DEW_POINT_MEAN_200 = "ERROR_ABSOLUTE_TEMPERATURE_DEW_POINT_MEAN_200"

    # VISIBILITY
    # ---- distance ----
    VISIBILITY_RANGE_INDEX = "VISIBILITY_RANGE_INDEX"
    VISIBILITY_RANGE = "VISIBILITY_RANGE"  # through clouds, fog, etc
    # ---- probability ----
    PROBABILITY_VISIBILITY_BELOW_1000_M = "PROBABILITY_VISIBILITY_BELOW_1000_M"

    # WATER EQUIVALENT
    # ---- aggregated ----
    WATER_EQUIVALENT_SNOW_DEPTH = "WATER_EQUIVALENT_SNOW_DEPTH"
    WATER_EQUIVALENT_SNOW_DEPTH_NEW = "WATER_EQUIVALENT_SNOW_DEPTH_NEW"
    WATER_EQUIVALENT_SNOW_DEPTH_EXCELLED = "WATER_EQUIVALENT_SNOW_DEPTH_EXCELLED"
    WATER_EQUIVALENT_SNOW_DEPTH_NEW_LAST_1H = "WATER_EQUIVALENT_SNOW_DEPTH_NEW_LAST_1H"
    WATER_EQUIVALENT_SNOW_DEPTH_NEW_LAST_3H = "WATER_EQUIVALENT_SNOW_DEPTH_NEW_LAST_3H"

    # WEATHER
    # ---- aggregated ----
    WEATHER_SIGNIFICANT = "WEATHER_SIGNIFICANT"
    WEATHER_SIGNIFICANT_LAST_3H = "WEATHER_SIGNIFICANT_LAST_3H"
    WEATHER_LAST_6H = "WEATHER_LAST_6H"
    WEATHER_SIGNIFICANT_OPTIONAL_LAST_1H = "WEATHER_SIGNIFICANT_OPTIONAL_LAST_1H"
    WEATHER_SIGNIFICANT_OPTIONAL_LAST_3H = "WEATHER_SIGNIFICANT_OPTIONAL_LAST_3H"
    WEATHER_SIGNIFICANT_OPTIONAL_LAST_6H = "WEATHER_SIGNIFICANT_OPTIONAL_LAST_6H"
    WEATHER_SIGNIFICANT_OPTIONAL_LAST_12H = "WEATHER_SIGNIFICANT_OPTIONAL_LAST_12H"
    WEATHER_SIGNIFICANT_OPTIONAL_LAST_24H = "WEATHER_SIGNIFICANT_OPTIONAL_LAST_24H"
    # TODO: ECCC parameter, same as significant weather?
    WEATHER = "WEATHER"
    WEATHER_TEXT = "WEATHER_TEXT"

    # WEATHER PHENOMENA
    # ---- averaged ----
    WEATHER_TYPE_FOG = "WEATHER_TYPE_FOG"
    WEATHER_TYPE_HEAVY_FOG = "WEATHER_TYPE_HEAVY_FOG"
    WEATHER_TYPE_THUNDER = "WEATHER_TYPE_THUNDER"
    WEATHER_TYPE_ICE_SLEET_SNOW_HAIL = "WEATHER_TYPE_ICE_SLEET_SNOW_HAIL"
    WEATHER_TYPE_HAIL = "WEATHER_TYPE_HAIL"
    WEATHER_TYPE_GLAZE_RIME = "WEATHER_TYPE_GLAZE_RIME"
    WEATHER_TYPE_DUST_ASH_SAND = "WEATHER_TYPE_DUST_ASH_SAND"
    WEATHER_TYPE_SMOKE_HAZE = "WEATHER_TYPE_SMOKE_HAZE"
    WEATHER_TYPE_BLOWING_DRIFTING_SNOW = "WEATHER_TYPE_BLOWING_DRIFTING_SNOW"
    WEATHER_TYPE_TORNADO_WATERSPOUT = "WEATHER_TYPE_TORNADO_WATERSPOUT"
    WEATHER_TYPE_HIGH_DAMAGING_WINDS = "WEATHER_TYPE_HIGH_DAMAGING_WINDS"
    WEATHER_TYPE_BLOWING_SPRAY = "WEATHER_TYPE_BLOWING_SPRAY"
    WEATHER_TYPE_MIST = "WEATHER_TYPE_MIST"
    WEATHER_TYPE_DRIZZLE = "WEATHER_TYPE_DRIZZLE"
    WEATHER_TYPE_FREEZING_DRIZZLE = "WEATHER_TYPE_FREEZING_DRIZZLE"
    WEATHER_TYPE_RAIN = "WEATHER_TYPE_RAIN"
    WEATHER_TYPE_FREEZING_RAIN = "WEATHER_TYPE_FREEZING_RAIN"
    WEATHER_TYPE_SNOW_PELLETS_SNOW_GRAINS_ICE_CRYSTALS = "WEATHER_TYPE_SNOW_PELLETS_SNOW_GRAINS_ICE_CRYSTALS"
    WEATHER_TYPE_PRECIPITATION_UNKNOWN_SOURCE = "WEATHER_TYPE_PRECIPITATION_UNKNOWN_SOURCE"
    WEATHER_TYPE_GROUND_FOG = "WEATHER_TYPE_GROUND_FOG"
    WEATHER_TYPE_ICE_FOG_FREEZING_FOG = "WEATHER_TYPE_ICE_FOG_FREEZING_FOG"

    WEATHER_TYPE_VICINITY_FOG_ANY = "WEATHER_TYPE_VICINITY_FOG_ANY"
    WEATHER_TYPE_VICINITY_THUNDER = "WEATHER_TYPE_VICINITY_THUNDER"
    WEATHER_TYPE_VICINITY_DUST_ASH_SAND = "WEATHER_TYPE_VICINITY_DUST_ASH_SAND"
    WEATHER_TYPE_VICINITY_SNOW_ICE_CRYSTALS = "WEATHER_TYPE_VICINITY_SNOW_ICE_CRYSTALS"
    WEATHER_TYPE_VICINITY_RAIN_SNOW_SHOWER = "WEATHER_TYPE_VICINITY_RAIN_SNOW_SHOWER"
    # ---- count ----
    # the following are coming from DWD Observations
    COUNT_WEATHER_TYPE_FOG = "COUNT_FOG"
    COUNT_WEATHER_TYPE_THUNDER = "COUNT_THUNDER"
    COUNT_WEATHER_TYPE_STORM_STRONG_WIND = "COUNT_STORM_STRONG_WIND"
    COUNT_WEATHER_TYPE_STORM_STORMIER_WIND = "COUNT_STORM_STORMIER_WIND"
    COUNT_WEATHER_TYPE_DEW = "COUNT_DEW"
    COUNT_WEATHER_TYPE_GLAZE = "COUNT_GLAZE"
    COUNT_WEATHER_TYPE_RIPE = "COUNT_RIPE"
    COUNT_WEATHER_TYPE_SLEET = "COUNT_SLEET"
    COUNT_WEATHER_TYPE_HAIL = "COUNT_HAIL"
    # ---- probability ----
    PROBABILITY_THUNDER_LAST_1H = "PROBABILITY_THUNDER_LAST_1H"
    PROBABILITY_THUNDER_LAST_6H = "PROBABILITY_THUNDER_LAST_6H"
    PROBABILITY_THUNDER_LAST_12H = "PROBABILITY_THUNDER_LAST_12H"
    PROBABILITY_THUNDER_LAST_24H = "PROBABILITY_THUNDER_LAST_24H"

    # WIND
    # ---- averaged ----
    WIND_SPEED = "WIND_SPEED"
    WIND_DIRECTION = "WIND_DIRECTION"
    WIND_FORCE_BEAUFORT = "WIND_FORCE_BEAUFORT"
    # ---- extremes ----
    WIND_GUST_MAX = "WIND_GUST_MAX"
    WIND_GUST_MAX_LAST_1H = "WIND_GUST_MAX_LAST_1H"
    WIND_GUST_MAX_LAST_3H = "WIND_GUST_MAX_LAST_3H"
    WIND_GUST_MAX_LAST_6H = "WIND_GUST_MAX_LAST_6H"
    WIND_GUST_MAX_LAST_12H = "WIND_GUST_MAX_LAST_12H"
    WIND_SPEED_MIN = "WIND_SPEED_MIN"
    WIND_SPEED_ROLLING_MEAN_MAX = "WIND_SPEED_ROLLING_MEAN_MAX"
    WIND_DIRECTION_GUST_MAX = "WIND_DIRECTION_GUST_MAX"

    WIND_GUST_MAX_5SEC = "WIND_GUST_MAX_5SEC"
    WIND_GUST_MAX_1MIN = "WIND_GUST_MAX_1MIN"
    WIND_GUST_MAX_2MIN = "WIND_GUST_MAX_2MIN"
    WIND_GUST_MAX_INSTANT = "WIND_GUST_MAX_INSTANT"
    WIND_GUST_MAX_1MILE = "WIND_GUST_MAX_1MILE"

    WIND_DIRECTION_GUST_MAX_5SEC = "WIND_DIRECTION_GUST_MAX_5SEC"
    WIND_DIRECTION_GUST_MAX_1MIN = "WIND_DIRECTION_GUST_MAX_1MIN"
    WIND_DIRECTION_GUST_MAX_2MIN = "WIND_DIRECTION_GUST_MAX_2MIN"
    WIND_DIRECTION_GUST_MAX_INSTANT = "WIND_DIRECTION_GUST_MAX_INSTANT"
    WIND_DIRECTION_GUST_MAX_1MILE = "WIND_DIRECTION_GUST_MAX_1MILE"
    # ---- probability ----
    PROBABILITY_WIND_GUST_GE_25_KN_LAST_6H = "PROBABILITY_WIND_GUST_GE_25_KN_LAST_6H"
    PROBABILITY_WIND_GUST_GE_25_KN_LAST_12H = "PROBABILITY_WIND_GUST_GE_25_KN_LAST_12H"
    PROBABILITY_WIND_GUST_GE_40_KN_LAST_6H = "PROBABILITY_WIND_GUST_GE_40_KN_LAST_6H"
    PROBABILITY_WIND_GUST_GE_40_KN_LAST_12H = "PROBABILITY_WIND_GUST_GE_40_KN_LAST_12H"
    PROBABILITY_WIND_GUST_GE_55_KN_LAST_6H = "PROBABILITY_WIND_GUST_GE_55_KN_LAST_6H"
    PROBABILITY_WIND_GUST_GE_55_KN_LAST_12H = "PROBABILITY_WIND_GUST_GE_55_KN_LAST_12H"
    # ---- count ----
    # Number of days included in the multiday wind movement
    COUNT_DAYS_MULTIDAY_WIND_MOVEMENT = "COUNT_DAYS_MULTIDAY_WIND_MOVEMENT"
    # ---- time ----
    TIME_WIND_GUST_MAX_1MILE_OR_1MIN = "TIME_WIND_GUST_MAX_1MILE_OR_1MIN"
    TIME_WIND_GUST_MAX = "TIME_WIND_GUST_MAX"
    # ---- distance ----
    WIND_MOVEMENT_MULTIDAY = "WIND_MOVEMENT_MULTIDAY"
    WIND_MOVEMENT_24HOUR = "WIND_MOVEMENT_24HOUR"
    # ---- error ----
    ERROR_ABSOLUTE_WIND_SPEED = "ERROR_ABSOLUTE_WIND_SPEED"
    ERROR_ABSOLUTE_WIND_DIRECTION = "ERROR_ABSOLUTE_WIND_DIRECTION"

    # Waterways related parameters
    TEMPERATURE_WATER = "TEMPERATURE_WATER"
    ELECTRIC_CONDUCTIVITY = "ELECTRIC_CONDUCTIVITY"
    WATER_LEVEL = "WATER_LEVEL"
    GROUNDWATER_LEVEL = "GROUNDWATER_LEVEL"
    DISCHARGE = "DISCHARGE"
    FLOW_SPEED = "FLOW_SPEED"
    OXYGEN_LEVEL = "OXYGEN_LEVEL"
    TURBIDITY = "TURBIDITY"
    PRECIPITATION_INTENSITY = "PRECIPITATION_INTENSITY"
    WAVE_PERIOD = "WAVE_PERIOD"
    CLEARANCE_HEIGHT = "CLEARANCE_HEIGHT"
    CURRENT = "CURRENT"
    WAVE_HEIGHT_SIGN = "WAVE_HEIGHT_SIGN"
    WAVE_HEIGHT_MAX = "WAVE_HEIGHT_MAX"
    PH_VALUE = "PH_VALUE"
    CHLORID_CONCENTRATION = "CHLORID_CONCENTRATION"
    STAGE = "STAGE"
    FLOW = "FLOW"
