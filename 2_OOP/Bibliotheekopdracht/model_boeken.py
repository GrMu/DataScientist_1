import os
import csv

# Definieer de Medewerker-klasse
class Boek:
    def __init__(self, id, titel, paginas, auteur):
        self.id = id
        self.titel = titel
        self.paginas = paginas
        self.auteur = auteur

    def __repr__(self):
        return (f"Boek(id={self.id}, titel= {self.titel}, aantal pagina's='{self.paginas}', "
                f"Auteur='{self.auteur}'")


# Pad instellen naar het CSV-bestand
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, "boeken_1.csv")

# Lees de CSV en maak een lijst van boek-objecten
Boeken_lijst = []

with open(csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter =";")
    # reader = csv.DictReader(file)
    for row in reader:
        Boek_ = Boek(
            id=int(row['id']),
            titel=row['titel'],
            paginas=int(row['paginas']),
            auteur=row['auteur']
        )
        Boeken_lijst.append(Boek_)

print(Boeken_lijst)

