#Scott Larrentree
# module_9.2
#reuse form 8.2


## import to connect to database+

import mysql.connector
from mysql.connector import errorcode

#profile for database
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

#try to connect if failed throw exception
try:

    db = mysql.connector.connect(**config) # connect to the pysports database 
    
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    print('\n')


except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)


#create a database object
cursor = db.cursor()

#makeing sql string for later use 
sql = "SELECT player_id, first_name, last_name, team_name\
     FROM player\
     INNER JOIN team\
     ON player.team_id = team.team_id;"


# execute sql inner join
cursor.execute(sql)

#get the information form the database an make an array called players
players = cursor.fetchall()

print("- - DISPLAYING PLAYER RECORDS - -")

#print info 
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name : {}".format(player[1]))
    print("Last Name : {}".format(player[2]))
    print("Team Name : {}".format(player[3]))
    print('\n')

input("\n\n  Press any key to continue...")

db.close()