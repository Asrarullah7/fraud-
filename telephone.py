#Import necessary modules.
import pymongo
from pymongo import MongoClient
import pandas as pd
import numpy as np

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["task_guvi"]
print(db)

db= MongoClient("mongodb://localhost:27017")
#Create a database using attribute style on a MongoClient instance.
#Declare a variable db and assign the new database as an attribute of the client.
#Create a collection.
mycollection = db["telephonedirectory"]
print(mycollection)

#For CRUD operation, create a directory which has fields like Name, Phone number, Place etc.,    
#Insert the record into the collection.

document = {'name':"farid", 
            "phone no": 234567891,
            "place": "chennai"}
mycollection.insert_one(document)
    
document1 = [{"Name":"abc","Phone no":123456789,"place":"chennai"},
                 {"Name":"cde","Phone no":525252525,"place":"salem"},
                 {"Name":"efg","Phone no":9638527410,"place":"goa"},
                 {"Name":"qwe","Phone no":2326565989,"place":"kerala"},
                 {"Name":"rty","Phone no":7898152626,"place":"ooty"}
                 ]
    
mycollection.insert_many(document1)


#Make a query to find records you just created.
    
all_records = mycollection.find()
print(all_records)
for row in all_records:
    print(row)
#Modify the records, use the update_one() method. The update_one() method requires two arguments, query and update.
prev = {"Name": "cde"}
nextt= {'$set': {"Name": "cfg"}}
mycollection.update_one(prev,nextt)


all_records = mycollection.find()
print(all_records)
for row in all_records:
    print(row)


#Delete the record, use delete_one() method. delete_one() requires a query parameter which specifies the document to delete.
mycollection.delete_one({"Name":"Vivek"})
all_records = mycollection.find()
print(all_records)
for row in all_records:
    print(row)
