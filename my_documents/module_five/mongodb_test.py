
# Scott larrentree
#Module 5.2

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.4diuzc0.mongodb.net/?retryWrites=true&w=majority";
client = MongoClient(url);
db = client.pytech;

print(" -- Pytech Collection List -- \n");
print(db.list_collection_names());

input('End of program, press any key to exit');
