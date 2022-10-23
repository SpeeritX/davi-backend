import pandas as pd
import os.path

pickledData = './resources/pickled.data'

def load_dataset():
    if not os.path.exists(pickledData):
        df = read_csv()
        df.to_pickle(pickledData)
        return df
    df = pd.read_pickle(pickledData)
    return df

def read_csv():
    df = []
    with pd.read_csv('./resources/processed_data_davi.csv', 
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
        date_parser = pd.to_datetime,
        parse_dates=['time at position'],
        usecols=[
            "ICAO 24-bit code",
            "callsign",
            "origin country",
            "time at position",
            "longitude",
            "latitude",
            "country",
            "oblast"
        ],
        chunksize=1_000_000) as reader:
        for chunk in reader:
            df.append(chunk)
    df = pd.concat(df)
    return df