from Les9_data import *

def toon_docenten_of_cursisten(personen):
    gewenst = input("Docent of cursist: typ d of c: ")
    if gewenst.upper() == "D":
        for per in personen:
            if isinstance(per, Docent):
                print(per)
    elif gewenst.upper() == "C":
        for per in personen:
            if isinstance(per, Cursist):
                print(per)
    else: print("Foute keuze")

def voeg_docent_toe():
    id = int(input("Geef id: "))
    naam = input("Geef naam: ")
    leeftijd = int(input("Geef leeftijd: "))
    woonplaats = input("Geef woonplaats: ")
    maandloon = int(input("Geef maandloon: "))
    d = Docent(id, naam, leeftijd, woonplaats, maandloon)
    data_personen.append(d)

# voeg_docent_toe()
toon_docenten_of_cursisten(data_personen)