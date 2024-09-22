# Noel Miranda, September 21, 2024, Module 8.2 assignment.

# The purpose of this program is to execute queries to display selected contents 
# of the film table multiple times with a python function which would allow to be called
# with both a cursor and an output. 

# The credentials in the configuration object has asterisks for 
# security and privacy purposes. Replace with appropriate credentials.

import mysql.connector
from mysql.connector import errorcode

# configuration object to hold database credentials 
# (asterisks used in configuration for security purposes due to uploading to GitHub)
config = {
    "user": "********", # Replace asterisks with actual username
    "password": "*****************", # Replace asterisks with actual password
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

# cursor object for database
cursor = db.cursor()

# Main function to be executed when program called
def main():
    # executes the show_film function
    show_films(cursor, "DISPLAYING FILMS")

    # executes the insert statement & displays output again
    insert_statement(cursor)
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # executes the update statement & displays output again
    update_statement(cursor)
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    # executes the delete statement & displays output again
    delete_statement(cursor)
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

    # Closes the database connection
    cursor.close()
    db.close()

def show_films(cursor, title):
    # Function to execute an inner join on all tables, 
    #       iterate over the dataset and output the results to the terminal window. 

    # Inner Join Query
    cursor.execute("""
        SELECT film_name AS Name, 
               film_director AS Director, 
               genre_name AS Genre, 
               studio_name AS `Studio Name`
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id;
    """)

    # get the results from the cursor object
    films = cursor.fetchall()

    print("\n  -- {} --".format(title))

    # iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format
        (film[0], film[1], film[2], film[3]))

# Insert query function 
def insert_statement(cursor):
    cursor.execute("""
        INSERT INTO film (film_id, film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
            VALUES (4, 'M3GAN', 2022, 102, 'Gerard Johnstone', 2, 1);
    """)

# Update query function
def update_statement(cursor):
    cursor.execute("""
        UPDATE film
        SET genre_id = 1
        WHERE film_id = 2;
    """)

# Delete query function
def delete_statement(cursor):
    cursor.execute("""
        DELETE FROM FILM 
        WHERE film_id = 1;
    """)

# Executes main() function when on main
if __name__ == '__main__':
    main()