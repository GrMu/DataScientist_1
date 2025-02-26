import mysql.connector

class DBConnector:

    def __init__(self, database):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database=database
        )
        self.cursor = self.mydb.cursor()

    def toon_tabel_data(self, table):
        sql_string = f"SELECT * FROM {table}"
        self.cursor.execute(sql_string)
        data = self.cursor.fetchall()
        for row in data:
            print(*row)

    def toon_tabellen(self):
        self.cursor.execute("show tables")
        data = self.cursor.fetchall()
        for row in data:
            print(*row)

    def geef_lijst_met_tabellen(self):
        lijst_tabellen = []
        self.cursor.execute("show tables")
        data = self.cursor.fetchall()
        for tabel in data:
            lijst_tabellen.append(*tabel)
        return lijst_tabellen

    def toon_views(self):
        sql = ("SHOW FULL TABLES FROM personeel1 "
               "WHERE table_type = 'VIEW'")
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        for row in data:
            print(*row)


    def toon_kolommen_van_tabel(self, table):
        sql_string = f"SHOW COLUMNS FROM {table}"
        self.cursor.execute(sql_string)
        data = self.cursor.fetchall()
        for row in data:
            print(*row)
    def geef_kolomnamen(self,table):
        sql_string = f"SHOW COLUMNS FROM {table}"
        kolommen_tuples = self.return_query_data(sql_string)
        kolommen = [kolom[0] for kolom in kolommen_tuples]
        return kolommen

    def voer_query_uit(self,sql_string):
        self.cursor.execute(sql_string)
        data = self.cursor.fetchall()
        for row in data:
            print(*row)
    def return_query_data(self,sql_string):
        self.cursor.execute(sql_string)
        data = self.cursor.fetchall()
        return data

    def toon_tabel_view(self):
        lijst_tabellen = self.geef_lijst_met_tabellen()
        for index, tabel in enumerate(lijst_tabellen):
            print(index, tabel)
        keuze = int(input("geef je keuze"))
        if keuze < len(lijst_tabellen):
            tabel = lijst_tabellen[keuze]
            self.toon_tabel_data(tabel)
        else:
            print("foute invoer")


    def sluit_verbinding(self):
        """ Sluit de databaseverbinding netjes af. """
        self.cursor.close()
        self.mydb.close()

