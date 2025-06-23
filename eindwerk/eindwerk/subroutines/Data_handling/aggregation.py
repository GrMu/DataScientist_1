"""
Here functions for data aggregation exist used by GUI_aggr
"""

# Import
import pandas as pd

# Resample data if under 1 min.
# Tiny function, but maybe needs to grow in future
def resample_data(data_in):
    data_in.resample('min').mean()
    return data_in

# Aggregate the data
def aggregate(data, data_info, nr_days_to_discern):
    aggregation = {'average': None, 'minimum': None, 'maximum': None}
    #--- Calculate minimum/average/maximum per (week)day (depending on 'nr_days_to_discern')
    # Calculate the average temperature profile for the days that have the same day number

    # Get start date. This is helpful for later operations when averaging days.
    # base_date = data[data_info['datetime_column']][0].date()  # Get first datetime
    base_date = data.index[0].date()  # Get first datetime
    # print("First element base date: ", base_date, type(base_date))
    base_date = pd.to_datetime(base_date)  # Ensures that the date starts at 00:00
    # print("Corrected base date: ", base_date, type(base_date))

    average_profiles = data.groupby([data.index.hour, data.index.minute, data['Day_nr'] % nr_days_to_discern]).mean().unstack()
    # print("average_profiles: \n", average_profiles)
    average_profiles['time_minutes'] = average_profiles.index.get_level_values(0)*60 + average_profiles.index.get_level_values(1)
    # print("average_profiles['time_minutes']: \n", average_profiles['time_minutes'])
    average_profiles['Datetime_(day)'] = base_date + pd.to_timedelta(average_profiles['time_minutes'], unit='m')
    # print("average_profiles['Datetime_(day)']: \n", average_profiles['Datetime_(day)'])
    # Calculate the minimum temperature profile for the days that have the same day number
    minimum_profiles = data.groupby([data.index.hour, data.index.minute, data['Day_nr'] % nr_days_to_discern]).min().unstack()
    # Calculate the minimum temperature profile for the days that have the same day number
    maximum_profiles = data.groupby([data.index.hour, data.index.minute, data['Day_nr'] % nr_days_to_discern]).max().unstack()
    aggregation['average'] = average_profiles
    aggregation['minimum'] = minimum_profiles
    aggregation['maximum'] = maximum_profiles
    return aggregation

# Smoothen data
def smoothen(data, filteroptions):
    # No good method found yet
    pass
