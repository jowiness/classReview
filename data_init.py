import pymongo


def data_init():
    client = pymongo.MongoClient('127.0.0.1',27017)
    db = client['teach']
    return db


db = data_init()
