from pymongo import MongoClient
import os


def get_db_client():
    client = MongoClient(os.getenv('MONGO_CONNECTION_STRING'))
    db = client.get_database(os.getenv('DATABASE_NAME'))
    return db
