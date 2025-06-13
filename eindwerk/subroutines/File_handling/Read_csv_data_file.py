"""
This function reads a CSV file with automatic recognition of delimiter
"""

import csv
import clevercsv
import pandas as pd
import os


def read_csv_file_auto_2(csv_file):
    # find delimiter first with help of dialect that is found by sniffer
    # using clevercsv
    # clevercsv needs copyright statement:
    # CleverCSV is licensed under the MIT license.
    # Please cite our research if you use CleverCSV in your work.
    with open(csv_file, newline='') as csvfile:
        sample = csvfile.read(1024)
        dialect = clevercsv.Sniffer().sniff(sample)
        csvfile.seek(0)
        data = clevercsv.read_dataframe(csv_file)
        dialect_ = dialect
    '''
    Here code should come to detect decimal separator (and maybe thousands separator
    '''
    return data, sample, dialect_

def read_csv_file_auto_1(csv_file):
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
    data = pd.read_csv(csv_file, dialect=dialect_)

    return data, sample, dialect_

def read_csv_file_simple(csv_file):
    data = pd.read_csv(csv_file, sep=";", decimal=".")
    csv.register_dialect('custom', delimiter=';')
    dialect_ = csv.get_dialect('custom')
    sample = data[:1024]
    return data, sample, dialect_

def read_csv_file_with_method(csv_file, method):
    assert method in ["simple", "auto1", "auto2"], f"Read_csv_file_with_method has no method: {method}. \n"
    if method == 'simple':
        data, sample, dialect_ = read_csv_file_simple(csv_file)
    elif method == 'auto1':
        data, sample, dialect_ = read_csv_file_auto_1(csv_file)
    elif method == 'auto2':
        data, sample, dialect_ = read_csv_file_auto_2(csv_file)
    else:
        # Unnecessary since catched by assert statement
        raise(NotImplementedError(f"Read_csv_file_with_method has no method: {method}. \n"))
    return data, sample, dialect_


if __name__ == "__main__":
    # csv_file = "../../appdata/example_data/S21_profile.csv"
    csv_file = "C:/Users/mulderg/Downloads/1_January--GM--intermediate_1500--export.csv"
    # csv_file = "../../appdata/example_data/imdb.csv"
    output_data, sample, dialect = read_csv_file_with_method(csv_file, "auto2")  # auto1, simple, auto2
    # print("dialect : \n", help(dialect))
    print(f"Delimiter: {dialect.delimiter}")
    # print(f"Quote char: {dialect.quotechar}")
    # print(f"Line terminator: {repr(dialect.lineterminator)}")

    print("data : \n", output_data)
    print()
    columns_ = list(output_data.columns)
    print("columns: ", columns_)

