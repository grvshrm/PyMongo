import pymongo

if __name__ == '__main__':
    print('Welcome To PyMongo')

    client = pymongo.MongoClient('mongodb://localhost:27017')
    print(client)
    db = client['new_db'] # need to create collection too, not just db
    collection = db['new_collection']
    """
    # one = collection.find_one() # any random doc pulled
    one = collection.find_one({'name': 'Michael'}) # if multiple with same val, only one is returned cuz its find_one
    print(one)
    print("All....")
    all_docs = collection.find({'name': 'Michael'}) # return all
    print(all_docs)
    for item in all_docs:
        print(item)

    one = collection.find_one({'name': 'Jack'}, {'name': 1, '_id': 0}) # val 1 by default for all, turn to 0 to hide
    print(one)
    print(collection.find_one({'name': 'Jack'}, {'name': 1})) # if u turn one as 1, all others become 0 except _id, _id needs to be explicitly set to 0
    print(collection.find_one({'name': 'Jack'}, {'name': 0})) # if u turn one as 0, all others become 1

    john = collection.find({'name': 'John'}).limit(1)
    print(john.count())
    for j in john:
        print(j)
    print(collection.count_documents(filter = {'name': 'John'}))
    john = collection.find({'name': 'John'})
    for j in john:
        print(j)"""

    john_50 = collection.find({'name': 'John', 'marks': {"$lte": 50}})
    for i in john_50:
        print(i)
