#Scott Larrentree
#Module 5.3

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.4diuzc0.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url);
db = client.pytech;

scott = {
    "first_name" : "Scott",
    "last_name" : "Larrentree",
    "student_id" : 1007
};

emily = {
    "first_name" : "Emily",
    "last_name" : "Cox",
    "student_id" : 1008
};

milo = {
    "first_name" : "Milo",
    "last_name" : "Marshal",
    "student_id" : 1009
};


scott_student_id = db.students.insert_one(scott).inserted_id;
emily_student_id = db.students.insert_one(emily).inserted_id;
milo_student_id = db.students.insert_one(milo).inserted_id;

print(" -- INSERT STATEMENTS -- \n");

print("Inserted student record Scott Larrentree into the students collection with document_id ");
print(scott_student_id);
print("Inserted student record Emily Cox into the students collection with document_id ");
print(emily_student_id);
print("Inserted student record Milo Marshal into the students collection with document_id ");
print(milo_student_id);

input("End of program, press any key to exit...");