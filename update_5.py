import pymongo

if __name__ == '__main__':
    print('Welcome To PyMongo')

    client = pymongo.MongoClient('mongodb://localhost:27017')
    print(client)
    db = client['new_db'] # need to create collection too, not just db
    collection = db['new_collection']
    
    collection.update_one({'name': 'John'}, {"$set": {"marks": 10}})
    upd = collection.update_many({'name': 'John'}, {"$set": {"marks": 10}})
    print(upd.modified_count)