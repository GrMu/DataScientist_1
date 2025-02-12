
import mysql.connector
from faker import Faker
import random

# Maak verbinding met de MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

# Maak een cursor object
cursor = conn.cursor()

# Maak de database
cursor.execute("CREATE DATABASE IF NOT EXISTS personeel")
cursor.execute("USE personeel")

# Maak de tabel
cursor.execute("""
CREATE TABLE IF NOT EXISTS medewerkers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    voornaam VARCHAR(50),
    achternaam VARCHAR(50),
    leeftijd INT,
    gemeente VARCHAR(50),
    afdeling VARCHAR(50),
    maandloon DECIMAL(10, 2)
)
""")

# Initialiseer de Faker bibliotheek
fake = Faker('nl_BE')

# Lijst van afdelingen met IT als grootste
departments = ['IT', 'HR', 'Finance', 'Marketing', 'Sales']
department_weights = [0.5, 0.1, 0.1, 0.1, 0.2]

# Lijst van gemeenten binnen een straal van 40km rond Genk
municipalities = [
    'Genk', 'Hasselt', 'Maasmechelen', 'Bilzen', 'Diepenbeek',
    'Zutendaal', 'Lanaken', 'As', 'Opglabbeek', 'Houthalen-Helchteren'
]

# Voeg 40 rijen data toe aan de tabel
for _ in range(40):
    voornaam = fake.first_name()
    achternaam = fake.last_name()
    leeftijd = random.randint(20, 65)
    gemeente = random.choice(municipalities)
    afdeling = random.choices(departments, weights=department_weights, k=1)[0]
    maandloon = round(random.uniform(2000, 6000), 2)

    cursor.execute("""
    INSERT INTO medewerkers (voornaam, achternaam, leeftijd, gemeente, afdeling, maandloon)
    VALUES (%s, %s, %s, %s, %s, %s)
    """, (voornaam, achternaam, leeftijd, gemeente, afdeling, maandloon))

# Commit de transactie
conn.commit()

cursor.execute("SELECT * FROM personeel.medewerkers")
myresult = cursor.fetchall()
for x in myresult:
    print(*x)

# Sluit de cursor en verbinding
cursor.close()
conn.close()

print("Database en tabel succesvol aangemaakt met 40 rijen data.")


