#Scott Larrentree
#
# I did get stuck for a few days and
# had to look at the document for direction
#

# connect to database
import sys
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


# create a method to see what the cutomer wants to do with the program
#
#
#
def show_menu():
    print ("\n - - - Main Menu - - - ")

    print ("    1. View Books\n    2. View Store Locations\n    3. My Account\n    4. Exit Program")

# get input from customer
    try: 
        choice = int(input('\nPlease enter your selection, example enter 1 to View Books :  '))

# make it valid get choice from customer until it is a valid selection     ( moved this to the main instead of the method)
#        while choice <=0 or choice >=5:
#          print( "\nInvalid selection please try again")
#            choice = int(input('\nPlease enter your selection:  '))
#           
        return choice

    except ValueError:
        print("   You have made an invalid selection the program will now end.  ")

        sys.exit(0)
########################################################################## end of show menu method



# create a method to show the books at the store 
#
#
def show_books(cursor):

# inner join set as variable
    sql = "SELECT book_id, book_name, author, details FROM book"

#execute inner join
    cursor.execute(sql)

    books = cursor.fetchall()

    print("\n  Here is the list of books we have to offer! ")


# print the books and details for all the books at the store 
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[1],book[2],book[3]))

########################################################################  end of show books method


#create show locations method to show all the location for the store
#
#
def show_locations(cursor):
    
    #sql to select the store info
    sql = "SELECT store_id, locale FROM store"

    cursor.execute(sql)

    locations = cursor.fetchall()

    print("\n  Here is the current locations we have! ")

# display the location
    for location in locations:
        print("   Locale:  {}\n".format(location[1]))

########################################################### end of show locations method


# validate the user id 
#
#
def validate_user():

    try:

# get user id 
        user_id = int(input("\n Please enter your customer ID number : "))

#validate user id before returning
        while user_id < 0 or user_id > 3:
            
            print("\n Sorry that does not match our records please try again.")
            user_id = int(input("\n Please enter your customer ID number : "))
        return user_id
    
    except ValueError:

        print("   You have made an invalid selection the program will now end.  ")

        sys.exit(0)

############################################### end of validate method




# show account method 
#
#
#
def show_account_menu():

# get the user choice in the account menu
    try:
        print("\n Welcome back! Please choose an option below. ")

        print("\n   1. Wishlist\n   2. Add Book\n   3.Main Menu ")

        account_option = int(input('Selection:  '))

        return account_option
    except ValueError:
        print("   You have made an invalid selection the program will now end.  ")

        sys.exit(0)
##################################################### end of show account method



# method to show the wishlist for the user
#
#
def show_wishlist(cursor,user_id):
    
    # a complex JOIN that i did not figure out had to look at the class docs to understand this one
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " +
    "FROM wishlist " +
    "INNER JOIN user ON wishlist.user_id = user.user_id " +
    "INNER JOIN book ON  wishlist.book_id = book.book_id " +
    "WHERE user.user_id = {}".format(user_id))

    wishlist = cursor.fetchall()


    print("\n Here are the current books in your wishlist. ")

# print wishlist
    for book in wishlist:
        print("\n    Book Name: {}\n    Author: {}\n".format(book[4],book[5]))


#################################################################### end of show wish list method


# mehtod to show what books can be added to the user wishlist
#
#

def show_books_to_add(cursor,user_id):

# another part that lost me here we take all the books in the store and remove the ones already in the user wish list
    cursor.execute("SELECT book_id, book_name, author, details "+
    "FROM book "+
    "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(user_id))

    books_to_add = cursor.fetchall()

    print("\n Here are all the books available that is NOT on your wishlist. ")

# show all the books that are no in the user wishlist
    for book in books_to_add:
        print("\n    Book ID: {}\n    Book Name: {}\n".format(book[0],book[1]))

######################################################## end of show avaialbe books for wishlist


# method to add book to wishlist
#
#

def add_book_to_wishlist(cursor, user_id, book_id):

    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(user_id, book_id))

############################################ end of add book to wishlist



### main program 
#
#


# try connect to data base
try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    print("\n Welcome to WhatABook! ")
    print("\n What would you like to do? ")

# send user to main menu 
    user_selection = show_menu()

# if user does not choose option 4 user starts loop
    while user_selection != 4 :

# if user choose option 1 show books to user
        if user_selection == 1:
            show_books(cursor)
        
#if user choose option 2 show user the store location        
        if user_selection == 2:
            show_locations(cursor)
        
#if user choose option 3 first validate the user id the send user to account menu
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

# in account menu if user does not enter 3 user will enter loop
            while account_option !=3:
                
# if user chooses 1 show user their wishlist                
                if account_option == 1:
                    show_wishlist(cursor,my_user_id)

# if user chooses 2 show user books not on wishlist that they can add and then get book id and add book to wishlist
                if account_option == 2:
                    show_books_to_add(cursor,my_user_id)

                    book_id = int(input("\n What is the ID of the book you want to add: "))

                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit()

                    print(" Book ID: {} was added to your wishlist!".format(book_id))

# if user makes a invalid choice try again
                if account_option < 0 or account_option > 3:
                    print( "\n Im sorry thats not a valid choice please try again. ")

                account_option = show_account_menu()

#if user makes an invalid choice try again 
        if user_selection < 0 or user_selection > 4:
            print("Sorry that is not a valid choice please try again. ")

        user_selection = show_menu()
    print("\n Thanks for trying the program! GoodBye!")

    db.close()

# if exveption is thrown when trying to connect to data base
except mysql.connector.Error as err:
    
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)
