# Programma om doktersdata te lezen en te bewerken

# Variabelen
#Doktersbestand = "Data\Dokters.csv"
#Doktersbestand = "Data\Personeelsdata2.csv"
#Doktersbestand = "Data\ziekenhuizen_specialisten_30.csv"
Doktersbestand = "Data\ziekenhuizen_specialisten_kort.csv"

# Initialisatie
Doktersdata = [] # List met dictionaries
Tabel_list = []
Header = []

# Definities
import csv
def LeesBestand(Doktersbestand_lokaal):
    input_file = csv.DictReader(open(Doktersbestand_lokaal)) # Lees direct als dict
    Doktersdata_lokaal = []
    for row in input_file:
        Doktersdata_lokaal.append(row)
    return  Doktersdata_lokaal

def Tabel_uit_List_van_Dicts(Doktersdata_lokaal):
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
    print("Matrix:", Persoonsgegevens_matrix)
    return Persoonsgegevens_matrix, Header_lokaal

def Tabel_opmaak(Data_list_lokaal, Header_lokaal):
    from tabulate import tabulate
    print(tabulate(Data_list_lokaal, headers=Header_lokaal, tablefmt="fancy_grid"))

def Voeg_rij_toe(Doktersdata_lokaal):
    Items = [key for key in Doktersdata_lokaal[0].keys()]
    print("We gaan een rij toevoegen met volgende items :", Items)
    Invoer = {}
    for item in Items:
        Invoer[item] = input("Geef een waarde voor {}: ".format(item))
    print("Invoer :", Invoer )
    Doktersdata_lokaal.append(Invoer)
    return Doktersdata_lokaal

Doktersdata = LeesBestand(Doktersbestand)
print("Doktersdata:", Doktersdata)
#print("De dokters in het bestand zijn:")
#Tabel_list, Header = Tabel_uit_List_van_Dicts(Doktersdata)
#print("Header:", Header)
#print("Tabel :", Tabel_list)
#Tabel_opmaak(Tabel_list, Header)
Doktersdata_nieuw = Voeg_rij_toe(Doktersdata)
print("Doktersdata nieuw: ", Doktersdata_nieuw)
