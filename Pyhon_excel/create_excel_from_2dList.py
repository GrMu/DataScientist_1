from openpyxl import Workbook

# De 2D-lijst
data = [["Naam", "Leeftijd", "Woonplaats"],
        ["Brent", 22, "Hasselt"],
        ["Marie", 26, "Genk"],
        ["Karel", 25, "Hasselt"],
        ["Fien", 24, "AS"]]

# Maak een nieuw Excel-werkboek
wb = Workbook()
ws = wb.active
# Voeg de data toe aan het werkblad
for row in data:
    ws.append(row)
# Sla het Excel-bestand op
wb.save("data.xlsx")
print("Excel-bestand opgeslagen als 'data.xlsx'")