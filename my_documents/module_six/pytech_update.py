#Scott Larrentree
#moudule 6.2

#reused code from pytech_queries.py only needed to add update line 27

#import mongo client
from pymongo import MongoClient

#connection key into a variable for easy of use
url = "mongodb+srv://admin:admin@cluster0.4diuzc0.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url);
db = client.pytech;

#setting docs equal to the document students with find()
docs = db.students.find({});

#print for display
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --");

#printing what is on the document in readable format
for item in docs :
    print("Student ID: " + item["student_id"] + "\n" +
     "First Name: " + item["first_name"] + "\n" + 
     "Last Name: " + item["last_name"] + "\n" );

#updating last name to Snuffles for student with the id 1007
update = db.students.update_one({"student_id" : "1007"}, {"$set": {"last_name": "Snuffles"}});

# find_one 
doc = db.students.find_one({"student_id" : "1007"});
 #print for dislay
print( "-- DISPLAY STUDENT DOCUMENT 1007 --" );

#printing what is found in readable format
print("Student ID : " + doc["student_id"]);
print("First Name : " + doc["first_name"]);
print("Last Name : " + doc["last_name"]);

#print end of program so it stays open till user closes the program
input("End of program, press any key to continue...");