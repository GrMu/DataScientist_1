
import pandas as pd

# Load the CSV file
df = pd.read_csv('data/shopdata.csv')

# Select the required columns
df_filtered = df[['Customer ID', 'Age', 'Gender', 'Item Purchased', 'Category', 'Color', 'Season']]

# Rename the columns
df_filtered.columns = ['id', 'leeftijd', 'geslacht', 'product', 'categorie', 'kleur', 'seizoen']

print(df_filtered)