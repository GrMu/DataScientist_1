"""
Dit is de uitwerking van de examenopdrachten betreft Leren Programmeren in Python
door Grietus Mulder
"""
# Variabelen
Invoerbestand = "Data\muzikanten_data.csv"
Uitvoerbestand = "Data\muzikanten_nieuw.csv"
Key_te_wijzigen = "instrument"
Key_om_op_te_zoeken = "genre"
Key_naam = "artiestennaam"

# Import
from tabulate import tabulate
import csv
from tabulate import tabulate
from colorama import Fore

# Initialisatie
Muzikantendata = [] # List met dictionaries
Tabel_list = []
Header = []
Keuze = None
Foute_keus = 0

# Definities van lager niveau
def Tabel_uit_List_van_Dicts(Data_lokaal, MetIndex):
    eerste_item = Data_lokaal[0]
    Header_lokaal = [key for key in eerste_item.keys()]
    # print("Header is: ", Header)
    Persoonsgegevens_matrix = []
    for Row_Dict in Data_lokaal:
        Persoonsgegevens_vector = []
        # print("Row:", Row_Dict)
        for item,waardes in Row_Dict.items():
            Persoonsgegevens_vector.append(waardes)
        # print("Persoonsgegevens_vector :",Persoonsgegevens_vector)
        Persoonsgegevens_matrix.append(Persoonsgegevens_vector)
    if MetIndex:
        Header_lokaal.insert(0, "Index")
        for i, Row in enumerate(Persoonsgegevens_matrix):
            Row.insert(0, str(i))
    # print("Matrix:", Persoonsgegevens_matrix)
    return Persoonsgegevens_matrix, Header_lokaal

def Tabel_opmaak(Data_list_lokaal, Header_lokaal):
    print(tabulate(Data_list_lokaal, headers=Header_lokaal, tablefmt="fancy_grid", numalign="center"))

def Verwijder_rij_niv2(Data_lokaler, ID):
    Items = [key for key in Data_lokaler[0].keys()]
    ID_key = Items[0]
    # rprint("ID_key: ", ID_key)
    Gelukt = 0
    Persoonsgegevens_matrix = []
    for i, Row_Dict in enumerate(Data_lokaler):
        Gezochte_ID = int(Row_Dict[ID_key])
        # print("Row_Dict[ID_key]: ", Row_Dict[ID_key]," van type: ", type(Row_Dict[ID_key]), "Gezochte ID: ", ID, "van type: ", type(ID))
        if Gezochte_ID == ID:
            print("De persoon is verwijderd")
            Data_lokaler.pop(i)
            Gelukt = 1
    if Gelukt==0:
        print("De gekozen artiest is niet gevonden.")
    return Data_lokaler

# Data_lokaal.pop(Keus)

"""
*** definities van eerste niveau ***
"""

def Vraag_keuze():
    print(Fore.GREEN+"Maak keuze uit volgende lijst:")
    print(Fore.RESET+"1.	Voeg een muzikant toe")
    print("2.	Verwijder een muzikant")
    print("3.	Toon alle muzikanten in tabulate")
    print("4.	Toon alle muzikanten van genre(x) in tabulate")
    print("5.	Pas het instrument aan voor een muzikant")
    print("6.	Sorteer alle muzikanten op naam a-z")
    print("7.	Schrijf huidige data weg naar een nieuw csv bestand.")
    print(Fore.RED+"8.   Stop")
    print(Fore.RESET + " ")
    try:
        Keuze_lokaal = int(input("Mijn keuze is: "))
    except:
        print("Foutieve keuze. Alleen getallen kunnen worden ingevoerd.")
        Keuze_lokaal = None
    print("Uw keuze is:  ", Keuze_lokaal)
    return Keuze_lokaal

def LeesBestand(Doktersbestand_lokaal):
    try:
        input_file = csv.DictReader(open(Doktersbestand_lokaal)) # Lees direct als dict
        Doktersdata_lokaal = []
        for row in input_file:
            Doktersdata_lokaal.append(row)
        print("Databestand met succes gelezen.")
    except:
        print("Het lezen van het bestand is mislukt. Dit geeft een lege dataset waar niets mee aan te vangen valt.")
    return  Doktersdata_lokaal

def Toon_data(Data_lokaal, MetIndex):
    print("De muzikanten in het bestand zijn:")
    Tabel_list, Header = Tabel_uit_List_van_Dicts(Data_lokaal, MetIndex)
    print("Header:", Header)
    print("Tabel :", Tabel_list)
    Tabel_opmaak(Tabel_list, Header)
    input("Druk op Enter om verder te gaan ")

def Voeg_rij_toe(Data_lokaal):
    Items = [key for key in Data_lokaal[0].keys()]
    Items_zonder_ID = Items[1:]
    print(Items_zonder_ID)
    print("U gaat een rij toevoegen met volgende items :", Items_zonder_ID)
    Invoer = {}
    Invoer[Items[0]] = len(Data_lokaal)+1 # Dit is niet per sé een uniek getal als er een element verwijderd wordt: //
    # te verbeteren
    for item in Items_zonder_ID:
        Invoer[item] = input("Geef een waarde voor {}: ".format(item))
    print("Invoer :", Invoer )
    Data_lokaal.append(Invoer)
    input("Druk op Enter om verder te gaan ")
    return Data_lokaal

def Verwijder_rij(Data_lokaal):
    print("U wilt een muzikant verwijderen uit de lijst. ")
    print("De muzikanten in het bestand zijn:")
    Tabel_list, Header = Tabel_uit_List_van_Dicts(Data_lokaal, False) # De data heeft al een ingebouwde index
    Tabel_opmaak(Tabel_list, Header)
    try:
        Keus = int(input("Geef de index van de muzikant die u wilt verwijderen:"))
    except:
        print("Dit was geen nummer. Er gebeurt niets.")
    HoogsteIndex = int(Tabel_list[-1][0])
    # print("Hoogste index: ", HoogsteIndex)
    if Keus <= HoogsteIndex:
        Verwijder_rij_niv2(Data_lokaal, Keus)
    else:
        print("Keuze is groter dan ", HoogsteIndex, ".")
    input("Druk op Enter om verder te gaan ")
    return Data_lokaal

def Filter_muzikanten(Data_lokaal, Key):
    Selectie = []
    for Regel in Data_lokaal:
        Selectie.append(Regel[Key])
    print(Selectie)
    Gefilterd_Set = set(Selectie) # Verwijder dubbelen via 'set'-type
    print(Gefilterd_Set)
    GefilterdeElementen = []
    for i, val in enumerate(Gefilterd_Set):
        GefilterdeElementen.append([i, val])
    print(tabulate(GefilterdeElementen, headers = ["Index", "Elementen"]))
    try:
        Keuze = int(input("Geef de index van het element waarop u wilt filteren: "))
    except:
        print("De keuze is geen getal. De keuze wordt verlaten.")
        return
    Hoogste_index = GefilterdeElementen[-1][0]
    if Keuze < 0 or Keuze > Hoogste_index:
        print("De keuze is een onjuist getal. De keuze wordt verlaten.")
        return
    # Toon de lijnen
    ZoekElement = GefilterdeElementen[Keuze][1]
    print("U gaat filteren op: ",ZoekElement)
    Gefilterde_dict = []
    for Regel in Data_lokaal:
        if Regel[Key] == ZoekElement:
            Gefilterde_dict.append(Regel)
    # print(Gefilterde_dict)
    Persoonsgegevens_matrix, Header = Tabel_uit_List_van_Dicts(Gefilterde_dict, False)
    Tabel_opmaak(Persoonsgegevens_matrix, Header)
    input("Druk op Enter om verder te gaan ")

def Wijzig_muzikanten(Data_lokaal, Key):
    print("De muzikanten worden getoond waaruit u een keuze kunt maken: ")
    Persoonsgegevens_matrix, Header = Tabel_uit_List_van_Dicts(Data_lokaal, True)
    Tabel_opmaak(Persoonsgegevens_matrix, Header)
    try:
        Keuze = int(input(f"Geef de index van de doctor waarvan u veld {Key} wilt veranderen : " ))
    except:
        print("De keuze is geen getal. De keuze wordt verlaten.")
        return Data_lokaal
    Hoogste_index = len(Data_lokaal)-1
    if Keuze < 0 or Keuze > Hoogste_index:
        print("De keuze is een onjuist getal. De keuze wordt verlaten.")
        return Data_lokaal
    # Vraag nieuwe waarde en vervang die in de dict
    NieuweWaarde = input(f"Geef de nieuwe waarde voor veld {Key}: ")
    Data_lokaal[Keuze][Key] = NieuweWaarde
    print("Zie onder de aangepaste lijn: ")
    Persoonsgegevens_matrix, Header = Tabel_uit_List_van_Dicts(Data_lokaal, False)
    Datalijn = []
    Datalijn.append(Persoonsgegevens_matrix[Keuze])
    Tabel_opmaak(Datalijn, Header)
    input("Druk op Enter om verder te gaan ")
    return Data_lokaal

def Sorteer_Muzikanten(Data_lokaal, Veld, Richting):
    Data_lokaal.sort(key=lambda e: e[Veld], reverse=Richting)
    Persoonsgegevens_matrix, Header = Tabel_uit_List_van_Dicts(Data_lokaal, False)
    Tabel_opmaak(Persoonsgegevens_matrix, Header)
    input("Druk op Enter om verder te gaan ")

def Schrijf_bestand(Data_lokaal, Bestand_uit):
    eerste_item = Data_lokaal[0]
    Header_lokaal = [key for key in eerste_item.keys()]
    with open(Bestand_uit,"w+",newline="", encoding="utf-8") as csvfile:
        with csvfile:
            writer = csv.DictWriter(csvfile, fieldnames= Header_lokaal)
            writer.writeheader()
            writer.writerows(Data_lokaal)
        print("Succesvol geschreven")
    input("Druk op Enter om verder te gaan ")

"""
*** Hoofdgedeelte *** 
"""
# Lees eerst bestand
Muzikantendata_oorspronkelijk = LeesBestand(Invoerbestand)
print("Muzikantendata:", Muzikantendata_oorspronkelijk)
Muzikantendata = Muzikantendata_oorspronkelijk  # Bewaar oorspronkelijke data. Nuttig voor een reset.

# Gebruiker maakt een keuze
while ((Keuze != 8) and (Foute_keus < 4)):
    Keuze = Vraag_keuze()
    # print("Nogmaals, uw keuze blijkt : ", Keuze)
    if Keuze == 3:
        Foute_keus = 0
        Toon_data(Muzikantendata, False)
    elif Keuze == 1: # Voeg muzikant toe
        Foute_keus = 0
        Muzikantendata = Voeg_rij_toe(Muzikantendata)
        # print("Muzikantendata aangepast: ", Muzikantendata)
    elif Keuze == 2: # Verwijder een muzikant
        Foute_keus = 0
        Muzikantendata = Verwijder_rij(Muzikantendata)
        print("Muzikantendata aangepast: ", Muzikantendata)
    elif Keuze == 4:  # Filter muzikanten (Toon alle muzikanten van gender x in tabulate)
        Foute_keus = 0
        Filter_muzikanten(Muzikantendata, Key_om_op_te_zoeken) # Geef Key mee
    elif Keuze == 5:  # Pas een veld aan (Pas het instrument aan van de muzikant"
        Foute_keus = 0
        Muzikantendata = Wijzig_muzikanten(Muzikantendata, Key_te_wijzigen) # Geef Key mee
    elif Keuze == 6:  # Sorteer muzikanten op naam a-z"
        Foute_keus = 0
        Sorteer_Muzikanten(Muzikantendata, Key_naam, False) # (dict, Key, Reverse (True/False))
    elif Keuze == 7:  # Schrijf naar nieuw bestand"
        Foute_keus = 0
        Schrijf_bestand(Muzikantendata, Uitvoerbestand)
    else:
        print("Geen opdracht of vraag tot beëindiging")
        Foute_keus += 1
print("Programma beëindigd")