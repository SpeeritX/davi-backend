import pandas as pd
import os.path

pickled_minute = './resources/pickled_minute.data'
pickled_day = './resources/pickled_day.data'
pickled_parallel = './resources/pickled_parallel.data'


def load_days():
    if not os.path.exists(pickled_day):
        df = read_days()
        df.to_pickle(pickled_day)
        return df
    df = pd.read_pickle(pickled_day)
    df = df.rename(columns={
                   "barometric altitude": "barometric_altitude", "origin country": "origin_country"})
    return df


def load_minutes():
    if not os.path.exists(pickled_minute):
        df = read_minutes()
        df.to_pickle(pickled_minute)
        return df
    df = pd.read_pickle(pickled_minute)
    return df


def load_parallel():
    if not os.path.exists(pickled_parallel):
        df = read_parallel_sets()
        df.to_pickle(pickled_parallel)
        return df
    df = pd.read_pickle(pickled_parallel)
    return df


def read_minutes():
    df = pd.read_csv('./resources/processed_data_davi.csv',
                     dtype={
                         "ICAO 24-bit code": 'string[pyarrow]',
                         "callsign": 'string[pyarrow]',
                         "origin country": 'category',
                         "time at position": 'string[pyarrow]',
                         "longitude": 'string[pyarrow]',
                         "latitude": 'string[pyarrow]',
                         "barometric altitude": 'float32',
                         "aircraft is grounded": 'bool',
                         "velocity": 'float32',
                         "heading": 'float32',
                         "vertical rate": 'float32',
                         "geo_altitude": 'float32',
                         "squawk": 'float32',
                         "country": 'category',
                         "oblast": 'category',
                     },
                     index_col='time at position',
                     parse_dates=True,
                     date_parser=pd.to_datetime,
                     usecols=[
                         "ICAO 24-bit code",
                         "callsign",
                         "origin country",
                         "time at position",
                         "longitude",
                         "latitude",
                         "country",
                         "oblast",
                         "flight-id"
                     ])
    return df


def read_parallel_sets():
    df = pd.read_csv('./resources/parallel_sets_numbers.csv',
                     dtype={
                         "spi": 'int16',
                         "squawk": 'string[pyarrow]',
                         "was_in_ukraine": 'int16'
                     },
                     index_col='date',
                     parse_dates=True,
                     date_parser=pd.to_datetime)
    return df


def read_days():
    #    df = pd.read_csv(csv, index_col='date', parse_dates=True)
    df = pd.read_csv('./resources/flights_separate.csv',
                     dtype={
                         "flight-id": 'string[pyarrow]',
                         "origin country": 'category',
                         "date": 'string[pyarrow]',
                         "latitude, longitude": 'string[pyarrow]',
                         "barometric altitude": 'float32',
                         "velocity": 'float32',
                         "vertical rate": 'float32',
                         "was_in_ukraine": 'bool'
                     },
                     index_col='date',
                     parse_dates=True,
                     date_parser=pd.to_datetime,
                     usecols=[
                         "date",
                         "origin country",
                         "barometric altitude",
                         "velocity",
                         "vertical rate",
                         "latitude, longitude",
                         "country",
                         "oblast",
                         "was_in_ukraine"
                     ])
    return df
