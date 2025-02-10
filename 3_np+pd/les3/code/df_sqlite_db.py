import pandas as pd
import sqlite3

# Dummy data
data = {
    "id": range(1, 13),
    "naam": ["Jan", "Sara", "Ali", "Emma", "Tom", "Lisa", "Mark", "Eva", "Noah", "Sophie", "Lars", "Mila"],
    "functie": ["Manager", "HR Medewerker", "IT Support", "Marketing Specialist", "Developer", "HR Manager", "Accountant", "Verkoper", "Engineer", "Designer", "Logistiek", "CEO"],
    "afdeling": ["Management", "HR", "IT", "Marketing", "IT", "HR", "Finance", "Sales", "Engineering", "Design", "Logistiek", "Management"],
    "loon": [5000, 3200, 3500, 3700, 4000, 4500, 3800, 3400, 4200, 3600, 3300, 8000]
}

# DataFrame maken
personeel = pd.DataFrame(data)

# Verbinding maken met SQLite database (bestand db)
conn = sqlite3.connect('personeel.db')

# Zet de DataFrame om naar een SQLite-tabel
personeel.to_sql('personeel', conn, if_exists='replace', index=False)

# Functie om te filteren op afdeling
def filter_op_afdeling_sql(conn, afdeling):
    query = f"SELECT * FROM personeel WHERE afdeling = '{afdeling}'"
    return pd.read_sql(query, conn)

# Functie om het aantal medewerkers in een bepaalde afdeling te tellen
def aantal_in_afdeling_sql(conn, afdeling):
    query = f"SELECT COUNT(*) FROM personeel WHERE afdeling = '{afdeling}'"
    result = pd.read_sql(query, conn)
    return result.iloc[0, 0]

# Voorbeeld: filteren op HR
hr_personeel_sql = filter_op_afdeling_sql(conn, "HR")
print(hr_personeel_sql)

# Totale loon voor afdeling HR
totaal_loon_hr_sql = hr_personeel_sql["loon"].sum()
print(f"Totale loon voor afdeling HR: {totaal_loon_hr_sql}")

# Aantal medewerkers in IT
aantal_it_sql = aantal_in_afdeling_sql(conn, "IT")
print(f"Aantal medewerkers in IT: {aantal_it_sql}")

# Sluit de databaseverbinding
conn.close()
