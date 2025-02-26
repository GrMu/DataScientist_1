from connect_to_db import *
import pandas as pd
import matplotlib.pyplot as plt

db = DBConnector("personeel1")
kolom_namen = db.geef_kolomnamen("medewerkers")
data = db.return_query_data("select * from medewerkers")
df = pd.DataFrame(data)
df.columns = kolom_namen

# Zet de waarden in de kolom "afdeling" om naar hoofdletters
df["afdeling"] = df["afdeling"].str.upper()

gemiddeld_loon_per_afdeling = df.groupby("afdeling")["maandloon"].mean().round(2)

# Print het resultaat
print(gemiddeld_loon_per_afdeling)

plt.figure(figsize=(8, 8))  # Optionele grootte-instelling
plt.pie(
    gemiddeld_loon_per_afdeling.values,
    labels=gemiddeld_loon_per_afdeling.index,
    autopct="%1.2f%%",
    startangle=140,
    colors=plt.cm.Paired.colors,
)

plt.title("Gemiddeld Maandloon per Afdeling")  # Titel toevoegen
plt.show()  # Toon de grafiek
