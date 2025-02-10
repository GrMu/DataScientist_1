import sqlite3
import pandas as pd

# Verbinding maken met SQLite database (bestand db)
conn = sqlite3.connect('personeel.db')

# Query om alle gegevens van personeel op te halen
query = "SELECT * FROM personeel"

# Voer de query uit en laad de resultaten in een Pandas DataFrame
alle_personeel = pd.read_sql(query, conn)

# Toon de resultaten
print(alle_personeel)

# Sluit de databaseverbinding
conn.close()