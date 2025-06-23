'''
Read measurement data from Suriname and create plots with the average day per week
'''
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from datetime import datetime
from scipy.signal._savitzky_golay import savgol_filter

# FileWithPath = fr"C:\Users\mulderg\Downloads\1_January--GM--short.csv"
# FileWithPath = fr"C:\Users\mulderg\Downloads\1_January--GM--intermediate_360.csv"
# FileWithPath = fr"C:\Users\mulderg\Downloads\1_January--GM--intermediate_750.csv"
# FileWithPath = fr"C:\Users\mulderg\Downloads\1_January--GM--intermediate_1500.csv"
# FileWithPath = fr"C:\Users\mulderg\Downloads\1_January--GM--daytest.csv"
FileWithPath = fr"C:\Users\mulderg\Downloads\1_January.csv"
# FileWithPath = fr"C:\Users\mulderg\Downloads\10_October.csv"
# FileWithPath = fr"C:\Users\mulderg\PycharmProjects\Plot_weekday_avg_from_yeardata\data\family_solar_economic.csv"
# FileWithPath = fr"C:\Users\mulderg\Downloads\temperature_data_genk.csv"
column_name_datetime = 'Date'
# column_name_datetime = 'Datetime'
column_name_plot = 'Total_power' #'SOC' #'PVP'
# column_name_plot = 'Family [W]'
time_format = "%Y-%m-%d %H:%M:%S"
# time_format = "%d/%m/%Y %H:%M"
f_window_length = 16
f_polyorder = 4
nr_days_to_discern = 1 # For averaging daily data: set to 7 for each weekday, or 1

def printdata(name, data, nr_lines, position):
    nr_lines_corr = min(nr_lines, len(data) - position)
    # print("Lengte data: ", len(data))
    # print("nr_lines_corr: ", nr_lines_corr)
    print(f"{name}")
    print(data.iloc[position:nr_lines_corr+position])
    # print(data.iloc[position:position+nr_lines_corr])

def write_data(FileWithPath, data):
    # --- Write the cleaned data to file for later verification ---
    # Split the path and filename
    path, filename = os.path.split(FileWithPath)
    # Extract the file extension
    file_extension = os.path.splitext(filename)[1]
    # Add '--export' to the filename
    new_filename = filename.replace(file_extension, f'--export{file_extension}')
    # Create the new file path
    new_file_path = os.path.join(path, new_filename)
    # Write the data to the new CSV file with the updated filename
    data.to_csv(new_file_path, index=True, sep=';', header=True)
    print(f"Data has been written to the new file: {new_file_path}")

# --- Read the CSV file and rework the data ---
data = pd.read_csv(FileWithPath, delimiter=';')
# printdata("Original data: ", data, 10, 0)
# Convert the date column to datetime format
data[column_name_datetime] = pd.to_datetime(data[column_name_datetime], format=time_format)
# data[column_name_datetime] = pd.to_datetime(data[column_name_datetime])
print("Datalengte van origineel: ", data.shape[0], "rows, ", data.shape[1], "columns." )
# Get start date. This is helpful for later operations when averaging days.
base_date = data[column_name_datetime][0].date() #Get first datetime
print("First element base date: ", base_date, type(base_date))
base_date = pd.to_datetime(base_date) # Ensures that the date starts at 00:00
print("Corrected base date: ", base_date, type(base_date))
# Drop rows where all columns except 'Date' are NaN
data = data.dropna(how='all', subset=data.columns.difference([column_name_datetime]))
# printdata("Cleaned DataFrame: ", data, 10, 0)
# Merge lines with identical datetime:
# Group by Date and aggregate the values using 'max' for all columns
data = data.groupby(column_name_datetime).max().reset_index()
# Fill empty elements with previous data
data.ffill(inplace=True)
#--- add information about the weekday ---
# data['Day'] = data[column_name_datetime].dt.day_name()
data['Day_nr'] = data[column_name_datetime].dt.day_of_week
# Set the date column as the index. This only can after the .dt operations
data.set_index(column_name_datetime, inplace=True)
data['Total_power']=data['PWR']+data['NF_PWP01']+data['NF_PWP02']+data['NF_PWP03']+data['NF_PWP05']+data['DS_PWP01']+data['DS_PWP02']
print("Datalengte voor hersampling: ", data.shape[0], "rows, ", data.shape[1], "columns." )
print('columns: ', data.columns)

# Calculate the difference between consecutive timestamps
time_deltas = data.index.to_series().diff().dropna()
# Get the most common timestep (mode) in the dataframe
timestep = time_deltas.mode()[0]
timestep_seconds = timestep.total_seconds()
print(f"The timestep is: {timestep} and in seconds: {timestep_seconds}")
print("type timestep: ", type(timestep))
time_deviation = time_deltas.std()
time_deviation_seconds = time_deviation.total_seconds()
print(f"The deviation in time is: {time_deviation} and in seconds: {time_deviation_seconds}")


# Downscale data. This makes the averaging over the days better since the timestamps agree.
if timestep_seconds < 60:
    data = data.resample('min').mean()
    print("Datalengte na hersampling: ", data.shape[0], "rows, ", data.shape[1], "columns." )
printdata("Merged DataFrame:", data, 20, 000)
# write_data(FileWithPath, data)


# Plot all data for 1 column
plt.plot(data[column_name_plot]) # 'PVP'
plt.title(f'January ')
plt.xlabel('Time')
plt.ylabel('Demand power')
plt.show()


# Get the unique days in the data
unique_days = data.index.date

'''
# Plot data for each day in one graph
plt.figure(figsize=(12, 7))
for day in unique_days:
    daily_data = data.loc[data.index.date == day]
    # plt.plot(daily_data.index, daily_data[column_name_plot], label=f'Day {day}') # all days consecutively
    plt.plot(daily_data.index.hour + daily_data.index.minute / 60, daily_data[column_name_plot], label=f'Day {day}')
plt.title('Temperature Data for 14 Days in Genk')
plt.xlabel('DateTime')
plt.ylabel('Temperature')
plt.legend()
plt.show()
'''
#--- Calculate minimum/average/maximum per (week)day (depending on 'nr_days_to_discern')
# Calculate the average temperature profile for the days that have the same day number
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

'''
#--- Replace the multi-index due to groupby to a datetime-index (needed for filtering)
# Reset the index to get hour and minute as columns
df_reset = data.reset_index()
# Assuming the original date is known (e.g., '2023-01-01')
original_date = '2023-01-01'
# Create a new datetime column
df_reset['Timestamp'] = pd.to_datetime(original_date) + pd.to_timedelta(df_reset['hour'], unit='h') + pd.to_timedelta(df_reset['minute'], unit='m')
# Set the new datetime column as the index
df_reset.set_index('Timestamp', inplace=True)
# Drop the now redundant hour and minute columns
# df_final = df_reset.drop(columns=['hour', 'minute'])
print("df_reset: /n ", df_reset)
'''
'''
#--- smoothen the data with help of filter 
average_profiles_f = []
for day, _ in enumerate(average_profiles):
    average_profiles_f[day] = savgol_filter(average_profiles[column_name_plot][day], window_length=f_window_length, polyorder=f_polyorder)
print(average_profiles_f)
'''
'''
# Plot the average temperature profiles for each day number (nr_days_to_discern)
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
plt.figure(figsize=(12, 7))
for day in range(nr_days_to_discern):
    plt.plot(average_profiles.index.get_level_values(0) + average_profiles.index.get_level_values(1) / 60, average_profiles[column_name_plot].iloc[:, day], label=days[day])
plt.title('Average power over each weekday')
plt.xlabel('Hour of the Day')
plt.ylabel('Power')
plt.xticks(np.arange(0, 25, 1)) # Set x-axis ticks to show every hour
plt.legend()
plt.show()
'''

# Plot the average temperature profiles for each day number (nr_days_to_discern)
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# Find the maximum value among all plots
'''max_y_values = []
for day in range(nr_days_to_discern):
    day_profile = average_profiles[column_name_plot].iloc[:, day]
    print("day_profile \n", day_profile)
    max_y_values[day] = max(day_profile.reset_index)
    # max_y_values[day] = max(average_profiles.iloc[:, day].max(), minimum_profiles.iloc[:, day].max(), maximum_profiles.iloc[:, day].max())
'''
max_y_values = maximum_profiles[column_name_plot].max()
max_y_value = max(max_y_values)
min_y_values = minimum_profiles[column_name_plot].min()
min_y_value = min(min_y_values)
'''min_y_value = min(average_profiles[0].max(), minimum_profiles[0].min(), maximum_profiles[0].min())
if min_y_value > 0:
    min_y_value = 0'''
'''max_y_value = max(max_y_values)
print('min_Y:', min_y_value, "max_Y; ", max_y_value)
'''
# min_y_value = 0
# max_y_value = 10000 # 110 # 10000
parameter = 'Demand [W?]'# 'SOC' # 'PV power'
# Create a figure and a grid of subplots
fig, axs = plt.subplots(1, 3, figsize=(14, 5), sharey=False)
# Plot with minimum
for day in range(nr_days_to_discern):
    axs[0].plot(minimum_profiles.index.get_level_values(0) + minimum_profiles.index.get_level_values(1) / 60, minimum_profiles[column_name_plot].iloc[:, day], label=days[day])
# axs[0].set_ylim(min_y_value, max_y_value)
axs[0].set_title(f'Minimum {parameter} found over each day')
axs[0].set_xlabel('Hour of the Day')
axs[0].set_ylabel(parameter)
axs[0].set_xticks(np.arange(0, 25, 2)) # Set x-axis ticks to show every hour
# axs[0].legend()
# Plot with average
for day in range(nr_days_to_discern):
    axs[1].plot(average_profiles.index.get_level_values(0) + average_profiles.index.get_level_values(1) / 60, average_profiles[column_name_plot].iloc[:, day], label=days[day])
# axs[1].set_ylim(min_y_value, max_y_value)
axs[1].set_title(f'Average {parameter} over each day')
axs[1].set_xlabel('Hour of the Day')
axs[1].set_ylabel(parameter)
axs[1].set_xticks(np.arange(0, 25, 2)) # Set x-axis ticks to show every hour
# axs[1].legend()
# Plot with maximum
for day in range(nr_days_to_discern):
    axs[2].plot(maximum_profiles.index.get_level_values(0) + maximum_profiles.index.get_level_values(1) / 60, maximum_profiles[column_name_plot].iloc[:, day], label=days[day])
# axs[2].set_ylim(min_y_value, max_y_value)
# axs[2].set_title('Maximum power found over each day')
axs[2].set_title(f'Maximum {parameter} found over each day')
axs[2].set_xlabel('Hour of the Day')
axs[2].set_ylabel(parameter)
axs[2].set_xticks(np.arange(0, 25, 2)) # Set x-axis ticks to show every hour
# axs[2].legend()
# Get the limits of the axes of the plots and derive the min. and max. value.
limits=[]
for i, _ in enumerate(axs):
    print("i", i)
    limits.append(axs[i].get_ylim())
# print("limits: ", limits)
# Extract all values from the list of tuples
lim_values = [item for sublist in limits for item in sublist]
min_value = min(lim_values)
max_value = max(lim_values)
lim_new = (min_value, max_value)
plt.setp(axs, ylim=lim_new)
plt.tight_layout() # Adjust layout to prevent overlap
plt.show()
