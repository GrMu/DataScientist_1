"""
This function reads a CSV file with automatic recognition of delimiter
"""

import csv
import clevercsv
import pandas as pd
import os

# Global variables, to be updated in the functions on header file
# They are used when reading the file (with correct delimiter)
sample_ = ""
dialect_= ""
file_path_ = ""

def read_file(datetime_column, datetime_format):
    data = pd.read_csv(file_path_, sep=dialect_.delimiter, decimal=".")
    # Convert the date column to datetime format
    data[datetime_column] = pd.to_datetime(data[datetime_column], format=datetime_format)
    return data

def column_names_from_sample(sample, dialect):
    delim = dialect.delimiter
    # Split the data into lines
    lines = sample.split('\n')
    # Get the first line which contains the column names and strip any trailing whitespace and '\r'
    column_names_line = lines[0].strip()
    # Split the column names line by delimiter ";"
    column_names = column_names_line.split(delim)
    print("column_names: ", column_names)
    return column_names

def header_csv_file_auto_2(csv_file):
    # find delimiter first with help of dialect that is found by sniffer
    # using clevercsv
    # clevercsv needs copyright statement:
    # CleverCSV is licensed under the MIT license.
    # Please cite our research if you use CleverCSV in your work.
    with open(csv_file, newline='') as csvfile:
        sample = csvfile.read(1024)
        dialect = clevercsv.Sniffer().sniff(sample)
        csvfile.seek(0)
    columns = column_names_from_sample(sample, dialect)
    # data = clevercsv.read_dataframe(sample)

    # data = pd.read_csv(csv_file, dialect=dialect)
    print("sample via clevercsv: ", sample)

    # print("data via clevercsv: ", data)
    '''
    Here code should come to detect decimal separator (and maybe thousands separator
    '''
    globals()['file_path_'] = csv_file
    globals()['sample_'] = sample
    globals()['dialect_'] = dialect
    return columns, sample, dialect

def header_csv_file_auto_1(csv_file):
    # find delimiter first with help of dialect that is found by sniffer
    # using Python's standard method (= bad unfortunately)
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        sample = file.read(1024)
        print("sample ", sample)
        dialect_ = csv.Sniffer().sniff(sample)  # The delimiter list may be omitted , [',', ';', '\t']
    # Now, use the detected dialect to read the CSV file
    '''
    Here code should come to detect decimal separator (and maybe thousands separator
    '''
    data = pd.read_csv(sample, dialect=dialect_)
    columns_ = list(data.columns)
    globals()['file_path_'] = csv_file
    globals()['sample_'] = sample
    globals()['dialect_'] = dialect_
    return columns_, sample, dialect_

def header_csv_file_simple(csv_file):
    data = pd.read_csv(csv_file, sep=";", decimal=".")
    csv.register_dialect('custom', delimiter=';')
    dialect_ = csv.get_dialect('custom')
    sample = data[:1024]
    columns_ = list(data.columns)
    globals()['file_path_'] = csv_file
    globals()['sample_'] = sample
    globals()['dialect_'] = dialect_
    return columns_, sample, dialect_

def header_csv_file_with_method(csv_file, method):
    assert method in ["simple", "auto1", "auto2"], f"Header_csv_file_with_method has no method: {method}. \n"
    if method == 'simple':
        columns, sample, dialect_ = header_csv_file_simple(csv_file)
    elif method == 'auto1':
        columns, sample, dialect_ = header_csv_file_auto_1(csv_file)
    elif method == 'auto2':
        columns, sample, dialect_ = header_csv_file_auto_2(csv_file)
    else:
        # Unnecessary since catched by assert statement
        raise(NotImplementedError(f"Read_csv_file_with_method has no method: {method}. \n"))
    return columns, sample, dialect_


if __name__ == "__main__":
    # csv_file = "../../appdata/example_data/S21_profile.csv"
    csv_file = "C:/Users/mulderg/Downloads/1_January--GM--intermediate_1500--export.csv"
    # csv_file = "../../appdata/example_data/imdb.csv"
    columns_, sample, dialect = header_csv_file_with_method(csv_file, "auto2")  # auto1, simple, auto2
    # print("dialect : \n", help(dialect))
    print(f"Delimiter: {dialect.delimiter}")
    # print(f"Quote char: {dialect.quotechar}")
    # print(f"Line terminator: {repr(dialect.lineterminator)}")

    print("sample : \n", sample)
    print()
    print("columns: ", columns_)

