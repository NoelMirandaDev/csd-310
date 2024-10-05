# Noel Miranda, October 2, 2024, Module 11.1 assignment.
# The purpose of this program is to execute queries to the outland adventures database from a
# python program. The credentials in the configuration object has asterisks for 
# security and privacy purposes. Replace with appropriate credentials.

import mysql.connector
from mysql.connector import errorcode

# Dictionary configuration object to hold database credentials 
config = {
    "user": "*********", # Replace asterisks with actual username
    "password": "************", # Replace asterisks with actual password
    "host": "localhost", # Replace with your host name
    "database": "outland_adventures", # Replace with your database
    "raise_on_warnings": True
}

# Connection test to verify the connection to MySQL server
try: 
    db = mysql.connector.connect(**config)
    print("\nDatabase user {} connected to MySQL on host {} with database {}\n".format
    (config["user"], config["host"], config["database"]))

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

    # Stored Procedure Creation for Database
    cursor.execute("DROP PROCEDURE IF EXISTS GetBookingsByYear;")
    cursor.execute("""
        CREATE PROCEDURE GetBookingsByYear(IN input_year INT)
        BEGIN 
            SELECT 
                SUBSTRING_INDEX(T.`Location`, ' - ', 1) AS Continent,
                COUNT(B.BookingID) AS Booking_Count
            FROM Trip_Information AS T
            LEFT JOIN Booking AS B
            ON T.TripID = B.TripID AND YEAR(B.Date_Booked) = input_year
            GROUP BY Continent;
        END;
        """)

    # Commit the changes
    db.commit()

    # Input year to analyze bookings for the year.
    # Caution this input does not have a validation, validation would be required in the future if
    # database were to be public to avoid security breaches.
    input_year = input("What year would you like to analyze bookings for: ")
    print("\n")

    print(f"\nOutland Adventures Bookings Per Location for {input_year}")
    print("--------------------------------------------------------")
    
    # Call stored procedure in database
    cursor.execute(f"CALL GetBookingsByYear({input_year});")

    trends = cursor.fetchall()
    for trend in trends:
        print(f"\nLOCATION: {trend[0]:<17}    |   BOOKINGS: {trend[1]:<10}\n")
        print("--------------------------------------------------------")

    # Closes the database connection
    cursor.close()
    db.close()

if __name__ == '__main__':
    main()