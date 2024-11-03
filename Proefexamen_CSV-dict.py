# Programma om doktersdata te lezen en te bewerken

# Variabelen
#Doktersbestand = "Data\Dokters.csv"
#Doktersbestand = "Data\Personeelsdata2.csv"
#Doktersbestand = "Data\ziekenhuizen_specialisten_30.csv"
Doktersbestand = "Data\ziekenhuizen_specialisten_kort.csv"

# Import
from tabulate import tabulate

# Initialisatie
Doktersdata = [] # List met dictionaries
Tabel_list = []
Header = []
Keuze = None
Foute_keus = 0

# Definities van lager niveau
def Vraag_keuze():
    print("Maak keuze uit volgende lijst:")
    print("1.	Voeg een dokter toe")
    print("2.	Verwijder een dokter")
    print("3.	Toon alle dokters in tabulate")
    print("4.	Toon alle dokters van ziekenhuis x in tabulate")
    print("5.	Pas een veld aan voor een dokter")
    # print("5.	Pas het ziekenhuis aan van de dokter")
    # print("6.	Wijzig de woonplaats van een dokter")
    # print("7.	Wijzig het ereloon van een dokter")
    print("8.	Sorteer alle dokters op naam a-z")
    print("9.	Sorteer alle dokters op ereloon(hoog-naar-laag)")
    print("10.	Schrijf huidige dictioniary weg naar een nieuw csv bestand.")
    print("11.  Maak alle wijzigingen ongedaan")
    print("12.  Stop")
    try:
        Keuze_lokaal = int(input("Mijn keuze is: "))
    except:
        print("Foutieve keuze. Alleen getallen kunnen worden ingevoerd.")
        Keuze_lokaal = None
    print("Uw keuze is: ", Keuze_lokaal)
    return Keuze_lokaal

import csv
def LeesBestand(Doktersbestand_lokaal):
    import csv
    input_file = csv.DictReader(open(Doktersbestand_lokaal)) # Lees direct als dict
    Doktersdata_lokaal = []
    for row in input_file:
        Doktersdata_lokaal.append(row)
    return  Doktersdata_lokaal

def Tabel_uit_List_van_Dicts(Doktersdata_lokaal, MetIndex):
    eerste_item = Doktersdata_lokaal[0]
    Header_lokaal = [key for key in eerste_item.keys()]
    # print("Header is: ", Header)
    Persoonsgegevens_matrix = []
    for Row_Dict in Doktersdata_lokaal:
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
    print(tabulate(Data_list_lokaal, headers=Header_lokaal, tablefmt="fancy_grid"))

# Definities van eerste niveau
def Voeg_rij_toe(Doktersdata_lokaal):
    Items = [key for key in Doktersdata_lokaal[0].keys()]
    print("We gaan een rij toevoegen met volgende items :", Items)
    Invoer = {}
    for item in Items:
        Invoer[item] = input("Geef een waarde voor {}: ".format(item))
    print("Invoer :", Invoer )
    Doktersdata_lokaal.append(Invoer)
    return Doktersdata_lokaal

def Verwijder_rij(Doktersdata_lokaal):
    print("U wilt een dokter verwijderen uit de lijst. ")
    print("De dokters in het bestand zijn:")
    Tabel_list, Header = Tabel_uit_List_van_Dicts(Doktersdata_lokaal, True) # Toon tabel met index per rij.
    Tabel_opmaak(Tabel_list, Header)
    try:
        Keus = int(input("Geef de index van de dokter die u wilt verwijderen:"))
    except:
        print("Dit was geen nummer. Er gebeurt niets.")
    HoogsteIndex = int(Tabel_list[-1][0])
    print("Hoogste index: ", HoogsteIndex)
    if Keus <= HoogsteIndex:
        Doktersdata_lokaal.pop(Keus)
    else:
        print("Keuze is groter dan ", HoogsteIndex, ".")
    return Doktersdata_lokaal

def Filter_dokters(Doktersdata_lokaal):
    # Toon eerst de invoervelden, waaruit een keus moet worden gemaakt
    eerste_item = Doktersdata_lokaal[0]
    Header_lokaal = [key for key in eerste_item.keys()]
    Tabel = []
    for i, key in enumerate(Header_lokaal):
        Tabel.append([i, key])
    print("Er zijn de volgende invoervelden: ")
    print(tabulate(Tabel, headers= ["Index", "Invoerveld"]))
    try:
        Keuze = int(input("Geef de index waarop u wilt filteren: "))
    except:
        print("De keuze is geen getal. De keuze wordt verlaten.")
        return
    Hoogste_index = Tabel[-1][0]
    if Keuze <0 or Keuze > Hoogste_index:
        print("De keuze is een onjuist getal. De keuze wordt verlaten.")
        return
    # Toon de elementen in het gekozen invoerveld en vraag keuze
    Key = Header_lokaal[Keuze]
    Selectie = []
    for Regel in Doktersdata:
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
    for Regel in Doktersdata:
        if Regel[Key] == ZoekElement:
            Gefilterde_dict.append(Regel)
    # print(Gefilterde_dict)
    Persoonsgegevens_matrix, Header = Tabel_uit_List_van_Dicts(Gefilterde_dict, False)
    Tabel_opmaak(Persoonsgegevens_matrix, Header)
    input("Druk op Enter om verder te gaan ")

def Wijzig_dokters(Doktersdata_lokaal):
    # Toon eerst de invoervelden, waaruit een keus moet worden gemaakt
    eerste_item = Doktersdata_lokaal[0]
    Header_lokaal = [key for key in eerste_item.keys()]
    Tabel = []
    for i, key in enumerate(Header_lokaal):
        Tabel.append([i, key])
    print("Er zijn de volgende invoervelden: ")
    print(tabulate(Tabel, headers= ["Index", "Invoerveld"]))
    try:
        Keuze = int(input("Geef de index van het veld waarvan u de waarde wilt veranderen : "))
    except:
        print("De keuze is geen getal. De keuze wordt verlaten.")
        return Doktersdata_lokaal
    Hoogste_index = Tabel[-1][0]
    if Keuze <0 or Keuze > Hoogste_index:
        print("De keuze is een onjuist getal. De keuze wordt verlaten.")
        return
    Key = Header_lokaal[Keuze]
    # Toon de doktoren en vraag keuze
    print("De doktoren worden getoond waaruit u een keuze kunt maken: ")
    Persoonsgegevens_matrix, Header = Tabel_uit_List_van_Dicts(Doktersdata_lokaal, True)
    Tabel_opmaak(Persoonsgegevens_matrix, Header)
    try:
        Keuze = int(input(f"Geef de index van de doctor waarvan u veld {Key} wilt veranderen : " ))
    except:
        print("De keuze is geen getal. De keuze wordt verlaten.")
        return Doktersdata_lokaal
    Hoogste_index = len(Doktersdata_lokaal)-1
    if Keuze < 0 or Keuze > Hoogste_index:
        print("De keuze is een onjuist getal. De keuze wordt verlaten.")
        return Doktersdata_lokaal
    # Vraag nieuwe waarde en vervang die in de dict
    NieuweWaarde = input(f"Geef de nieuwe waarde voor veld {Key}: ")
    Doktersdata_lokaal[Keuze][Key] = NieuweWaarde
    print("Zie onder de aangepaste lijn: ")
    Persoonsgegevens_matrix, Header = Tabel_uit_List_van_Dicts(Doktersdata_lokaal, False)
    Dokterslijn = []
    Dokterslijn.append(Persoonsgegevens_matrix[Keuze])
    Tabel_opmaak(Dokterslijn, Header)
    input("Druk op Enter om verder te gaan ")

def Sorteer_dokters(Doktersdata_lokaal, Veld, Richting):
    # def myFunc(e):
    #    return e[Veld]
    # Doktersdata_lokaal.sort(key=myFunc, reverse= Richting)
    Doktersdata_lokaal.sort(key=lambda e: e[Veld], reverse=Richting)
    Persoonsgegevens_matrix, Header = Tabel_uit_List_van_Dicts(Doktersdata_lokaal, False)
    Tabel_opmaak(Persoonsgegevens_matrix, Header)
    input("Druk op Enter om verder te gaan ")

def Schrijf_bestand(Doktersdata_lokaal):
    Doktersbestand_uit = "Data\ziekenhuizen_specialisten_uit.csv"
    eerste_item = Doktersdata_lokaal[0]
    Header_lokaal = [key for key in eerste_item.keys()]
    with open(Doktersbestand_uit,"w+",newline="", encoding="utf-8") as csvfile:
        with csvfile:
            writer = csv.DictWriter(csvfile, fieldnames= Header_lokaal)
            writer.writeheader()
            writer.writerows(Doktersdata_lokaal)
        print("Succesvol geschreven")

# Lees eerst bestand
Doktersdata_oorspronkelijk = LeesBestand(Doktersbestand)
print("Doktersdata:", Doktersdata_oorspronkelijk)
Doktersdata = Doktersdata_oorspronkelijk # Bewaar oorspronkelijke data. Nuttig voor een reset.

# Gebruiker maakt een keuze
while ((Keuze != 12) and (Foute_keus < 4)):
    Keuze = Vraag_keuze()
    print("Nogmaals, uw keuze blijkt : ", Keuze)
    if Keuze == 3:
        Foute_keus = 0
        print("De dokters in het bestand zijn:")
        Tabel_list, Header = Tabel_uit_List_van_Dicts(Doktersdata, True)
        # print("Header:", Header)
        # print("Tabel :", Tabel_list)
        Tabel_opmaak(Tabel_list, Header)
        input("Druk op Enter om verder te gaan ")
    elif Keuze  == 11: # Maak alle wijzigingen ongedaan
        Foute_keus = 0
        Doktersdata = Doktersdata_oorspronkelijk
        print("Doktersdata (hersteld): ", Doktersdata)
    elif Keuze == 1: # Voeg dokter toe
        Foute_keus = 0
        Doktersdata = Voeg_rij_toe(Doktersdata)
        print("Doktersdata aangepast: ", Doktersdata)
    elif Keuze == 2: # Verwijder een dokter
        Foute_keus = 0
        Doktersdata = Verwijder_rij(Doktersdata)
        print("Doktersdata aangepast: ", Doktersdata)
    elif Keuze == 4:  # Filter dokters (Toon alle dokters van ziekenhuis x in tabulate)
        Foute_keus = 0
        Filter_dokters(Doktersdata)
    elif Keuze == 5:  # Pas een veld aan (Pas het ziekenhuis aan van de dokter", //
    # Wijzig de woonplaats van een dokter", Wijzig het ereloon van een dokter"))
        Foute_keus = 0
        Doktersdata = Wijzig_dokters(Doktersdata)
    elif Keuze == 8:  # Sorteer dokters op naam"
        Foute_keus = 0
        Sorteer_dokters(Doktersdata, "achternaam", False) # (dict, Key, Reverse (True/False))
    elif Keuze == 9:  # Sorteer dokters op ereloon"
        Foute_keus = 0
        Sorteer_dokters(Doktersdata, "ereloon", True)  # (dict, Key, Reverse (True/False))
    elif Keuze == 10:  # Schrijf naar nieuw bestand"
        Foute_keus = 0
        Schrijf_bestand(Doktersdata)
    else:
        print("Geen opdracht of vraag tot beëindiging")
        Foute_keus += 1
print("Programma beëindigd")