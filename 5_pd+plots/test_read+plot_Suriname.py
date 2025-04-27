''' Read measurement data from Suriname and create plots with the average day per week'''
import pandas as pd
import matplotlib.pyplot as plt
import os

# --- Read the CSV file and rework the data ---
# FileWithPath = fr"C:\Users\mulderg\Downloads\1_January--GM--short.csv"
FileWithPath = fr"C:\Users\mulderg\Downloads\1_January--GM--tmp.csv"
data = pd.read_csv(FileWithPath, delimiter=';')
# print("Original data: ","\n", data)
# Convert the date column to datetime format
data['Date'] = pd.to_datetime(data['Date'])
# Drop rows where all columns except 'Date' are NaN
data = data.dropna(how='all', subset=data.columns.difference(['Date']))
# print("Cleaned DataFrame: ","\n", data)
# Merge lines with identical datetime:
# Group by Date and aggregate the values using 'max' for all columns
data = data.groupby('Date').max().reset_index()
# Set the date column as the index
data.set_index('Date', inplace=True)
# Fill empty elements with previous data
data.ffill()
# print("Merged DataFrame:", "\n", data)

#--- Write the cleaned data to file for later verification ---
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

'''
# Get the unique days in the data
unique_days = data.index.date
print("unique_days: ")
for element in unique_days:
    print(element)
'''

# Plot all data fo 1 column
plt.plot(data.index.date, data['PVP'])
plt.title(f'Data ')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()

'''
# Plot data for each day
for day in unique_days:
    daily_data = data.loc[data.index.date == day]
    plt.plot(daily_data.index, daily_data['PVP'])
    plt.title(f'Data for {day}')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.show()'''