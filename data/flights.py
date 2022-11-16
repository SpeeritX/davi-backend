from data.load_pandas import load_minutes, load_days, load_parallel
from datetime import datetime
import pandas as pd
from datetime import timedelta
import numpy as np


class Flights:
    def __init__(self):
        self.df_minutes = load_minutes()
        self.df_days = load_days()
        self.df_parallel = load_parallel()
        print("Dataset is ready...")

    @property
    def oblasts(self):
        return list(self.df_minutes.oblast.unique())

    def filter_flight_by_id(self, flight_id):
        #return flight_id
        return self.df_minutes[self.df_minutes['flight-id'] == flight_id]

    def filter(self, filter):
        if filter['date_1'] != '' and filter['date_2'] != '':
            selected_dates = self.df_days.loc[filter['date_1']:filter['date_2']]
        if len(filter) == 2:
            return selected_dates
        query = []
        if 'velocity' in filter:
            query.append('velocity >= ' + str(float(filter['velocity'])))
        if 'maxalt' in filter:
            query.append('barometric_altitude >= ' + str(float(filter['maxalt'])))
        if 'spi' in filter:
            query.append('spi == ' + filter['spi'])
        if 'squawk' in filter:
            query.append( 'squawk == ' + filter['squawk'])
        if 'current country' in filter:
            query.append('country.str.contains(\'|\'.join(\"'+filter['current country']+'\".split(\',\')))')
        if 'origin country' in filter:
            query.append('origin_country.isin(\"'+filter['origin country']+'\".split(\',\'))')
        query = ' & '.join(query)
        return selected_dates.query(query)

    def count(self, filter):
        if filter['date_1'] != '' and filter['date_2'] != '':
            selected_dates = self.df_days.loc[filter['date_1']:filter['date_2']]
        if len(filter) == 2:
            return selected_dates.groupby(level='date')["latitude, longitude"].count()
        query = []
        if 'velocity' in filter:
            query.append('velocity >= ' + str(float(filter['velocity'])))
        if 'maxalt' in filter:
            query.append('barometric_altitude >= ' + str(float(filter['maxalt'])))
        if 'spi' in filter:
            query.append('spi == ' + filter['spi'])
        if 'squawk' in filter:
            query.append( 'squawk == ' + filter['squawk'])
        if 'current country' in filter:
            query.append('country.str.contains(\'|\'.join(\"'+filter['current country']+'\".split(\',\')))')
        if 'origin country' in filter:
            query.append('origin_country.isin(\"'+filter['origin country']+'\".split(\',\'))')
        query = ' & '.join(query)
        return selected_dates.query(query).groupby(level='date')['latitude, longitude'].count()

    def parallel(self, filter):
        if 'date_1' in filter and 'date_2' in filter:
            selected_dates = self.df_parallel.loc[filter['date_1']:filter['date_2']]
            return selected_dates
        else:
            return self.df_parallel

    def filter_by_date_return_country_count_too(self, date_1, date_2):
        return {self.df_days[date_1:date_2],self.df_days[date_1:date_2]['origin country'].value_counts()}
