#Scott Larrentree
#module 6.3
# delete
# a lot of code form previous 
# assignments pytech_queries, pytech_insert

#import mongo client
from pymongo import MongoClient

#connection key into a variable for easy of use
url = "mongodb+srv://admin:admin@cluster0.4diuzc0.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url);
db = client.pytech;

#setting docs equal to the document students with find()
docs1 = db.students.find({});

#print for display
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --");

#printing what is on the document in readable format
for item in docs1 :
    print("Student ID: " + item["student_id"] + "\n" +
     "First Name: " + item["first_name"] + "\n" + 
     "Last Name: " + item["last_name"] + "\n" );

#creating a new student with id 1010
sam = {
    "student_id" : "1010",
    "first_name" : "Sam",
    "last_name" : "Sung"};

# insert new student
sam_student_id = db.students.insert_one(sam).inserted_id;

#printing student document id 
print("Inserted student record into the students collection with document_id ");
print (sam_student_id);


# find_one 
doc = db.students.find_one({"student_id" : "1010"});


#spacing
print("\n");
 #print for dislay
print( "-- DISPLAY STUDENT DOCUMENT 1010 --" );

#printing what is found in readable format
print("Student ID : " + doc["student_id"]);
print("First Name : " + doc["first_name"]);
print("Last Name : " + doc["last_name"]);


#delete student with id 1010
db.students.delete_one({"student_id" : "1010"})



#setting docs equal to the document students with find()
#used new variable to make sure we get new info
docs2 = db.students.find({});

#spacing when display
print("\n");
#print for display
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --");

#printing what is on the document in readable format
for item in docs2 :
    print("Student ID: " + item["student_id"] + "\n" +
     "First Name: " + item["first_name"] + "\n" + 
     "Last Name: " + item["last_name"] + "\n" );

