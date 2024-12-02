class auto:
    aantal_wagens = 0

    def __init__(self, merk, model, bouwjaar, brandstof, kleur):
        self.merk = merk
        self. model = model
        self.bouwjaar = bouwjaar
        self.brandstof = brandstof
        self.kleur = kleur
        auto.aantal_wagens += 1

    def __str__(self):
        return(f"Auto heeft merk {self.merk} en model {self.model}")

    def geef_terug_als_dict(self):
        return self.__dict__

    def hoeveel_wagens(self):
        return (f"Het aantal wagens is {auto.aantal_wagens}")

a1 = auto("audi", "a5", 2020, "diesel", "rood")
a2 = auto("Tesla", "Y", 1990, "elektrisch", "wit")
a3 = auto("Toyota", "Verso", 2013, "diesel", "grijs")
lijst_wagens = [a1, a2, a3]
a4 = auto("Ford", "Fiesta", 2016, "benzine", "blauw")
lijst_wagens.append(a4)
for wagen in lijst_wagens:
    print(wagen)

def voeg_auto_toe_aan_lijst():
    merk = input("Geef merk in: ")
    model = input("Geef model in: ")
    bouwjaar = input("Geef bouwjaar in: ")
    brandstof = input("Geef brandstof in: ")
    kleur = input("Geef kleur in: ")
    a = auto(merk, model, bouwjaar, brandstof, kleur)
    return a

def bestaat_merk(lijst, zoek_merk):
    for a in lijst:
        gevonden = False
        if a.merk == zoek_merk:
            gevonden =True
            break
    if gevonden ==True :
        print("Merk gevonden")
    else : print("Merk niet gevonden")

def verander_model(lijst):
    oud_model = input("Geef model in: ")
    nieuw_model = input("Geef nieuw model in: ")
    for a in lijst.model:
        if a == oud_model:
            a = nieuw_model
            break
    return lijst

bestaat_merk(lijst_wagens, "Ford")

# a5 = voeg_auto_toe_aan_lijst()
lijst_wagens.append(a4)
print(lijst_wagens)
#Maak dict
dict_lijst= []
lijst_wagens[0]
for item in (lijst_wagens):
    dict_lijst.append(auto.geef_terug_als_dict(item))
print(lijst_wagens)
# Gebruik tabulate
from tabulate import tabulate
Keys = dict_lijst[0].keys()
list_lijst = []
for i, item in enumerate(dict_lijst):
    list_lijst.append(item.values())
print(tabulate(list_lijst, headers=Keys))

