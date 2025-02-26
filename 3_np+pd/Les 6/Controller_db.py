from connect_to_db import *

db = DBConnector("personeel1")

def toon_alle_medewerkers():
    """Toont alle medewerkers in de tabel."""
    sql = "SELECT * FROM medewerkers"
    db.voer_query_uit(sql)

def toon_wagens():
    sql = "select * from autos"
    db.voer_query_uit(sql)

def toon_alle_medewerkers_van_afdeling():
    """Toont medewerkers van een specifieke afdeling."""
    # Eerst alle unieke afdelingen ophalen
    sql = "SELECT DISTINCT afdeling FROM medewerkers"
    db.voer_query_uit(sql)

    afdeling = input("Geef de afdeling: ")
    sql = f"SELECT * FROM medewerkers WHERE afdeling = '{afdeling}'"
    db.voer_query_uit(sql)

def voeg_medewerker_toe():
    """Voegt een nieuwe medewerker toe aan de database."""
    voornaam = input("Voornaam: ")
    achternaam = input("Achternaam: ")
    functie = input("Functie: ")
    startjaar = input("Startjaar: ")
    geslacht = input("Geslacht: ")
    maandloon = input("Maandloon: ")
    afdeling = input("Afdeling: ")
    bedrijfswagen = input("Heeft de medewerker een bedrijfswagen? (ja/nee): ")

    sql = f"""
    INSERT INTO medewerkers (voornaam, achternaam, functie, startjaar, geslacht, maandloon, afdeling, bedrijfswagen)
    VALUES ('{voornaam}', '{achternaam}', '{functie}', {startjaar}, '{geslacht}', {maandloon}, '{afdeling}', '{bedrijfswagen}')
    """
    db.cursor.execute(sql)
    db.mydb.commit()
    print("Medewerker toegevoegd!")

def verwijder_medewerker():
    """Verwijdert een medewerker op basis van ID."""
    toon_alle_medewerkers()
    medewerker_id = input("Geef het ID van de medewerker die je wilt verwijderen: ")

    sql = f"DELETE FROM medewerkers WHERE id = {medewerker_id}"
    db.cursor.execute(sql)
    db.mydb.commit()
    print("Medewerker verwijderd!")

def pas_maandloon_aan():
    """Past het maandloon van een specifieke medewerker aan."""
    toon_alle_medewerkers()
    medewerker_id = input("Geef het ID van de medewerker: ")
    nieuw_loon = input("Geef het nieuwe maandloon: ")

    sql = f"UPDATE medewerkers SET maandloon = {nieuw_loon} WHERE id = {medewerker_id}"
    db.cursor.execute(sql)
    db.mydb.commit()
    print("Maandloon aangepast!")

def toon_functies():
    print("\n1. Toon alle medewerkers")
    print("2. Toon medewerkers van een afdeling")
    print("3. Voeg een medewerker toe")
    print("4. Verwijder een medewerker")
    print("5. Pas maandloon aan")
    print("6. Stoppen")

if __name__ == "__main__":
    # Menu
    while True:
        print("\n1. Toon alle medewerkers")
        print("2. Toon medewerkers van een afdeling")
        print("3. Voeg een medewerker toe")
        print("4. Verwijder een medewerker")
        print("5. Pas maandloon aan")
        print("6. Toon de wagens")
        print("7. Stoppen")

        keuze = input("Maak een keuze: ")
        if keuze == "1":
            toon_alle_medewerkers()
        elif keuze == "2":
            toon_alle_medewerkers_van_afdeling()
        elif keuze == "3":
            voeg_medewerker_toe()
        elif keuze == "4":
            verwijder_medewerker()
        elif keuze == "5":
            pas_maandloon_aan()
        elif keuze == "6":
            toon_wagens()
        elif keuze == "7":
            db.sluit_verbinding()
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")
