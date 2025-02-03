import sqlite3
from colorama import Fore #nodig voor CRUD

def create_database():
    conn = sqlite3.connect("voetbal_club.db")
    cursor = conn.cursor()

    # Tabel aanmaken
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS spelers (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            voornaam TEXT NOT NULL,
            achternaam TEXT NOT NULL,
            gemeente TEXT NOT NULL,
            positie TEXT NOT NULL
        )
    ''')

    spelers_data = [("Jan", "Stevens", "Genk", "aanvaller"),
                    ("Piet", "Janssens", "As", "aanvaller"),
                    ("Miriam", "Claassen", "As", "spits" ),
                    ("Petra", "Claessens", "Zuttendaal", "spits")
                    ]

    cursor.executemany('''
        INSERT INTO spelers (voornaam, achternaam, gemeente, positie)
        VALUES (?, ?, ?, ?)
        ''', spelers_data)

    conn.commit()
    conn.close()
    print("Database succesvol gemaakt")

def fetch_spelers():
    conn = sqlite3.connect("voetbal_club.db")
    cursor = conn.cursor()
    # Selecteer alle spelers
    cursor.execute("SELECT * FROM spelers")
    spelers = cursor.fetchall()
    conn.close()
    return spelers

def fetch_aanvallers(): #inclusief oplopende ordening
    conn = sqlite3.connect("voetbal_club.db")
    cursor = conn.cursor()
    # Selecteer alleen spelers met positie 'Aanvaller' en sorteer op gemeente A-Z
    cursor.execute(
        "SELECT * FROM spelers WHERE positie = 'aanvaller'"
        " ORDER BY gemeente ASC")
    aanvallers = cursor.fetchall()
    conn.close()
    return aanvallers

def Vraag_keuze():
    print("Database-acties:")
    print(Fore.GREEN+"Maak keuze uit volgende lijst:")
    print(Fore.RESET+"1.	Creëer database")
    print("2.	Toon alle spelers")
    print("3.	Toon aanvallers")
    print("4.	Nog meer")
    print(Fore.RED+"5. Stop")
    print(Fore.RESET + " ")
    try:
        Keuze_lokaal = int(input("Mijn keuze is: "))
    except:
        print("Foutieve keuze. Alleen getallen kunnen worden ingevoerd.")
        Keuze_lokaal = None
    print("Uw keuze is:  ", Keuze_lokaal)
    return Keuze_lokaal

def main():
    # Initialisatie
    Foute_keus = 0
    Keuze = None
    while ((Keuze != 5) and (Foute_keus < 4)):
        Keuze = Vraag_keuze()
        if Keuze == 1:
            create_database()
        elif Keuze == 2:
            print("Keuze 2 gaat uitgevoerd worden.")
            spelers = fetch_spelers()
            if spelers == []:
                print("Geen spelers gevonden.")
            else:
                for speler in spelers:
                    print(
                        f"ID: {speler[0]}, Voornaam: {speler[1]}, Achternaam: {speler[2]}, Gemeente: {speler[3]}, Positie: {speler[4]}")
        elif Keuze == 3:
            # print("Keuze 3 gaat uitgevoerd worden.")
            aanvallers = fetch_aanvallers()
            if aanvallers == []:
                print("Geen aanvallers gevonden.")
            else:
                for aanvaller in aanvallers:
                    print(
                        f"ID: {aanvaller[0]}, Voornaam: {aanvaller[1]}, Achternaam: {aanvaller[2]}, Gemeente: {aanvaller[3]}, Positie: {aanvaller[4]}")
        elif Keuze == 4:
            pass
        else:
            print("Geen opdracht of vraag tot beëindiging")
            Foute_keus += 1
    print("Programma beëindigd")

if __name__ == "__main__":
    main()
