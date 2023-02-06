#Scott Larrentree
# module_8.2
import mysql.connector
from mysql.connector import errorcode


config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}

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

cursor = db.cursor()

cursor.execute("SELECT team_id, team_name, mascot FROM team")

teams = cursor.fetchall()

print('- - DISPLAYING TEAM RECORDS - -\n')

for team in teams:
    print("Team ID: {}".format(team[0]))
    print("Team Name: {}".format(team[1]))
    print("Mascot : {}".format(team[2]))
    print('\n')

cursor2 = db.cursor()

cursor2.execute("SELECT player_id, first_name, last_name, team_id FROM player")

players = cursor2.fetchall()

print("- - DISPLAYING PLAYER RECORDS - -")

for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name : {}".format(player[1]))
    print("Last Name : {}".format(player[2]))
    print("Team ID : {}".format(player[3]))
    print('\n')

input("\n\n  Press any key to continue...")

db.close()