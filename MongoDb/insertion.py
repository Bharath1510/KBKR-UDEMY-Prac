import pymongo

client = pymongo.MongoClient()

db = client['lib']
books = db['books']

books.insert_one({
    'name':'kbkr'
    'author':'me'
    'year': 2019

})

books.insert_many([
    {
        'name':'bharath'
        'author':'me'
        'year': 2020
    },
    {
        'name':'kumar'
        'author':'me'
        'year': 2019
    }
])