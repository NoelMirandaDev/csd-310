# Kevin Ramirez
# Module 11.1 Assignment
# October 2, 2024
# Python Script Objective: Displays data that is over or under 5 years old


import mysql.connector
from mysql.connector import errorcode

def main():

    config = {
        'user': 'root',
        'password': '*******',
        'host': 'localhost',
        'database': 'Outland_Adventures'
    }

    try:
        db = mysql.connector.connect(**config)
        print("\nDatabase user {} connected to MySQL on host {} with database {}\n".format(
            config["user"], config["host"], config["database"]))

        cursor = db.cursor()

        # SQL query to find inventory items over five years old
        query = """
            SELECT
                Inventory.ItemID, 
                Inventory.Date_On_Shelf, 
                Equipment.Equipment_Name,
                FLOOR(DATEDIFF(NOW(), Inventory.Date_On_Shelf) / 365) AS Age_Years, -- Calculate full years
                DATEDIFF(NOW(), Inventory.Date_On_Shelf) % 365 AS Age_Days -- Calculate remaining days
            FROM Inventory
            JOIN Equipment ON Inventory.EquipmentID = Equipment.EquipmentID
            WHERE Inventory.Date_On_Shelf <= DATE_SUB(CURDATE(), INTERVAL 5 YEAR);
        """

        cursor.execute(query)

        results = cursor.fetchall()
        if results:
            print("Items over 5 years old:")
            print("-" * 40)
            for row in results:
                print(f"ItemID: {row[0]}")
                print(f"Date_On_Shelf: {row[1]}")
                print(f"Equipment_Name: {row[2]}")
                print(f"Age: {row[3]} years and {row[4]} days")
                print("-" * 40)  # Separator line
        else:
            print("No items are over 5 years old.")

        cursor.close()
        db.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("The supplied username or password are invalid")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("The specified database does not exist")
        else:
            print(err)

if __name__ == "__main__":
    main()










