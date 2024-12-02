# Maak een list van functies in een dict
def inhoud_balk():
    Lengte = float(input("Geef lengte: "))
    Breedte = float(input("Geef breedte: "))
    Hoogte = float(input("Geef hoogte: "))
    return Lengte*Breedte*Hoogte
def inhoud_kubus():
    Lengte = float(input("Geef lengte: "))
    return Lengte**3
import math
def inhoud_bol():
    Straal = float(input("Geef straal: "))
    return Lengte^3*math.pi*4/3
# Maak een dict van de functies
Functies = {1: inhoud_balk, 2: inhoud_kubus, 3: inhoud_bol} # Dus geen '()' toevoegen!

CorrecteKeus = True
while CorrecteKeus:
    print("Maak een keuze uit: ")
    for k, v in Functies.items():
        naam = v.__name__
        print( k, " : ", naam)
    try:
        Keuze = int(input("Geef uw keuze (of typ stop): "))
        if Keuze not in Functies:
            print("Ongeldige keuze, probeer opnieuw.")
        else:
            Resultaat = Functies[Keuze]() # Hier wel de '()'
            print("Resultaat is : ", Resultaat)
    except ValueError:
        CorrecteKeus = False
        print("Ongeldige keuze, programma wordt beëindigd")



