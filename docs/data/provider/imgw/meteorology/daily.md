# daily

## metadata

| property      | value                                                                                               |
|---------------|-----------------------------------------------------------------------------------------------------|
| name          | daily                                                                                               |
| original name | dobowe                                                                                              |
| url           | [here](https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/dobowe/) |

## datasets

### climate

#### metadata

| property      | value                                                                                                      |
|---------------|------------------------------------------------------------------------------------------------------------|
| name          | climate                                                                                                    |
| original name | klimat                                                                                                     |
| description   | historical daily climate data                                                                              |
| access        | [here](https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/dobowe/klimat/) |

#### parameters

| name                       | original name                      | description                | unit  | original unit | constraints |
|----------------------------|------------------------------------|----------------------------|-------|---------------|-------------|
| cloud_cover_total          | średnie dobowe zachmurzenie        | cloud cover total          | %     | 1/8           | >=0,<=100   |
| humidity                   | średnia dobowa wilgotność          | humidity                   | %     | %             | >=0,<=100   |
| precipitation_height       | suma dobowa opadów                 | precipitation height       | kg/m² | mm            | >=0         |
| snow_depth                 | wysokość pokrywy śnieżnej          | snow depth                 | m     | cm            | >=0         |
| temperature_air_max_2m     | maksymalna temperatura dobowa      | temperature air max 2m     | K     | °C            | -           |
| temperature_air_mean_0_05m | temperatura minimalna przy gruncie | temperature air mean 0 05m | K     | °C            | -           |
| temperature_air_mean_2m    | średnia dobowa temperatura         | temperature air mean 2m    | K     | °C            | -           |
| temperature_air_min_2m     | minimalna temperatura dobowa       | temperature air min 2m     | K     | °C            | -           |
| wind_speed                 | średnia dobowa prędkość wiatru     | wind speed                 | m/s   | m/s           | >=0         |

### precipitation

#### metadata

| property      | value                                                                                                    |
|---------------|----------------------------------------------------------------------------------------------------------|
| name          | precipitation                                                                                            |
| original name | opad                                                                                                     |
| description   | historical daily precipitation data                                                                      |
| access        | [here](https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/dobowe/opad/) |

#### parameters

| name                 | original name                 | description          | unit  | original unit | constraints |
|----------------------|-------------------------------|----------------------|-------|---------------|-------------|
| precipitation_height | suma dobowa opadów            | precipitation height | kg/m² | mm            | >=0         |
| snow_depth           | wysokość pokrywy śnieżnej     | snow depth           | m     | cm            | >=0         |
| snow_depth_new       | wysokość świeżospałego śniegu | snow depth new       | m     | cm            | >=0         |

### synop

#### metadata

| property      | value                                                                                                     |
|---------------|-----------------------------------------------------------------------------------------------------------|
| name          | synop                                                                                                     |
| original name | synop                                                                                                     |
| description   | historical daily synop data                                                                               |
| access        | [here](https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_meteorologiczne/dobowe/synop/) |

#### parameters

| name                    | original name                  | description          | unit  | original unit | constraints |
|-------------------------|--------------------------------|----------------------|-------|---------------|-------------|
| cloud_cover_total       | średnie dobowe zachmurzenie    | cloud cover total    | %     | 1/8           | >=0,<=100   |
| humidity                | średnia dobowa wilgotność      | humidity             | %     | %             | >=0,<=100   |
| precipitation_height    | suma dobowa opadów             | precipitation height | kg/m² | mm            | >=0         |
| pressure_air_site       | średnia dobowe ciśnienie       | pressure air site    | Pa    | hPa           | >=0         |
| pressure_air_sea        | średnie dobowe ciśnienie morza | pressure air sea     | Pa    | hPa           | >=0         |
| pressure_vapor          | średnie dobowe ciśnienie pary  | pressure vapor       | Pa    | hPa           | >=0         |
| temperature_air_mean_2m | średnia dobowa temperatura     | temperature air mean | K     | °C            | -           |
| wind_speed              | średnia dobowa prędkość wiatru | wind speed           | m/s   | m/s           | >=0         |