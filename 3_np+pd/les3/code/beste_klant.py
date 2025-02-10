import numpy as np

# Producten en voorraad
producten = np.array(["Water", "Frisdrank", "Bier", "Wijn"])
voorraad = np.array([40, 20, 50, 20])

# Prijzen aangeboden door 3 klanten (rijen: klanten, kolommen: producten)
klanten_prijzen = np.array([
    [1.0, 1.5, 2.0, 5.0],  # Klant 1
    [1.2, 1.4, 2.1, 4.8],  # Klant 2
    [1.1, 1.6, 2.05, 4.9]  # Klant 3
])

# Bereken de totale opbrengst per klant
totale_opbrengsten = klanten_prijzen @ voorraad

# Bepaal de beste klant
beste_klant_index = np.argmax(totale_opbrengsten)

# Resultaten
print("Totale opbrengsten per klant:", totale_opbrengsten)
print(f"De beste klant is klant {beste_klant_index + 1} met een opbrengst van €{totale_opbrengsten[beste_klant_index]:.2f}")
