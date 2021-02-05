
from pymongo import MongoClient
import os

client = MongoClient(os.environ.get("MONGODB_URI"))
database = client["planets_db"]


def get_collection():
    planet_collection = database.planet_collection
    planet_collection.create_index("name", unique=True)
    return planet_collection
