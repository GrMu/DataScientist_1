# Dictionaries intro
Persoon = {"naam":"Bert", "leeftijd":40}
print(Persoon)
nieuwe_key = "plaats"
nieuwe_value = "Hasselt"
Persoon[nieuwe_key]=nieuwe_value
for item in Persoon:
    print(item)
for item in Persoon.values():
    print(item)
for k,v in Persoon.items(): #!!
    print(k,v)
print("Aantal elementen:",len(Persoon))
print(Persoon.keys())
print(Persoon.values())
print(Persoon.items())

# Dictionaries in list
Persoon1 = {"naam":"Bert", "leeftijd":40}
Persoon2 = {"naam":"Bart", "leeftijd":42, "stad":"Genk"}
Persoon3 = {"naam":"Bern", "leeftijd":44}
Lijst_personen = [Persoon1, Persoon2, Persoon3]
print(Lijst_personen)
for Pers in Lijst_personen:
    for item in Pers.values():
        print(item, end="\t")
    print("")
for header in Persoon1.keys():
    print(header, end="\t")
print("")
for Pers in Lijst_personen:
    for item in Pers.values():
        print(item, end="\t")
    print("")
# Met tabulate combineren: eerst een matrix maken
Matrix = []
for Pers in Lijst_personen:
    Vector = []
    for item in Pers.values():
        Vector.append(item)
    Matrix.append(Vector)
from tabulate import tabulate
# print(tabulate(Matrix, headers= Persoon1.keys(), tablefmt="fancy_grid") )
print(tabulate(Lijst_personen, headers= Persoon1.keys(), tablefmt="fancy_grid") ) # tabulate werkt in principe met dictionaries


