import pytest
import mock
from api.services.planet_services import PlanetService
import json

planets = [
    {
        "_id": {
            "$oid": "some_id"
        },
        "name": "some_name",
        "climate": "some_climate",
        "terrain": "some_terrain",
        "movie_appearances_counter": 1
    }
]

planet = {
    "_id": {
        "$oid": "some_id"
    },
    "name": "some_name",
    "climate": "some_climate",
    "terrain": "some_terrain",
    "movie_appearances_counter": 1
}


class TestPlanetServices:

    @mock.patch("api.services.planet_services.PlanetDbAccess")
    def test_should_call_find_planets(self, mock_db_access):

        mock_find_planets = mock.MagicMock()
        mock_db_access.return_value.find_planets = mock_find_planets
        mock_find_planets.return_value = planets
        service = PlanetService()
        result = service.get_planets()
        mock_find_planets.assert_called_once()
        assert result == json.dumps([
            {
                "_id": {
                    "$oid": "some_id"
                },
                "name": "some_name",
                "climate": "some_climate",
                "terrain": "some_terrain",
                "movie_appearances_counter": 1
            }
        ])

    @mock.patch("api.services.planet_services.PlanetDbAccess")
    def test_should_call_find_planet_by_name(self, mock_db_access):

        mock_find_planet_by_name = mock.MagicMock()
        mock_db_access.return_value.find_planet_by_name = mock_find_planet_by_name
        mock_find_planet_by_name.return_value = planet
        service = PlanetService()
        result = service.get_planet_by_name("some_name")
        mock_find_planet_by_name.assert_called_once_with(
            "some_name")
        assert result == json.dumps({
            "_id": {
                "$oid": "some_id"
            },
            "name": "some_name",
            "climate": "some_climate",
            "terrain": "some_terrain",
            "movie_appearances_counter": 1
        })

    @mock.patch("api.services.planet_services.PlanetDbAccess")
    def test_should_return_empty_object_when_find_planet_by_name_response_is_None(self, mock_db_access):

        mock_find_planet_by_name = mock.MagicMock()
        mock_db_access.return_value.find_planet_by_name = mock_find_planet_by_name
        mock_find_planet_by_name.return_value = None
        service = PlanetService()
        result = service.get_planet_by_name("some_name")
        mock_find_planet_by_name.assert_called_once_with(
            "some_name")
        assert result == {}

    @mock.patch("api.services.planet_services.PlanetDbAccess")
    def test_should_return_empty_object_when_find_planet_by_id_response_is_None(self, mock_db_access):

        mock_find_planet_by_id = mock.MagicMock()
        mock_db_access.return_value.find_planet_by_id = mock_find_planet_by_id
        mock_find_planet_by_id.return_value = None
        service = PlanetService()
        result = service.get_planet_by_id("some_id")
        mock_find_planet_by_id.assert_called_once_with(
            "some_id")
        assert result == {}

    @mock.patch("api.services.planet_services.PlanetDbAccess")
    def test_should_call_find_planet_by_id(self, mock_db_access):

        mock_find_planet_by_id = mock.MagicMock()
        mock_db_access.return_value.find_planet_by_id = mock_find_planet_by_id
        mock_find_planet_by_id.return_value = planet
        service = PlanetService()
        result = service.get_planet_by_id("some_id")
        mock_find_planet_by_id.assert_called_once_with(
            "some_id")
        assert result == json.dumps({
            "_id": {
                "$oid": "some_id"
            },
            "name": "some_name",
            "climate": "some_climate",
            "terrain": "some_terrain",
            "movie_appearances_counter": 1
        })

    @mock.patch("api.services.planet_services.PlanetDbAccess")
    def test_should_call_delete_planet_by_id(self, mock_db_access):

        mock_find_planet_by_id = mock.MagicMock()
        mock_delete_planet = mock.MagicMock()
        mock_db_access.return_value.find_planet_by_id = mock_find_planet_by_id
        mock_db_access.return_value.delete_planet = mock_delete_planet
        mock_find_planet_by_id.return_value = planet
        mock_delete_planet.return_value = None
        service = PlanetService()
        result = service.delete_planet_by_id("601ab2431731769ae20b8fba")
        mock_find_planet_by_id.assert_called_once_with(
            "601ab2431731769ae20b8fba")
        mock_delete_planet.assert_called_once_with("601ab2431731769ae20b8fba")

    @mock.patch("api.services.planet_services.PlanetDbAccess")
    def test_should_throw_exception_if_planet_does_not_exist_delete_planet_by_id(self, mock_db_access):

        mock_find_planet_by_id = mock.MagicMock()
        mock_delete_planet = mock.MagicMock()
        mock_db_access.return_value.find_planet_by_id = mock_find_planet_by_id
        mock_db_access.return_value.delete_planet = mock_delete_planet
        mock_find_planet_by_id.return_value = None
        mock_delete_planet.return_value = None
        service = PlanetService()
        try:
            result = service.delete_planet_by_id("601ab2431731769ae20b8fba")
        except Exception as e:
            mock_find_planet_by_id.assert_called_once_with(
                "601ab2431731769ae20b8fba")
            mock_delete_planet.assert_not_called

    @mock.patch("api.services.planet_services.PlanetDbAccess")
    @mock.patch("api.services.planet_services.enrich_planet_data")
    def test_should_call_create_planet(self, mock_enrich_data, mock_db_access):
        planet.pop("movie_appearances_counter")
        mock_find_planet_by_name = mock.MagicMock()
        mock_add_planet = mock.MagicMock()
        mock_enrich_data.return_value = {
            "_id": {
                "$oid": "some_id"
            },
            "name": "some_name",
            "climate": "some_climate",
            "terrain": "some_terrain",
            "movie_appearances_counter": 1
        }
        mock_db_access.return_value.find_planet_by_name = mock_find_planet_by_name
        mock_db_access.return_value.add_planet = mock_add_planet
        mock_find_planet_by_name.return_value = None
        mock_add_planet.return_value.inserted_id = "id"
        service = PlanetService()
        result = service.create_planet(planet)
        mock_find_planet_by_name.assert_called_once_with(
            "some_name")
        mock_add_planet.assert_called_once_with({
            "_id": {
                "$oid": "some_id"
            },
            "name": "some_name",
            "climate": "some_climate",
            "terrain": "some_terrain",
            "movie_appearances_counter": 1
        })
        assert result == {"_id": "id"}

    @ mock.patch("api.services.planet_services.PlanetDbAccess")
    def test_should_not_call_create_planet_if_planet_already_exist(self, mock_db_access):

        mock_find_planet_by_name = mock.MagicMock()
        mock_add_planet = mock.MagicMock()
        mock_db_access.return_value.find_planet_by_name = mock_find_planet_by_name
        mock_db_access.return_value.add_planet = mock_add_planet
        mock_find_planet_by_name.return_value = planet
        service = PlanetService()
        try:
            result = service.create_planet(planet)
        except Exception as e:
            mock_find_planet_by_name.assert_called_once_with(
                "some_name")
            mock_add_planet.assert_not_called
