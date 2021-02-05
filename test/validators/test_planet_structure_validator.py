import pytest
import mock
from api.validators.planet_structure_validator import validate_planet_structure
from api.exceptions.planet_missing_fields_exception import PlanetMissingFieldsException


class TestSwapiHelper:

    def test_should_throw_error_if_one_or_more_fields_are_missing(self):
        planet = {
            "name": "Tatooine",
            "climate": "some_climate"
        }
        try:
            validate_planet_structure(planet)
        except Exception as e:
            print(e)
            assert isinstance(e, PlanetMissingFieldsException)
