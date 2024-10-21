# Opmerking: databanken geven tuples terug

Steden = ("Hasselt", "Genk", "As", "Bree", "Lommel")
print(type(Steden), Steden)
for Stad in Steden:
    print(Stad)
# Hoe een element toevoegen?
# Steden.append("Gent") # Kan niet: onveranderbaar
# Oplossing: tijdelijk omzetten naar list
Steden = list(Steden)
print(type(Steden), Steden)
Steden.append("Hoeselt")
Steden = tuple(Steden)
print(type(Steden), Steden)
print(Steden[:-2])

# List met tuples
Lotto = [(5,18,21,27), (3,4,9,12)]
for Reeks in Lotto:
    for Getal in Reeks:
        print(Getal, end="\t")
    print("")

# tabulate blijkt te werken op tuples
from tabulate import tabulate
Header = ["Getal1","Getal2","Getal3","Getal4"]
print(tabulate(Lotto, headers=Header))

# Verwijderen element
Steden = list(Steden)
Steden.remove("As")
Steden = tuple(Steden)
# Korter, maar werkt echter niet:
# Steden = tuple( (list(Steden)).remove("Genk") )

# 1 item: afsluiten met komma!
not_a_tuple = ("Genk")
print(type(not_a_tuple))
this_tuple = ("Genk",)
print((type(this_tuple)))

# Uitbreiden kan niet met append of extend. Echter wel door een tupple toe te voegen via '+=':
Steden += this_tuple
print(Steden)

# inpakken en uitpakken
# uitpakken: elementen in tuple toekennen aan variabelen. Pas op: # variabelen moet kloppen!
"""
"""

# Gebruik van set
Voorbeeld_set = {"Genk", "Hassel", "As", "Hoeselt"}
Voorbeeld_set.add("Gent")
print((type(Voorbeeld_set)),Voorbeeld_set )

Element = ("Gent",)
Element2 = tuple("Genk") # Geen goed idee!
Element3 = tuple(["Maaseik"])
Steden_tuple = ("As", "Hoeselt")
Steden_tuple += Element
Steden_tuple += Element2
Steden_tuple += Element3
print(Steden_tuple)
