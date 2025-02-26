import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "root",
    database = "winkel"
)
c = mydb.cursor()
c.execute("select * from klant")
data = c.fetchall()
for item in data:
        print(*item)

