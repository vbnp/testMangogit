import pymongo
client = pymongo.MongoClient("mongodb+srv://sukubhi:Anu77852286@clustervish.ri4sb.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {"name" : "vishal",
     "emailid": "sukubhi@gmail.com",
      "surname" : "kumar"}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
