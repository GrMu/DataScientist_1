import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'mens'
)
mycursor = mydb.cursor()

"""
people_data = [("Jan", 33, "Zutedaal"),
                ("Piet", 66, "As"),
                ("Miriam", 44, "Diepenbeek"),
                ("Petra", 39, "Zutendaal")
                ]

mycursor.executemany('''
    INSERT INTO people (voornaam, leeftijd, gemeente)
    VALUES (?, ?, ?)
    ''', people_data)
"""

mycursor.execute("SELECT * FROM people")
myresult = mycursor.fetchall()
for x in myresult:
    print(*x)
