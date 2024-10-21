import csv
Data = [[1, "Jan", 14.3, "Leerling"], [2, "Piet", 16.8, "Leerling"], [3, "Björn", 40.7, "Meester"]]
Header = ["Nummer", "Naam", "Leeftijd", "Type"]
from tabulate import tabulate
print(tabulate(Data, headers=Header))

Schoolbestand = "Data\School.csv"
with open(Schoolbestand,"w+",newline="", encoding="utf-8") as csvfile:
    with csvfile:
        write = csv.writer(csvfile)
        write.writerow(Header)
        write.writerows(Data)
    print("Succesvol geschreven")

with open(Schoolbestand, mode='r', newline='', encoding='utf-8') as file:
    Reader = csv.reader(file)
    # Elke rij (record) afdrukken
    for row in Reader:
        for item in row:
            print(item,end="\t")
        print("")



