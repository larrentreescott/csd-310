#Scott Larrentree
#module 10.3


# connect to database
import mysql.connector
from mysql.connector import errorcode

# profile for database

config = {
    "user" : "whatabook_user",
    "password" : "MySQL8IsGreat!",
    "host" : "localhost",
    "database" : "whatabook",
    "raise_on_warnings" : True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    print("\n")

except mysql.connector.Error as err:
    
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)
