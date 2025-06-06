"""
Aanmaken en plotten van pivot-tabel
Aanvulling: regressie op pivot-tabel
"""

# Data van Belstat
# "https://statbel.fgov.be/nl/themas/bouwen-wonen/vastgoedprijzen"
# "C:\Users\mulderg\Downloads\NL_immo_statbel_kwartaal_per_gemeente.xlsx"

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

# Bestand inlezen
df = pd.read_excel('Data/immo_dataset.xlsx')

# Kolom 'Lokaliteit' hernoemen naar 'Gemeente' (indien nodig)
if 'Lokaliteit' in df.columns:
    df.rename(columns={'Lokaliteit': 'Gemeente'}, inplace=True)

# Gemeentes om te behouden
gemeentes = ['BILZEN', 'HASSELT', 'GENK', 'TONGEREN', 'KNOKKE-HEIST']

# DataFrame filteren op gewenste gemeentes
df_filtered = df[df['Gemeente'].isin(gemeentes)]

# Enkel de gewenste kolommen behouden
kolommen_behouden = ['Gemeente', 'jaar', 'periode', 'aantal transacties', 'mediaan prijs(€)']
df_filtered = df_filtered[kolommen_behouden]

# Kolomnamen aanpassen
df_filtered.rename(columns={
    'periode': 'kwartaal',
    'aantal transacties': 'transacties',
    'mediaan prijs(€)': 'mediaanprijs'
}, inplace=True)

# Draaitabel maken
df_pivot_transac = df_filtered.pivot_table(
    index='jaar',
    columns='Gemeente',
    values='transacties',
    aggfunc='sum'
)

# print(df_pivot_transac)

# Draaitabel maken
df_pivot_mediaan = df_filtered.pivot_table(
    index='jaar',
    columns='Gemeente',
    values='mediaanprijs',
    aggfunc='mean'
)

# print(df_pivot_mediaan)

# Initialiseer X & Y -vectoren tbv. regressie per gemeente
X = [0 for i in range(len(gemeentes))]
Y = [0 for i in range(len(gemeentes))]
voorspellingen = [0 for i in range(len(gemeentes))]
historische_voorspellingen = [0 for i in range(len(gemeentes))]
r2 = [0 for i in range(len(gemeentes))]

max_jaar = df_pivot_mediaan.index.max()
toekomstige_jaren = np.arange(max_jaar + 0, max_jaar + 11).reshape(-1, 1)
# print("toekomstige_jaren ", toekomstige_jaren)

for i, gemeente in enumerate(gemeentes):
    X[i] = df_pivot_mediaan.index.values    # Onafhankelijke variabele (input)
    X[i] = X[i].reshape(-1, 1)              # omzetten naar 2D array
    Y[i] = df_pivot_mediaan[gemeente].values  # Afhankelijke variabele (output)
    Y[i] = Y[i].reshape(-1, 1)              # omzetten naar 2D array
    model = LinearRegression()
    model.fit(X[i], Y[i])

    # Toon model parameters
    print(f"\nModel coëfficiënt (stijging per jaar): €{model.coef_[0][0]:,.0f}")
    print(f"Model intercept: €{model.intercept_[0]:,.0f}")

    voorspellingen[i] = model.predict(toekomstige_jaren)
    historische_voorspellingen[i] = model.predict(X[i])

    # R-squared score
    r2[i] = r2_score(Y[i], historische_voorspellingen[i])
    print(f"\nModel R² score {gemeente}: {r2[i]:.3f} (hoe dichter bij 1, hoe beter het model)")

'''
# Pivot-plot zonder trendlijnen
df_pivot_mediaan.plot(kind='line', figsize=(12,6))
plt.xlabel("Jaar")
plt.ylabel("Mediaanprijs")
plt.title("Mediaanprijs per gemeente per jaar")
plt.legend(title="Gemeente")

# Grafiek tonen
plt.show()
'''
# Visualisatie
# color = ['blue', 'red', 'green', 'yellow', 'orange']
color = ["red", "darkorange", "deepskyblue", "green", "purple", "brown", "magenta", "darkcyan"]
plt.figure(figsize=(12, 7))
for i, gemeente in enumerate(gemeentes):
    plt.scatter(X[i], Y[i], color=color[i], label=f"Historische data in {gemeente}")
    plt.plot(toekomstige_jaren, voorspellingen[i], color=color[i], linestyle='dashed', label=f"Voorspelde trend met R\N{SUPERSCRIPT TWO} = {r2[i]:,.2f}")
    plt.plot(X[i], historische_voorspellingen[i], color=color[i], linestyle='dashdot')

    # Creëer een annotatie als gekkigheid (dank aan Soffia)
    if gemeente == "KNOKKE-HEIST":
        for j in [1, 5, 10]:
            jaar = int(toekomstige_jaren[j][0])
            prijs = voorspellingen[i][j][0]
            plt.annotate(f"{jaar}: {prijs/1000:,.0f} k€", xy=(jaar, prijs), xytext=(jaar, prijs - 80000),
                         ha='center', fontsize=9, arrowprops=dict(arrowstyle='->', color='grey', lw=1.5))
plt.xlabel("Jaar")
plt.ylabel("Mediaanprijs (€)")
plt.title(f"Voorspelling van mediaanprijs voor de komende 10 jaar")
plt.legend()
# Formatteer y-as
ax = plt.gca()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'€{x:,.0f}'))
plt.show()

