# Noel Miranda, October 2, 2024, Module 11.1 assignment.
# The purpose of this program is to execute queries to the outland adventures database from a
# python program. The credentials in the configuration object has asterisks for 
# security and privacy purposes. Replace with appropriate credentials.

import mysql.connector
from mysql.connector import errorcode

# Dictionary configuration object to hold database credentials 
config = {
    "user": "*********", # Replace asterisks with actual username
    "password": "***************", # Replace asterisks with actual password
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
    try:
        # Drop Existing Stored Procedure
        cursor.execute("DROP PROCEDURE IF EXISTS GetEquipmentSalesSummaryByYear;")
    except mysql.connector.Error as err:
        print(f"Error dropping procedure: {err}")
        
    # Stored Procedure Creation for Database Using Subqueries
    cursor.execute("""
        CREATE PROCEDURE GetEquipmentSalesSummaryByYear(IN input_year INT)
        BEGIN
            SELECT
		        (SELECT COUNT(DISTINCT C.CustomerID)
		        FROM Customers AS C
		        LEFT JOIN Booking AS B
		        ON C.BookingID = B.BookingID
		        WHERE YEAR(B.Date_Booked) = input_year
                ) AS 'Total Customers in 2024',
		        (SELECT COUNT(C.Equipment_Bought)
		        FROM Customers AS C
		        LEFT JOIN BOOKING AS B
		        ON C.BookingID = B.BookingID
		        WHERE YEAR(B.Date_Booked) = input_year AND C.Equipment_Bought = 1
                ) AS 'Total Equipment Bought',
		        (SELECT COUNT(C.Equipment_Rented)
		        FROM Customers AS C
		        LEFT JOIN BOOKING AS B
		        ON C.BookingID = B.BookingID
		        WHERE YEAR(B.Date_Booked) = input_year AND C.Equipment_Rented = 1
                ) AS 'Total Equipment Rented';
        END;
    """) 

    # Commit the changes
    db.commit()

    # Input year to analyze equipment sales per year.
    # Caution this input does not have a validation, validation would be required in the future if
    # database were to be public to avoid security breaches.
    input_year = input("For what year would you like to retrieve the equipment sales summary: ")
    print("\n")

    print(f"\nOutland Adventures Equipment Sales Summary for {input_year}")
    print("--------------------------------------------------------")
    
    # Call stored procedure in database
    cursor.execute(f"CALL GetEquipmentSalesSummaryByYear({input_year});")

    Sales = cursor.fetchall()
    for sale in Sales:
        print(f"\nTOTAL DISTINCT CUSTOMERS: {sale[0]:<17}\n")
        print("--------------------------------------------------------")
        print(f"\nTOTAL EQUIPMENT BOUGHT: {sale[1]:<17}\n")
        print("--------------------------------------------------------")
        print(f"\nTOTAL EQUIPMENT RENTED: {sale[2]:<17}\n")
        print("--------------------------------------------------------")


    # Closes the database connection
    cursor.close()
    db.close()

if __name__ == '__main__':
    main()