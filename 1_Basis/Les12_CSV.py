"""
# Test enumerate
lijst = ["Genk", "As", "Hoeselt"]
Enum1 = enumerate(lijst)
print(type(Enum1), Enum1)
print(list(Enum1))
print(list(enumerate(lijst, 2))) # begin index vanaf 2
"""

# Lees CSV-bestanden
import csv

Bestand = r"C:\Users\mulderg\OneDrive - VITO\Documents\werk\T2Campus_SyntraPXL\DataScientist\1ste_jaar\personeeldata.csv"
# Bestand = "C:\TEMP\personeeldata.csv" # Absoluut pad
# Bestand = "Data\Personeelsdata2.csv"  # Relatief pad
with open(Bestand, mode='r', newline='', encoding='utf-8') as file:
    Reader = csv.reader(file)
    print(type(Reader), Reader)
    # Elke rij (record) afdrukken
    for row in Reader:
        for item in row:
            print(item,end="\t")
        print("")

with open(Bestand, mode='r', newline='', encoding='utf-8') as file:
    Reader = csv.reader(file)
    # tabulate gebruiken. Eerst data in lists
    # Get header
    Header = []
    for row in Reader:
        for item in row:
            Header.append(item)
        break # alleen erste regel lezen
    print("Header is: ", Header)
    Data = []
    for row in Reader:
        Regel = []
        for item in row:
            Regel.append(item)
        Data.append(Regel)
print(Data)
print("")
from tabulate import tabulate
print(tabulate(Data, headers = Header))
