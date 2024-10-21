import csv
Data = [{"Index": 1, "Naam": "Jan","Leeftijd": 14.3, "Type": "Leerling"} , {"Index": 2, "Naam": "Piet","Leeftijd": 16.8, "Type": "Leerling"}, {"Index": 3, "Naam": "Björn","Leeftijd": 40.7, "Type": "Meester"}]
Header = ["Index", "Naam", "Leeftijd", "Type"]

# Check dictionary door als tabel te tonen
from tabulate import tabulate
Data_list = []
for Row in Data:
    print(type(Row), Row)
    Regel = []
    for key, Item in Row.items():
        Regel.append(Item)
    Data_list.append(Regel)
print(tabulate(Data_list, headers=Header))

Schoolbestand = "Data\School_dict.csv"
"""
with open(Schoolbestand,"w+",newline="", encoding="utf-8") as csvfile:
    with csvfile:
        writer = csv.DictWriter(csvfile, fieldnames= Header)
        writer.writeheader()
        writer.writerows(Data)
    print("Succesvol geschreven")
"""
"""
with open(Schoolbestand, mode='r', newline='', encoding='utf-8') as file:
    Reader = csv.reader(file)
    # Elke rij (record) afdrukken
    for row in Reader:
        for item in row:
            print(item,end="\t")
        print("")
"""
input_file = csv.DictReader(open(Schoolbestand))
for row in input_file:
    for item in row.items():
        print(item, end="\t")
    print("")


