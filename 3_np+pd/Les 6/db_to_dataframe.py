from connect_to_db import *
import pandas as pd

db = DBConnector("winkel")
#haalt de kolomdata op
kolommen_tuples = db.return_query_data("SHOW COLUMNS FROM klant")
#geeft enkel de kolomnamen
kolommen = [kolom[0] for kolom in kolommen_tuples]
#data van de klanten ophalen
data = db.return_query_data("select*from klant")

df = pd.DataFrame(data)
df.columns = kolommen
print(df)