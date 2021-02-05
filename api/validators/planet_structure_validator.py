from api.exceptions.planet_missing_fields_exception import PlanetMissingFieldsException


def validate_planet_structure(planet):
    fields = ["name", "climate", "terrain"]
    for field in fields:
        if field not in planet:
            raise PlanetMissingFieldsException()
