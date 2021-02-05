from api.config.mongo import get_collection
from bson.json_util import ObjectId


class PlanetDbAccess():

    def __init__(self) -> None:
        self.__planet_collection = get_collection()

    def add_planet(self, planet: dict) -> dict:
        planet = self.__planet_collection.insert_one(planet)
        return planet

    def find_planets(self) -> list:
        planets = self.__planet_collection.find()
        return planets

    def find_planet_by_id(self, planet_id: str) -> dict:
        find_query = {"_id": ObjectId(planet_id)}
        planet = self.__planet_collection.find_one(find_query)
        return planet

    def find_planet_by_name(self, planet_name: str) -> dict:
        find_query = {"name": planet_name}
        planet = self.__planet_collection.find_one(find_query)
        return planet

    def delete_planet(self, planet_id: str) -> None:
        delete_query = {"_id": ObjectId(planet_id)}
        self.__planet_collection.delete_one(delete_query)
