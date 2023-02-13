#Scott Larrentre
#module 9.3
# reuse reuse almost made a class for this.
#



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


# sql string for insert 
sql_insert = "INSERT INTO player (first_name, last_name, team_id)\
    VALUES('Smeagol' , 'Shire Folk' , 1);"

cursor.execute(sql_insert)

#makeing sql string for inner join
sql_join = "SELECT player_id, first_name, last_name, team_name\
     FROM player\
     INNER JOIN team\
     ON player.team_id = team.team_id;"


# execute sql inner join
cursor.execute(sql_join)

#get the information form the database an make an array called players
players = cursor.fetchall()

print("- - DISPLAYING PLAYER AFTER INSERT - -")

#print info 
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name : {}".format(player[1]))
    print("Last Name : {}".format(player[2]))
    print("Team Name : {}".format(player[3]))
    print('\n')

#sql string for update 
sql_update = "UPDATE player\
    SET team_id = 2\
    WHERE first_name = 'Smeagol';"

#execute sql strings
cursor.execute(sql_update)
cursor.execute(sql_join)

players = cursor.fetchall()

print("- - DISPLAYING PLAYER AFTER UPDATE - -")

#print info 
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name : {}".format(player[1]))
    print("Last Name : {}".format(player[2]))
    print("Team Name : {}".format(player[3]))
    print('\n')

#sql string for delete
sql_delete = "DELETE FROM player\
    WHERE first_name = 'Smeagol'"

#execute 
cursor.execute(sql_delete)
cursor.execute(sql_join)

players = cursor.fetchall()

print("- - DISPLAYING PLAYER AFTER DELETE - -")

#print info 
for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name : {}".format(player[1]))
    print("Last Name : {}".format(player[2]))
    print("Team Name : {}".format(player[3]))
    print('\n')


input("\n\n  Press any key to continue...")

db.close()