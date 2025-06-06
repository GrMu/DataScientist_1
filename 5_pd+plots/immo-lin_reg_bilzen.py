import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# from scikit-learn.linear_model import LinearRegression
from Immo_Cleaning_1 import *

# Filter Bilzen-data
df_bilzen = df_filtered[df_filtered['Gemeente'] == 'BILZEN']
df_bilzen = df_bilzen.dropna(subset=['mediaanprijs'])


# Zorg ervoor dat de kolom 'jaar' numeriek is
X = df_bilzen[['jaar']].values  # Onafhankelijke variabele (input)
y = df_bilzen['mediaanprijs'].values  # Afhankelijke variabele (output)

# Lineair regressiemodel trainen
model = LinearRegression()
model.fit(X, y)

# Voorspelling maken voor de komende 10 jaar
toekomstige_jaren = np.arange(df_bilzen['jaar'].max() + 1, df_bilzen['jaar'].max() + 11).reshape(-1, 1)
voorspellingen = model.predict(toekomstige_jaren)
# print("toekomstige_jaren ", toekomstige_jaren)

# Visualisatie
plt.figure(figsize=(10, 5))
plt.scatter(X, y, color='blue', label="Historische data")
plt.plot(toekomstige_jaren, voorspellingen, color='red', linestyle='dashed', label="Voorspelde trend")
for i in [0, 4, 9]:
    jaar = int(toekomstige_jaren[i][0])
    prijs = voorspellingen[i]
    plt.annotate(f"{jaar}: €{prijs:,.0f}",
                 xy=(jaar,prijs),
                 xytext=(jaar, prijs+15000),
                 ha= 'center',
                 fontsize=9,
                 arrowprops=dict(arrowstyle='->', color= 'grey', lw=0.5))
plt.xlabel("Jaar")
plt.ylabel("Mediaanprijs (€)")
plt.title("Voorspelling van mediaanprijs in Bilzen voor de komende 10 jaar")
plt.legend()
plt.show()
