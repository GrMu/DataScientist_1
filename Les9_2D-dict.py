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
Personeel = {1:{"Naam":"Bert", "Leeftijd":20, "Woonplaats":"Genk", "Functie":"Operator", "Afdeling":"Centraal"},
             2:{"Naam":"Bart", "Leeftijd":33, "Woonplaats":"Gent", "Functie":"Chef", "Afdeling":"Centraal"},
             3:{"Naam":"Berend", "Leeftijd": 26, "Woonplaats": "Bilzen", "Functie": "Technieker", "Afdeling": "Centraal"},
             4:{"Naam":"Bern", "Leeftijd":30, "Woonplaats":"Alken", "Functie":"Operator", "Afdeling":"Centraal"},
             5:{"Naam":"Berend", "Leeftijd":20, "Woonplaats":"Genk", "Functie":"Operator", "Afdeling":"Centraal"}
             }
print(Personeel)

# Maak een mooie tabel
def tabelopmaak(Personeel):
    Header = ["id"]
    Header=[key for key in Personeel[1].keys()]
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

voeg_rij_toe(Personeel)
tabelopmaak(Personeel)
