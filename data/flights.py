from data.load_pandas import load_minutes, load_days
from datetime import datetime
import pandas as pd
from datetime import timedelta
import numpy as np
from datetime import datetime


class Flights:
    def __init__(self):
        self.df_minutes = load_minutes()
        self.df_days = load_days()

        def clean_regions(x):
            set_regions = x.strip("{}").split(", ")
            clean = []
            for reg in set_regions:
                reg = reg.strip("\'")
                if reg == 'nan':
                    continue
                clean.append(reg)
            return clean
        self.df_days['state'] = self.df_days.oblast.apply(clean_regions)
        print("Dataset is ready...")

    @property
    def oblasts(self):
        return list(self.df_minutes.oblast.unique())

    def filter_flight_by_id(self, flight_id):
        # return flight_id
        return self.df_minutes[self.df_minutes['flight-id'] == flight_id]

    def filter(self, filter):
        selected_dates = self.df_days
        if 'date_1' in filter and 'date_2' in filter:
            selected_dates = self.df_days.loc[filter['date_1']:filter['date_2']]
        query = []
        if 'velocity' in filter:
            query.append('velocity >= ' + str(float(filter['velocity'])))
        if 'maxalt' in filter:
            query.append('barometric_altitude >= ' +
                         str(float(filter['maxalt'])))
        if 'spi' in filter:
            query.append('spi == ' + filter['spi'])
        if 'squawk' in filter:
            query.append('squawk == ' + filter['squawk'])
        if 'current_country' in filter:
            query.append('country.str.contains(\'|\'.join(\"' +
                         filter['current_country']+'\".split(\',\')))')
        if 'current_region' in filter:
            query.append('oblast.str.contains(\'|\'.join(\"' +
                         filter['current_region']+'\".split(\',\')))')
        if 'origin_country' in filter:
            query.append('origin_country.isin(\"' +
                         filter['origin_country']+'\".split(\',\'))')
        query = ' & '.join(query)
        if query == '':
            return selected_dates
        return selected_dates.query(query)

    def region_counted(self, filter):
        counted = {}

        def add_regions(x):
            for reg in x:
                if reg in counted:
                    counted[reg] = counted[reg] + 1
                else:
                    counted[reg] = 1
        self.filter(filter).state.apply(add_regions)
        return counted

    def matrix_absolute(self, filter):
        mod_filter = filter.copy()
        counted = self.region_counted({})
        for reg in counted:
            mod_filter['current_region'] = reg
            counted[reg] = self.region_counted(mod_filter)
        return counted

    def matrix_expected(self, filter):
        absolute = self.matrix_absolute(filter)
        mod_filter = filter.copy()
        if 'date_1' in filter and 'date_2' in filter:
            del mod_filter['date_1']
            del mod_filter['date_2']
        all_time = self.matrix_absolute(mod_filter)
        for reg1, val in all_time.items():
            for reg2, count in val.items():
                if reg1 not in absolute or reg2 not in all_time[reg1]:
                    all_time[reg1][reg2] = -all_time[reg1][reg2] / 117
                else:
                    all_time[reg1][reg2] = -all_time[reg1][reg2] / 117 + count / ((datetime.fromisoformat(
                        filter['date_2']) - datetime.fromisoformat(filter['date_1'])).days + 1)
        return all_time

    def count(self, filter):
        dates = pd.date_range(start=filter['date_1'],end=filter['date_2'])
        dates = pd.DataFrame(index=dates, columns=['count'])
        filter = self.filter(filter).groupby(level='date')['latitude, longitude'].count()
        return dates.join(filter).drop(columns=['count']).fillna(0)


    def parallel(self, filter):
        if 'date_1' in filter and 'date_2' in filter:
            selected_dates = self.df_days.loc[filter['date_1']:filter['date_2']]
            return selected_dates[['squawk', 'was_in_ukraine', 'spi']]
        else:
            return self.df_days[['squawk', 'was_in_ukraine', 'spi']]

    def filter_by_date_return_country_count_too(self, date_1, date_2):
        return {self.df_days[date_1:date_2], self.df_days[date_1:date_2]['origin country'].value_counts()}
