"""
This function reads a CSV file with automatic recognition of delimiter
"""

import csv
import pandas as pd
import os

def read_csv_file_auto_1(csv_file):
    # find delimiter first with help of dialect that is found by sniffer
    with open(csv_file, 'r', encoding='utf-8') as file:
        sample = file.read(1024)
        print("sample ", sample)
        dialect_ = csv.Sniffer().sniff(sample)  # The delimiter list may be omitted , [',', ';', '\t']
    # Now, use the detected dialect to read the CSV file
    '''
    Here code should come to detect decimal separator (and maybe thousands separator
    '''
    data = pd.read_csv(csv_file, dialect=dialect_)

    return data, dialect_

def read_csv_file_simple(csv_file):
    data = pd.read_csv(csv_file, sep=";", decimal=".")
    csv.register_dialect('custom', delimiter=';')
    dialect_ = csv.get_dialect('custom')
    return data, dialect_

def read_csv_file_with_method(csv_file, method):
    if method == 'simple':
        data, dialect_ = read_csv_file_simple(csv_file)
    elif method == 'auto1':
        data, dialect_ = read_csv_file_auto1(csv_file)
    else:
        raise(NotImplementedError)
        print(f"Read_csv_file_with_method has no method: {method}. \n")
    return data, dialect_


if __name__ == "__main__":
    # csv_file = "../../appdata/example_data/S21_profile.csv"
    csv_file = "C:/Users/mulderg/Downloads/1_January--GM--intermediate_1500--export.csv"
    output_data, dialect = read_csv_file_with_method(csv_file, "simple")
    # print("dialect : \n", help(dialect))
    print(f"Delimiter: {dialect.delimiter}")
    print(f"Quote char: {dialect.quotechar}")
    print(f"Line terminator: {repr(dialect.lineterminator)}")

    print("data : \n", output_data)
    print()
    # for row in output_data:
    #    print(row)

    print("columns: ", output_data.columns)

