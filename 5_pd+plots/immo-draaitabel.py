import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

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

print(df_pivot_transac)

# Draaitabel maken
df_pivot_mediaan = df_filtered.pivot_table(
    index='jaar',
    columns='Gemeente',
    values='mediaanprijs',
    aggfunc='mean'
)

print(df_pivot_mediaan)

df_pivot_mediaan.plot(kind='line', figsize=(12,6))
plt.xlabel("Jaar")
plt.ylabel("Mediaanprijs")
plt.title("Mediaanprijs per gemeente per jaar")
plt.legend(title="Gemeente")

# Grafiek tonen
plt.show()
