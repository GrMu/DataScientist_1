# Oefening 2D dict
"""
Maak een 2d lijst personeel met 5  rijen aan data.
Naam, Leeftijd, Woonplaats, Functie, Afdeling
Toon deze data in een tabulate tabel
Zorg ervoor dat een rij toegevoegd kan worden
Zorg ervoor dat een rij verwijderd kan worden
Maak een functie sorteren op naam en sorteren op leeftijd
"""
from tabulate import tabulate
Personeel = {7:{"Naam":"Bert", "Leeftijd":20, "Woonplaats":"Genk", "Functie":"Operator", "Afdeling":"Centraal"},
             2:{"Naam":"Bart", "Leeftijd":33, "Woonplaats":"Gent", "Functie":"Chef", "Afdeling":"Centraal"},
             3:{"Naam":"Berend", "Leeftijd": 26, "Woonplaats": "Bilzen", "Functie": "Technieker", "Afdeling": "Centraal"},
             10:{"Naam":"Bern", "Leeftijd":30, "Woonplaats":"Alken", "Functie":"Operator", "Afdeling":"Centraal"},
             5:{"Naam":"Berend", "Leeftijd":20, "Woonplaats":"Genk", "Functie":"Operator", "Afdeling":"Centraal"}
             }
print(Personeel)

# Maak een mooie tabel
def tabelopmaak(Personeel):
    # Vind eerste item: dit is niet perse '1'
    for eerste_item in Personeel:
        print("Eerste item:", eerste_item, "van type:", type(eerste_item))
        break
    Header = ["id"]
    Header=[key for key in Personeel[eerste_item].keys()]
    Header.insert(0,"id")
    # print(Header)
    Persoonsgegevens_matrix = []
    for id,values in Personeel.items():
        Persoonsgegevens_vector = []
        Persoonsgegevens_vector.append(id)
        for item,waardes in values.items():
            Persoonsgegevens_vector.append(waardes)
        # print(Persoonsgegevens_vector)
        Persoonsgegevens_matrix.append(Persoonsgegevens_vector)
    print(tabulate(Persoonsgegevens_matrix, headers=Header, tablefmt="fancy_grid"))

    """
    # Deze constructie werkt niet:
    for Persoon in Personeel:
        print(type(Persoon))
        Persoonsgegevens_vector.append(Persoon)
        for value in Persoon.values():
            Persoonsgegevens_vector.append(value)
        print(Persoonsgegevens_vector)
    """

# Voeg een rij toe
def voeg_rij_toe(Personeel):
    IDs = [id for id in Personeel]
    IDs.sort()
    nieuwe_ID = IDs[-1]+1
    Personeel.update({nieuwe_ID:{"Naam":"Barend", "Leeftijd":18, "Woonplaats":"Stokkem", "Functie":"Operator", "Afdeling":"Decentraal"}})
    # print(Personeel)

# Verwijder een rij toe
def verwijder_rij(Personeel, rij_id):
    for id,values in Personeel.items():
        if id ==rij_id:
            Personeel.pop(rij_id)
            break

# Sorteren op een key zoals naam en leeftijd
def sorteer_2D_dict(Personeel, Key):
    print(Personeel[0][Key])
    # print(Personeel)

# Sorteren op een key zoals naam en leeftijd
def sorteer_2D_dict(Personeel, Key):
    gesorteerde_dict = dict(sorted(Personeel.items(), key=lambda item: item[1][Key]))
    # print(gesorteerde_dict)
    return gesorteerde_dict

def sorteer_2D_dict_op_index(Personeel):
    gesorteerde_dict = dict(sorted(Personeel.items(), key=lambda item: item[0])) ##dict wordt omgezet naar list. Eerste lijn nodig.
    print(gesorteerde_dict)
    return gesorteerde_dict

voeg_rij_toe(Personeel)
tabelopmaak(Personeel)
verwijder_rij(Personeel,3)
tabelopmaak(Personeel)
gesorteerde_dict2=sorteer_2D_dict(Personeel, "Naam")
tabelopmaak(gesorteerde_dict2)
print(gesorteerde_dict2)
gesorteerde_dict3=sorteer_2D_dict(gesorteerde_dict2, "Leeftijd")
tabelopmaak(gesorteerde_dict3)
gesorteerde_dict4=sorteer_2D_dict_op_index(gesorteerde_dict3)
tabelopmaak(gesorteerde_dict4)
