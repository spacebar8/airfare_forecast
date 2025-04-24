# Forecast US Airfare Data Using FaceBook / Meta Prophet
## Data
Kaggle https://www.kaggle.com/datasets/bhavikjikadara/us-airline-flight-routes-and-fares-1993-2024/code
* 250k records with 20+ features
* 4069 flights with at most 30+ years
  * Quarterly Dates: 1993-Q1 to 2024-Q1

## Features
* tbl: Table identifier
* Year: Year of the data record
* quarter: Quarter of the year (1-4)
* citymarketid_1: Origin city market ID
* citymarketid_2: Destination city market ID
* city1: Origin city name
* city2: Destination city name
* airportid_1: Origin airport ID
* airportid_2: Destination airport ID
* airport_1: Origin airport code
* airport_2: Destination airport code
* nsmiles: Distance between airports in miles
* passengers: Number of passengers
* fare: Average fare
* carrier_lg: Code for the largest carrier by passengers
* large_ms: Market share of the largest carrier
* fare_lg: Average fare of the largest carrier
* carrier_low: Code for the lowest fare carrier
* lf_ms: Market share of the lowest fare carrier
* fare_low: Lowest fare
* Geocoded_City1: Geocoded coordinates for the origin city
* Geocoded_City2: Geocoded coordinates for the destination city
* tbl1apk: Unique identifier for the route
