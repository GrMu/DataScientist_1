import pandas as pd

from connect_to_db import *
db = DBConnector("winkel")
db.toon_tabellen()
db.toon_tabel_data("klant")

data = db.return_query_data("select * from klant")
# Verschillende methodes om kolomnamen te verkrijgen en aan dataframe toe te voegen
kolommen_1 = db.geef_kolomnamen("klant")
print("kolommen_1: ", kolommen_1)
'''kolom= db.voer_query_uit("SHOW COLUMNS FROM klant")
db.mydb.commit()
print('kolom: ', kolom) # geeft none
'''
kolommen_tuple = db.return_query_data("SHOW COLUMNS FROM klant")
kolommen_2 = [kolom[0] for kolom in kolommen_tuple]
print("kolommen_2: ", kolommen_2)

print(data)

df=pd.DataFrame(data)
df.columns = kolommen_2
print(df)
