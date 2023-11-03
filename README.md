# flight-metrics-converter-python
Gets kts, km/h, m/s, mach, ft, NM, km and m as input and returns conversations of it

## Requirements
- Python3
- Unix shell
- Wget (optional)

## Installation
#### Debian/Ubuntu
- `apt install python3`
- `wget https://raw.githubusercontent.com/do-m-inik/flight-metrics-converter-python/main/flight-metrics-converter.py`

#### MacOS
- `brew install python3`
- `wget https://raw.githubusercontent.com/do-m-inik/flight-metrics-converter-python/main/flight-metrics-converter.py`

## Usage
- `python3 flight-metrics-converter.py [-h] [--kts KNOTS] [--kmh KILOMETERS_PER_HOUR] [--ms METERS_PER_SECOND] [--mach MACH] [--nm NAUTICAL_MILES] [--ft FOOT] [--km KILOMETERS] [--m METERS]`
- Only one value can be converted at once

## Examples
- Converting 230 kts: `python3 flight-metrics-converter.py --kt 230`
<br />
Output:

    ========== Flight Metrics Converter v1.0.0 ==========
    > 230.0 kts
    > 425.96 km/h
    > 118.32 m/s
    > 0.35 mach
    =====================================================
    = Important Note: Almost all values are not exactly =
    =====================================================

<br />

- Converting 0.82 mach: `python3 flight-metrics-converter.py --mach 0.82`
<br />
Output:

    ========== Flight Metrics Converter v1.0.0 ==========
    > 542.41 kts
    > 1004.54 km/h
    > 279.04 m/s
    > 0.82 mach
    =====================================================
    = Important Note: Almost all values are not exactly =
    =====================================================
  
<br />
- Converting 41000ft: `python3 flight-metrics-converter.py --ft 41000`
<br />
Output:

    ========== Flight Metrics Converter v1.0.0 ==========
    > 41000.0 ft
    > 6.75 NM
    > 12.5 km
    > 12496.8 m
    =====================================================
    = Important Note: Almost all values are not exactly =
    =====================================================

<br />

- Converting 200km: `python3 flight-metrics-converter.py --km 200`
<br />
Output:

    ========== Flight Metrics Converter v1.0.0 ==========
    > 656167.98 ft
    > 107.99 NM
    > 200.0 km
    > 200000.0 m
    =====================================================
    = Important Note: Almost all values are not exactly =
    =====================================================
