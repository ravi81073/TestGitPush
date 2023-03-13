import pymongo
client = pymongo.MongoClient("mongodb+srv://ravi:or73ek@cluster0.uwxszzc.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name" : "ravi",
    "email" : "ravi81073@gmail.com",
    "surname" : "kumar"
}

db1  = client [ 'mongotest']
coll = db1['test']
coll.insert_one(d)