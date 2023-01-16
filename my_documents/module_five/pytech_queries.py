#Scott Larrentree
#Module 5.3 

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.4diuzc0.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url);
db = client.pytech;




docs = db.students.find({});

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --");

#find
for item in docs :
    print("Student ID: " + item["student_id"] + "\n" +
     "First Name: " + item["first_name"] + "\n" + 
     "Last Name: " + item["last_name"] + "\n" );






# find_one 
doc = db.students.find_one({"student_id" : "1007"});

print( "-- DISPLAY STUDENT DOCUMENT FROM find_one() QUERY --" );

print("Student ID : " + doc["student_id"]);
print("First Name : " + doc["first_name"]);
print("Last Name : " + doc["last_name"]);

