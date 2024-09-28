# Module 10 Assignment 
# September 27, 2024
# Team Members: Noel Miranda, Christopher Reaney, Kevin Ramirez, Korbyn Mock
# Python Script Objective: Displays the data in each table from database Outland_Adventures

import mysql.connector
from mysql.connector import errorcode

def main():
    # Connect to the MySQL database
    try: 
        connection = mysql.connector.connect(
        host='localhost',  # Update with your host
        user='*********',  # Update with your username
        password='***************',  # Update with your password
        database='Outland_Adventures'  # Your database name
    )
    except mysql.connector.Error as err: 
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(" The supplied username or password are invalid")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(" The specified database does not exist")

        else:
            print(err)

    cursor = connection.cursor()

    # List of tables to display data from
    tables = [
        'Department',
        'Employees',
        'Equipment',
        'Trip_Information',
        'Booking',
        'Customers',
        'Inventory'
    ]

    for table in tables:
        display_data(cursor, table)

    # Close the cursor and connection
    cursor.close()
    connection.close()

def display_data(cursor, table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    print(f"\n - - {table_name} - -")
    for row in rows:
        print(row)

if __name__ == "__main__":
    main()