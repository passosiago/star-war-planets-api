import pytest
import mock
from api.helpers.swapi_helper import build_search_url, request_planet, enrich_planet_data


class TestSwapiHelper:

    @mock.patch("api.helpers.swapi_helper.os")
    def test_should_return_correct_url(self, mock_os):
        mock_os.environ = {
            "STAR_WARS_API": "teste_url"
        }
        url = build_search_url("Tatooine")
        # mock_os.getenv.assert_called_with("STAR_WARS_API")
        assert url == f"teste_url?search=Tatooine"

    @mock.patch("api.helpers.swapi_helper.request_planet")
    def test_should_return_planet_with_appearances_counter_propertie(self, mock_req_planet):
        mock_req_planet.return_value = {
            "results": [{
                "films": [
                    "film1", "film2"
                ]
            }]}
        planet = {
            "name": "some_name",
            "terrain": "some_terrain",
            "climate": "some_climate"
        }

        updated_planet = enrich_planet_data(planet)
        assert updated_planet == {
            "name": "some_name",
            "terrain": "some_terrain",
            "climate": "some_climate",
            "movie_appearances_counter": 2
        }

    @mock.patch("api.helpers.swapi_helper.requests.get")
    @mock.patch("api.helpers.swapi_helper.build_search_url")
    def test_should_request_with_correct_url(self, mock_url_builder, mock_requests):
        mock_url_builder.return_value = "https://swapi.dev/api/planets/?search=Tatooine"
        request_planet("Tatooine")
        mock_requests.assert_called_once_with(
            "https://swapi.dev/api/planets/?search=Tatooine")
