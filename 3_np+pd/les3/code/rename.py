import pandas as pd

# Sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Renaming columns
df.rename(columns={'A': 'X', 'B': 'Y', 'C': 'Z'}, inplace=True)
df.rename(columns={'X':'Wiskunde','Y':'Frans','Z':'Engels'}, inplace=True)
df.columns = [col.capitalize() for col in df.columns]
print(df)