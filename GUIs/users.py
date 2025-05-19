import mysql.connector
from mysql.connector import Error

def fetch_all_users():
    try:
        # Maak verbinding met de MySQL-server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',           # Vervang door je root-username of een gebruiker met toegang
            password='root'  # Vervang door het wachtwoord
        )

        if connection.is_connected():
            print("Verbonden met MySQL-server")

            # Maak een cursorobject om de query uit te voeren
            cursor = connection.cursor()
            query = "SELECT User, Host FROM mysql.user;"
            cursor.execute(query)

            # Resultaten ophalen en afdrukken
            users = cursor.fetchall()
            print("Lijst van gebruikers:")
            for user, host in users:
                print(f"Gebruiker: {user}, Host: {host}")

    except Error as e:
        print("Fout bij verbinden met MySQL", e)

    finally:
        # Sluit de verbinding
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL-verbinding gesloten")

# Functie aanroepen
fetch_all_users()
