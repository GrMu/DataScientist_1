# Om mooie tabel te maken moet eerst dict worden gemaakt om aan de 'keys' geraken
# Maak dict via __dict__ of via vars
class auto:
    aantal_wagens = 0

    def __init__(self, merk, model, bouwjaar, brandstof, kleur):
        self.merk = merk
        self. model = model
        self.bouwjaar = bouwjaar
        self.brandstof = brandstof
        self.kleur = kleur
        auto.aantal_wagens += 1

    def geef_terug_als_dict(self):
        return self.__dict__        # Via __dict__

    def geef_terug_als_dict_2(self):
        return vars(self)           # Via vars

    def hoeveel_wagens(self):
        return (f"Het aantal wagens is {auto.aantal_wagens}")

a1 = auto("audi", "a5", 2020, "diesel", "rood")
a2 = auto("Tesla", "Y", 1990, "elektrisch", "wit")
a3 = auto("Toyota", "Verso", 2013, "diesel", "grijs")
lijst_wagens = [a1, a2, a3]

#Maak dict via .__dict__
dict_lijst= []
for item in (lijst_wagens):
    dict_lijst.append(auto.geef_terug_als_dict(item))
#Maak dict via vars()
dict_lijst_2= []
for item in (lijst_wagens):
    dict_lijst_2.append(auto.geef_terug_als_dict_2(item))

# Gebruik tabulate
from tabulate import tabulate
Keys = dict_lijst_2[0].keys()
list_lijst = []
for i, item in enumerate(dict_lijst_2):
    list_lijst.append(item.values())
print(tabulate(list_lijst, headers=Keys))

