import logging
from api.db_access.planet_db_access import PlanetDbAccess
from api.helpers.swapi_helper import enrich_planet_data
from api.exceptions.planet_already_exist_exception import PlanetAlreadyExistException
from api.validators.planet_structure_validator import validate_planet_structure
from bson.json_util import dumps


class PlanetService:

    def __init__(self) -> None:
        self.__db_access = PlanetDbAccess()

    def create_planet(self, planet: dict) -> dict:
        logging.debug(f"[PLANET SERVICE] Creating planet")
        validate_planet_structure(planet)
        found_planet = self.__db_access.find_planet_by_name(planet["name"])

        if found_planet is not None:
            raise PlanetAlreadyExistException()
        planet = enrich_planet_data(planet)

        planet = self.__db_access.add_planet(planet)
        planet_id = str(planet.inserted_id)
        return {"_id": planet_id}

    def get_planets(self) -> list:
        logging.debug(f"[PLANET SERVICE] Finding planets")
        planets = dumps(self.__db_access.find_planets())
        return planets

    def get_planet_by_id(self, planet_id: str) -> dict:
        logging.debug(f"[PLANET SERVICE] Finding planet by id - {planet_id}")
        planet = self.__db_access.find_planet_by_id(planet_id)
        planet = dumps(planet) if planet is not None else {}
        return planet

    def get_planet_by_name(self, planet_name: str) -> dict:
        logging.debug(
            f"[PLANET SERVICE] Finding planet by name - {planet_name}")
        planet = self.__db_access.find_planet_by_name(planet_name)
        planet = dumps(planet) if planet is not None else {}
        return planet

    def delete_planet_by_id(self, planet_id: str) -> None:
        logging.debug(f"[PLANET SERVICE] Deleting planet by id - {planet_id}")
        found_planet = self.__db_access.find_planet_by_id(planet_id)
        if found_planet is None:
            raise Exception(f"ID {planet_id}")
        self.__db_access.delete_planet(planet_id)
