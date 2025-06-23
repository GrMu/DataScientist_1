"""
This function reads a CSV file with automatic recognition of delimiter
"""

import csv
import clevercsv
import pandas as pd
import os

# Global variables, to be updated in the functions on header file
# They are used when reading the file (with correct delimiter) and to store statistics
header_info={'sample': "", 'dialect': "", 'file_path': "", 'raw columns': []}
# Note: timestep and time_deviation are calculated in GUI_file_handling since only then
# datetime can be derived.
data_info = {'orig_rows': 0, 'orig_columns': 0, 'cleaned_rows': 0, 'cleaned_columns': 0,
             'datetime_column': 'no datetime', 'datetime_format': "", 'columns': [],
             'timestep': None, 'time_deviation': None,
             'data_name': "empty", 'data_path': None }


def calculate_avg_timestep(data):
    # Calculate the difference, deviation and max. between consecutive timestamps
    time_deltas = data.index.to_series().diff().dropna()
    # Get the most common timestep (mode) in the dataframe
    timestep = time_deltas.mode()[0]
    # print("timestep: ", timestep, "type: ", type(timestep))
    #time step_seconds = timestep.total_seconds()  # Does not function anymore: strange
    # print(f"The timestep is: {timestep} and in seconds: {timestep_seconds}")
    time_deviation = time_deltas.std().round('s ')
    time_maxstep =  time_deltas.max()
    return timestep, time_deviation, time_maxstep


def clean_data_without_datetime(data):
    # Drop rows where all columns except 'Date' are NaN
    # print("data before cleaning")
    # print(data)
    # print()
    data = data.dropna(how='all', subset=data.columns.difference(data.index))
    # printdata("Cleaned DataFrame: ", data, 10, 0)
    # Fill empty elements with previous data
    data.ffill(inplace=True)
    return data

def clean_data_with_datetime(data):
    global data_info
    # Drop rows where all columns except 'Date' are NaN
    data = data.dropna(how='all', subset=data.columns.difference([data_info['datetime_column']]))
    # printdata("Cleaned DataFrame: ", data, 10, 0)
    # Merge lines with identical datetime:
    # Group by Date and aggregate the values using 'max' for all columns
    data = data.groupby(data_info['datetime_column']).max().reset_index()
    # Fill empty elements with previous data
    data.ffill(inplace=True)
    # --- add information about the weekday ---
    # data['Day'] = data[datetime_column].dt.day_name()
    data['Day_nr'] = data[data_info['datetime_column']].dt.day_of_week
    # Set the date column as the index. This only can after the .dt operations
    data.set_index(data_info['datetime_column'], inplace=True)  # inplace=True: Necessary to calculate avg. timestep
    # print(f"cleaned data : \n{data} \n ")
    return data

def column_names_from_sample():
    global header_info
    delim = header_info['dialect'].delimiter
    # Split the data into lines
    lines = header_info['sample'].split('\n')
    # Get the first line which contains the column names and strip any trailing whitespace and '\r'
    column_names_line = lines[0].strip()
    # Split the column names line by delimiter ";"
    column_names = column_names_line.split(delim)
    print("column_names: ", column_names)
    return column_names

def header_csv_file_auto_2(csv_file):
    global header_info
    # find delimiter first with help of dialect that is found by sniffer
    # using clevercsv
    # clevercsv needs copyright statement:
    # CleverCSV is licensed under the MIT license.
    # Please cite our research if you use CleverCSV in your work.
    header_info['file_path'] = csv_file
    with open(csv_file, newline='') as csvfile:
        header_info['sample'] = csvfile.read(1024)
        header_info['dialect'] = clevercsv.Sniffer().sniff(header_info['sample'])
        csvfile.seek(0)
    header_info['raw columns'] = column_names_from_sample()
    # data = clevercsv.read_dataframe(sample)

    # data = pd.read_csv(csv_file, dialect=dialect)
    # print("sample via clevercsv: ", header_info['sample'])

    # print("data via clevercsv: ", data)
    '''
    Here code should come to detect decimal separator (and maybe thousands separator
    '''
    return header_info

def header_csv_file_auto_1(csv_file):
    # find delimiter first with help of dialect that is found by sniffer
    # using Python's standard method (= bad unfortunately)
    global header_info
    header_info['file_path'] = csv_file
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        header_info['sample'] = file.read(1024)
        # print("sample ", header_info['sample'])
        header_info['dialect'] = csv.Sniffer().sniff(header_info['sample'])  # The delimiter list may be omitted , [',', ';', '\t']
    # Now, use the detected dialect to read the CSV file
    '''
    Here code should come to detect decimal separator (and maybe thousands separator
    '''
    data = pd.read_csv(header_info['sample'], dialect=header_info['dialect'])
    header_info['raw columns'] = list(data.columns)
    header_info['file_path'] = csv_file
    header_info['sample'] = sample
    header_info['dialect'] = dialect_
    return header_info

def header_csv_file_simple(csv_file):
    global header_info
    header_info['file_path'] = csv_file
    data = pd.read_csv(csv_file, sep=";", decimal=".")
    csv.register_dialect('custom', delimiter=';')
    header_info['dialect'] = csv.get_dialect('custom')
    header_info['sample'] = data[:1024]
    header_info['raw columns'] = list(data.columns)
    header_info['file_path'] = csv_file
    header_info['sample'] = sample_
    header_info['dialect'] = dialect_
    return header_info

"""
Functions that can be called from outside
First header_csv_file_with_method should be called to derive header_info
then read_file can b called to deribe data_info and the data (pandas).  
"""

def header_csv_file_with_method(csv_file, method):
    assert method in ["simple", "auto1", "auto2"], f"Header_csv_file_with_method has no method: {method}. \n"
    if method == 'simple':
        header_info = header_csv_file_simple(csv_file)
    elif method == 'auto1':
        header_info = header_csv_file_auto_1(csv_file)
    elif method == 'auto2':
        header_info = header_csv_file_auto_2(csv_file)
    else:
        # Unnecessary since catched by assert statement
        raise(NotImplementedError(f"Read_csv_file_with_method has no method: {method}. \n"))
    return header_info

def read_file(datetime_column, datetime_format):
    global header_info
    global data_info
    data_info['datetime_column'] = datetime_column
    data_info['datetime_format'] = datetime_format
    data = pd.read_csv(header_info['file_path'], sep=header_info['dialect'].delimiter, decimal=".")
    data.columns.name = 'Index'
    data_info['orig_rows'] = data.shape[0]
    data_info['orig_columns'] = data.shape[1]
    # derive filename without extension and path from filepath:
    file_ = os.path.basename(header_info['file_path'])
    file_name = os.path.splitext(file_)[0]
    data_info['data_name'] = file_name
    data_info['data_path'] = os.path.dirname(header_info['file_path'])
    if data_info['datetime_column'] != 'no datetime': # So, data has datetime
        # Convert the date column to datetime format
        data[data_info['datetime_column']] = pd.to_datetime(data[data_info['datetime_column']], format=data_info['datetime_format'])
        data = clean_data_with_datetime(data)
        timestep, deviation, max = calculate_avg_timestep(data)
        data_info['cleaned_rows'] = data.shape[0]
        data_info['cleaned_columns'] = data.shape[1]
        # print(f"pandas columns: {list(data.columns)} \n")
        data_info['columns'] = list(data.columns)
        data_info['timestep'] = timestep
        data_info['time_deviation'] = deviation
        data_info['time_maxstep'] = max
    else:
        # print('no datetime case')
        data = clean_data_without_datetime(data)
        data_info['cleaned_rows'] = data.shape[0]
        data_info['cleaned_columns'] = data.shape[1]
        # print(f"pandas columns: {list(data.columns)} \n")
        data_info['columns'] = list(data.columns)  # Index lacks !!!!!!!!!!!!!
        data_info['timestep'] = None
        data_info['time_deviation'] = None
        data_info['time_maxstep'] = None
    print("data_info within read function: ", data_info)
    return data, data_info


if __name__ == "__main__":
    # Possibility to test and debug this module

    # csv_file = "../../appdata/example_data/S21_profile.csv"
    csv_file = "C:/Users/mulderg/Downloads/1_January--GM--intermediate_1500--export.csv"
    # header info is a dictionary of 'sample', 'dialect', 'file_path' and 'raw columns'
    # Get this information by reading start of the file using a specific method
    header_info = header_csv_file_with_method(csv_file, "auto2")  # auto1, simple, auto2
    # print("dialect : \n", help(data_info['dialect']))
    print(f"Delimiter: {header_info['dialect'].delimiter}")
    # print(f"Quote char: {header_info['dialect'].quotechar}")
    # print(f"Line terminator: {repr(header_info['dialect'].lineterminator)}")
    # print(f"sample : \n, {header_info['sample']} \n")
    # print("(raw) columns: ", header_info['raw columns'])
    # Now read the file and use pandas to store the data
    data, data_info = read_file('Date', "%Y-%m-%d %H:%M:%S")  # 'no datetime'
    # test: it may be more interesting to avoid datetime as index. This makes plotting more generic afterwards.
    data.reset_index(inplace=True)
    # print(f" Resetted data: \n{data}\n")
    print("data_info: ", data_info)