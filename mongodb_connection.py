import pymongo

# connect to mongodb
conn = pymongo.MongoClient()

# print database names in mongodb
print conn.database_names()

# set to database conn.db1
db = conn.db1

# set to db1.profiles collection
mycollect = db.profiles

# insert one json-like doc for db1.profiles collection
result = mycollect.insert({'name':'name1','age':1,'lang':['en','fr','de','zh']})

# print all docs in collection db1.profiles
for i in mycollect.find():
    print i

# note:
# sudo pip install pymongo