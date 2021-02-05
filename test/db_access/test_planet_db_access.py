import pytest
import mock
from api.db_access.planet_db_access import PlanetDbAccess


class TestPlanetDbAccess:

    @mock.patch("api.db_access.planet_db_access.get_collection")
    def setup(self, mock_mongo):
        self.__mongo_collection = mock.MagicMock()
        mock_mongo.return_value = self.__mongo_collection
        self.__db_access = PlanetDbAccess()

    def test_should_call_add_planet(self):
        self.__mongo_collection.insert_one.return_value = "Ok"

        planet = {
            "name": "some_name",
            "climate": "some_climate",
            "terrain": "some_terrain",
            "movie_appearances_counter": "2"
        }
        result = self.__db_access.add_planet(planet)
        self.__mongo_collection.insert_one.assert_called_once_with({
            "name": "some_name",
            "climate": "some_climate",
            "terrain": "some_terrain",
            "movie_appearances_counter": "2"
        })
        assert result == "Ok"

    def test_should_call_find_planet(self):
        self.__mongo_collection.find.return_value = "Ok"
        result = self.__db_access.find_planets()
        self.__mongo_collection.find.assert_called_once()
        assert result == "Ok"

    def test_should_call_find_planet_by_name(self):
        self.__mongo_collection.find_one.return_value = "Ok"

        planet = {
            "name": "some_name",
            "climate": "some_climate",
            "terrain": "some_terrain",
            "movie_appearances_counter": "2"
        }
        result = self.__db_access.find_planet_by_name(planet["name"])
        self.__mongo_collection.find_one.assert_called_once_with(
            {"name": "some_name"})
        assert result == "Ok"

    @mock.patch("api.db_access.planet_db_access.ObjectId")
    def test_should_call_find_planet_by_id(self, mock_object_id):
        mock_object_id.return_value = "601ab571a317cbbbbbff820f"
        self.__mongo_collection.find_one.return_value = "Ok"
        result = self.__db_access.find_planet_by_id("601ab571a317cbbbbbff820f")
        mock_object_id.assert_called_once_with("601ab571a317cbbbbbff820f")
        self.__mongo_collection.find_one.assert_called_once_with(
            {"_id": "601ab571a317cbbbbbff820f"})
        assert result == "Ok"

    @mock.patch("api.db_access.planet_db_access.ObjectId")
    def test_should_call_delete_planet(self, mock_object_id):
        mock_object_id.return_value = "601ab571a317cbbbbbff820f"
        self.__mongo_collection.delete_one.return_value = "Ok"
        result = self.__db_access.delete_planet("601ab571a317cbbbbbff820f")
        mock_object_id.assert_called_once_with("601ab571a317cbbbbbff820f")
        self.__mongo_collection.delete_one.assert_called_once_with(
            {"_id": "601ab571a317cbbbbbff820f"})
        assert result == None
