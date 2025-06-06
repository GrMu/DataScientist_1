import pandas as pd
import openpyxl

# Bestand inlezen
df = pd.read_excel('Data/immo_dataset.xlsx')

# Kolom 'Lokaliteit' hernoemen naar 'Gemeente' (indien nodig)
if 'Lokaliteit' in df.columns:
    df.rename(columns={'Lokaliteit': 'Gemeente'}, inplace=True)

# Gemeentes om te behouden
gemeentes = ['BILZEN', 'HASSELT', 'GENK', 'TONGEREN']

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

# Groepering per gemeente per jaar met som van transacties
df_grouped = df_filtered.groupby(['Gemeente', 'jaar'])['transacties'].sum().reset_index()

print(df_grouped)
