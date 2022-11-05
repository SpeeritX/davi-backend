from data.load_pandas import load_minutes, load_days
from datetime import datetime
import pandas as pd
from datetime import timedelta
import numpy as np


class Flights:
    def __init__(self):
        self.df_minutes = load_minutes()
        self.df_days = load_days()
        print("Dataset is ready...")

    @property
    def oblasts(self):
        return list(self.df_minutes.oblast.unique())

    def filter_by_date(self, date_1, date_2 ):
        return self.df_days.loc[date_1:date_2]

    def filter_by_date_and_origin_country(self, date_1, date_2, string_of_countries):
        selected_dates = self.df_days.loc[date_1:date_2]
        return selected_dates[selected_dates['origin country'].isin(string_of_countries.split(','))]

    def filter_by_date_and_current_country(self, date_1, date_2, string_of_countries):
        selected_dates = self.df_days.loc[date_1:date_2]
        return selected_dates[selected_dates['country'].str.contains('|'.join(string_of_countries.split(',')))]

    def filter_by_date_and_spi(self, date_1, date_2, boolean_v):
        selected_dates = self.df_minutes.loc[date_1:date_2]
        return selected_dates[selected_dates['spi'] == boolean_v]

    def filter_flight_by_id(self, flight_id):
        return self.df_minutes[self.df_minutes['flight-id'] == flight_id]

    def filter_by_date_and_max_altitude_higher(self, date_1, date_2, max_altitude):
        selected_dates = self.df_days.loc[date_1:date_2]
        return selected_dates[selected_dates['barometric altitude'] > float(max_altitude)]

    def filter_by_date_and_max_velocity_higher(self, date_1, date_2, max_velocity):
        selected_dates = self.df_days.loc[date_1:date_2]
        return selected_dates[selected_dates['velocity'] > float(max_velocity)]


    def filter_by_date_return_country_count_too(self, date_1, date_2):
        return {self.df_days[date_1:date_2],self.df_days[date_1:date_2]['origin country'].value_counts()}
