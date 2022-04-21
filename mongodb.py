from pymongo import MongoClient

def db_info():
    HOST = 'lotto.7mh4m.mongodb.net'
    USER = 'suzzang'
    PASSWORD = 'suzzang'
    DATABASE_NAME = 'myFirstDatabase'
    return HOST, USER, PASSWORD, DATABASE_NAME

def db_connect(MONGO_URI, DATABASE_NAME, COLLECTION_NAME):
    client = MongoClient(MONGO_URI)
    database = client(DATABASE_NAME)
    collection = database(COLLECTION_NAME)
    return collection
 
