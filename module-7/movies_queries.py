# Noel Miranda, September 19, 2024, Module 7.2 assignment.
# The purpose of this program is to execute queries to the movies database from a
# python program. The credentials in the configuration object has asterisks for 
# security and privacy purposes. Replace with appropriate credentials.

import mysql.connector
from mysql.connector import errorcode

# configuration object to hold database credentials 
# (asterisks used in configuration for security purposes due to uploading to GitHub)
config = {
    "user": "***", # Replace asterisks with actual username
    "password": "***************", # Replace asterisks with actual password
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

# connection test code to verify the connection to MySQL server
try: 
    db = mysql.connector.connect(**config)
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format
    (config["user"], config["host"], config["database"]))
    print("\n")

except mysql.connector.Error as err: 
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()

# Main function
def main():
    # First Query: Select all the fields for the studio table
    print("-- DISPLAYING Studio RECORDS --")
    cursor.execute("SELECT * FROM studio;")
    studios = cursor.fetchall()
    for studio in studios:
        print(f"Studio ID: {studio[0]}")
        print(f"Studio Name: {studio[1]}\n")
    print()

    # Second Query: Select all the fields for the genre table
    print("-- DISPLAYING Genre RECORDS --")
    cursor.execute("SELECT * FROM genre;")
    genres = cursor.fetchall()
    for genre in genres:
        print(f"Genre ID: {genre[0]}")
        print(f"Genre Name: {genre[1]}\n")
    print()

    # Third Query: Select the movie names for those movies that have a run 
    # time of less than two hours (120 minutes)
    print("--DISPLAYING Short Film RECORDS --")
    cursor.execute("""
        SELECT film_name, film_runtime
        FROM film
        WHERE film_runtime < 120;
    """)
    films = cursor.fetchall()
    for film in films:
        print(f"Film Name: {film[0]}")
        print(f"Runtime: {film[1]}\n")
    print()

    # Fourth Query: Select a list of film names and directors grouped by directors
    print("-- DISPLAYING Director RECORDS in ORDER --")
    cursor.execute("""
        SELECT film_name, film_director
        FROM film
        ORDER BY film_director;
        """)
    directors = cursor.fetchall()
    for director in directors:
        print(f"Film Name: {director[0]}")
        print(f"Director: {director[1]}\n")
    print()

    # Closes the database connection
    cursor.close()
    db.close()

# Executes main() function when on main
if __name__ == '__main__':
    main()