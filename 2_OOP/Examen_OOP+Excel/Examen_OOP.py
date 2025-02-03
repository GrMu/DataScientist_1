# Examen OOP door Grietus Mulder
from colorama import Fore #nodig voor CRUD
from tabulate import tabulate
import csv

class Verhuurauto:
    aantal_wagens = 0

    def __init__(self, id, merk, model, bouwjaar, brandstof, huurprijs):
        self.id = id
        self.merk = merk
        self.model = model
        self.bouwjaar = bouwjaar
        self.brandstof = brandstof
        self.huurprijs = huurprijs
        Verhuurauto.aantal_wagens += 1

    def __str__(self):
        return (f"Verhuurauto heeft id {self.id}, merk {self.merk} en model {self.model}"
                f" het bouwjaar is {self.bouwjaar} en de brandstof is {self.brandstof}"
                f" De huurprijs is {self.huurprijs}")

    def hoeveel_wagens(self):
        return f"het aantal auto's zijn {auto.aantal_wagens}"


"""
Functies buiten de klasse
"""
def file_exists(BestandRel_lokaal):
    try:
        with open(BestandRel_lokaal, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
        return True
    except FileNotFoundError:
        print("Fout", "Het opgegeven bestand bestaat niet.")
        return False
    except Exception as e:
        print("Fout", f"Fout bij het lezen van het bestand: {e}")
        return False

def MaakEenAutoAan(): # Om CRUD te testen
    # Tijdelijk model om te starten
    id = 1
    merk = "Ford"
    model = "Capri"
    bouwjaar = 2002
    brandstof = 'Benzine'
    huurprijs = 45
    Verhuurauto_obj = Verhuurauto(id,merk, model, bouwjaar, brandstof, huurprijs)
    print(Verhuurauto_obj)
    return Verhuurauto_obj

def LeesCSV_as_list(BestandRel):
    Verhuurauto_lijst_as_list_lokaal = []
    # Auto_as_list = list(Auto_obj)
    """Leest het CSV-bestand in en retourneert de inhoud als een lijst van rijen."""
    try:
        with open(BestandRel, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            Verhuurauto_lijst_as_list_lokaal = list(reader)
        return Verhuurauto_lijst_as_list_lokaal
    except FileNotFoundError:
        print("Fout: Het opgegeven bestand bestaat niet.")
        return []
    except Exception as e:
        print(f"Fout bij het lezen van het bestand: {e}")
        return []

def List_to_objects(Verhuurauto_lijst_as_list):
    Verhuurauto_lijst_lokaal = []
    for row in Verhuurauto_lijst_as_list:
        Verhuurauto_obj = Verhuurauto(row[0], row[1], row[2], row[3], row[4], row[5]) #(id, merk, model, bouwjaar, brandstof, huurprijs)
        Verhuurauto_lijst_as_list.append(Verhuurauto_obj)
        for row in Verhuurauto_lijst_as_list:
            print("De verhuurautos in de objectenlijst zijn:", row)
    return Verhuurauto_lijst_lokaal


def LeesVerhuurautosCSV(BestandRel): # Lees bestand en geef terug als list van Verhuurauto-klasse
    Verhuurauto_lijst_lokaal = []
    Verhuurauto_lijst_as_list = []
    Verhuurauto_obj = MaakEenAutoAan()  # Tijdelijk model om te starten
    Verhuurauto_lijst_lokaal.append(Verhuurauto_obj)
    Verhuurauto_lijst_as_list =  LeesCSV_as_list(BestandRel)
    print("Verhuurautolijst in CSV: ",Verhuurauto_lijst_as_list)
    Verhuurauto_lijst_lokaal = List_to_objects(Verhuurauto_lijst_as_list)
    return Verhuurauto_lijst_lokaal

def Toon_data(Verhuurauto_lijst_lokaal):
    # Uit excel_examen halen
    pass

def voeg_rij_toe(Verhuurauto_lijst_lokaal):
    NieuweRij=Verhuurauto_lijst_lokaal[0] # Tijdelijk
    return Verhuurauto_lijst_lokaal, NieuweRij

def Verwijder_rij(Verhuurauto_lijst_lokaal):
    VerwijderdeRij = None
    return Verhuurauto_lijst_lokaal, VerwijderdeRij

def Toon_wagens_met_brandstof(Verhuurauto_lijst_lokaal):  # Geeft succes retour
    pass

def Schrijf_weg(Verhuurauto_lijst_lokaal):
    pass

def Vraag_keuze():
    print("Verhuurauto Manager:")
    print(Fore.GREEN+"Maak keuze uit volgende lijst:")
    print(Fore.RESET+"1.	Toon alle wagens")
    print("2.	Voeg een wagen toe")
    print("3.	Verwijder een wagen op ID")
    print("4.	Toon wagens met brandstof (via vraag)")
    print("5.	Schrijf aangepaste data weg")
    print(Fore.RED+"6.   Stop")
    print(Fore.RESET + " ")
    try:
        Keuze_lokaal = int(input("Mijn keuze is: "))
    except:
        print("Foutieve keuze. Alleen getallen kunnen worden ingevoerd.")
        Keuze_lokaal = None
    print("Uw keuze is:  ", Keuze_lokaal)
    return Keuze_lokaal



"""
*** Hoofdgedeelte *** 
"""
# Initialisatie
Foute_keus = 0
Keuze = None
Verhuurauto_lijst = []

# Programma
if __name__ == "__main__":
    # Open bestand (de Excelklasse werkt alleen als het bestand bestaat)
    BestandRel = r"autoverhuur_data.csv"
    if file_exists(BestandRel) == True:
        Verhuurauto_lijst = LeesVerhuurautosCSV(BestandRel)  # Lees bestand en geef terug als list van Verhuurauto-klasse
        print(Verhuurauto_lijst)
        # Gebruiker maakt een keuze
        while ((Keuze != 6) and (Foute_keus < 4)):
            Keuze = Vraag_keuze()
            if Keuze == 1:
                Foute_keus = 0
                Toon_data(Verhuurauto_lijst)
                toets = input("Keuze 1 is afgelopen. Druk op Enter")
            elif Keuze == 2: # Voeg wagen toe
                Foute_keus = 0
                Verhuurauto_lijst, NieuweRij = voeg_rij_toe(Verhuurauto_lijst)
                print("Verhuurautolijst aangepast met : ", NieuweRij)
                toets = input("Keuze 2 is afgelopen. Druk op Enter")
            elif Keuze == 3: # Verwijder een auto op ID
                Foute_keus = 0
                Verhuurauto_lijst, VerwijderdeRij = Verwijder_rij(Verhuurauto_lijst)
                print("Verhuurautolijst aangepast door te verwijderen: ", VerwijderdeRij)
            elif Keuze == 4:  # Toon wagens met brandstof (op vraag)
                Foute_keus = 0
                Toon_wagens_met_brandstof(Verhuurauto_lijst) # Geeft succes retour
                toets = input("Keuze 4 is afgelopen. Druk op Enter")
            elif Keuze == 5:  # Schrijf aangepaste data weg"
                Foute_keus = 0
                Schrijf_weg(Verhuurauto_lijst)
            else:
                print("Geen opdracht of vraag tot beëindiging")
                Foute_keus += 1
        else: print(f"Bestand {BestandRel} niet gevonden." )
        print("Programma beëindigd")
