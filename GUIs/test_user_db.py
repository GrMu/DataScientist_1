import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="data_entry_user",
  password="root1234",
  database = "bieren"
)

mycursor = mydb.cursor()
mycursor.execute("drop schema bieren")
"""data = mycursor.fetchall()
for rij in data:
    print(*rij)
"""