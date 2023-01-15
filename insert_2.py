import pymongo

if __name__ == '__main__':
    print('Welcome To PyMongo')

    client = pymongo.MongoClient('mongodb://localhost:27017')
    print(client)
    db = client['new_db'] # need to create collection too, not just db
    collection = db['new_collection']
    # new_dict = {
    #     'name': 'John',
    #     'marks': 50
    # }
    # collection.insert_one(new_dict)
    # insert_list = [
    #     {'name': 'Shawn','marks': 100},
    #     {'name': 'Paul','marks': 90}
    # ]
    # collection.insert_many(insert_list)
    # insert_list = [
    #     {'_id': 1000, 'name': 'Michael','marks': 33},
    #     {'_id': 1001, 'name': 'Jack','marks': 75}
    # ]
    # collection.insert_many(insert_list)
    new_dict = {
        'name': 'John',
        'marks': 10
    }
    collection.insert_one(new_dict)