import pymongo

if __name__ == '__main__':
    print('Welcome To PyMongo')

    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client['new_db'] # need to create collection too, not just db
    collection = db['new_collection']
    
    # collection.delete_one({'name': 'John'})
    del_mny = collection.delete_many({'name': 'John'})
    print(del_mny.deleted_count)