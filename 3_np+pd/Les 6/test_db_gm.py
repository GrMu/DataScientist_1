from connect_to_db import *
db = DBConnector("winkel")
db.toon_tabellen()
#tabellen = ["klant", 'producten', "bestelling"]
tabellen = db.geef_lijst_met_tabellen()
'''for tabel in tabellen:
    print(); print(tabel)
    print("----------")
    db.toon_tabel_data(tabel)
'''
db.toon_kolommen_van_tabel("klant")

kolommen = db.geef_kolomnamen("klant")
print(kolommen)

for tabel in tabellen:
    print(tabel, db.geef_kolomnamen(tabel))

db.voer_query_uit("select * from klant where gemeente = "genk"")

