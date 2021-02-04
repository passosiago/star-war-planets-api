import requests
import os


def build_search_url(planet_name):
    swapi_uri = os.environ.get("STAR_WARS_API")
    return f"{swapi_uri}?search={planet_name}"


def request_planet(planet_name):
    url = build_search_url(planet_name)
    response = requests.get(url)
    return response.json()


def enrich_planet_data(planet):
    result = request_planet(planet['name'])
    result = result["results"]
    if len(result) == 0:
        return 0
    planet_info = result[0]
    planet["movie_appearances_counter"] = len(planet_info['films'])
    return planet
