import mysql.connector
from mysql.connector import errorcode

# configuration object to hold database credentials 
# (asterisks used in configuration for security purposes due to uploading to GitHub)
config = {
    "user": "***", # Replace asterisks with actual username
    "password": "*************", # Replace asterisks with actual password
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

# connection test code to verify the connection to MySQL server
try: 
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")

except mysql.connector.Error as err: 
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally: 
    db.close()