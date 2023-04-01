import pymongo

from helper import MongoConfig

# connect to the MongoDB server
client = pymongo.MongoClient(MongoConfig().db_url())

# create a new database and collection
db = client['test_database']
collection = db['persons']

# insert a document into the collection
document = {'name': 'Alice', 'age': '20', 'email': 'something@something.com'}
result = collection.insert_one(document)
print(result.inserted_id)

# query the collection for all documents
documents = collection.find()
for document in documents:
    # print(document['_id'], document['name'], document['age'])
    print(document)

print('=== Search results 1 === ')
# query the collection for documents that match a specific condition
documents = collection.find({'name': 'Alice'})
for document in documents:
    print(document)

print('=== Search results 2 === ')
documents = collection.find({'email': 'something@something.com'})
for document in documents:
    print(document['_id'], document['name'], document.get('age'), document.get('email'))
