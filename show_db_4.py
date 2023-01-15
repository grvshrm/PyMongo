import pymongo

if __name__ == '__main__':
    print('Welcome To PyMongo')

    client = pymongo.MongoClient('mongodb://localhost:27017')
    print(client)
    db = client['new_db'] # need to create collection too, not just db
    collection = db['new_collection']
    print(client.list_database_names())
    print(db.list_collection_names())