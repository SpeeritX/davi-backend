from data.load_pandas import load_dataset
from datetime import datetime
import pandas as pd


class Flights:
    def __init__(self):
        self.df = load_dataset()
        print("Dataset is ready...")

    @property
    def oblasts(self):
        return list(self.df.oblast.unique())

    def filter_by_time(self, time_1, time_2):
        return str(self.df[(self.df['time at position'] > time_1) & (self.df['time at position'] < time_2)])
