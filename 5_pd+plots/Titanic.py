# Dit heet analyse.py in de les "

import pandas as pd
df = pd.read_csv("data/titanic.csv")
'''
print(df.columns)
print(df.describe())
print(df.info())
print(f"Rijen: {df.shape[0]}, kolommen: {df.shape[1]}")
'''
# df_subset = df.copy()
df_subset = df['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Fare']
# df_subset = df_subset[['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'Fare']]
df_subset.columns = ['id', 'overleefd', 'klasse', 'Naam', 'Geslacht', 'Leeftijd', 'ticketprijs']
'''
print("df_subset type ", type(df_subset))
print("df_subset ", (df_subset))
'''
df_subset['Leeftijd']= df_subset['Leeftijd'].fillna(0).astype(int)
# df_subset['Leeftijd']= df_subset['Leeftijd'].fillna(0).astype(int)

print("Subset: ", df_subset.head)
print("Klasses: ", df_subset['klasse'].unique())