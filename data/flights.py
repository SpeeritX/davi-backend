from data.load_pandas import load_minutes, load_days
from datetime import datetime
import pandas as pd
from datetime import timedelta


class Flights:
    def __init__(self):
        self.df_minutes = load_minutes()
        self.df_days = load_days()
        print("Dataset is ready...")

    @property
    def oblasts(self):
        return list(self.df_minutes.oblast.unique())

    def filter_by_time(self, time_1 ):
        return self.df_minutes.loc[time_1]

    def filter_by_date(self, time_1, time_2 ):
        return self.df_days.loc[time_1:time_2]

    def filter_by_date_return_country_count_too(self, time_1, time_2):
        return {self.df_days[time_1:time_2],self.df_days[time_1:time_2]['origin country'].value_counts()}
