from flask import Blueprint, request, Response
from flask.json import jsonify
from api.services.planet_services import PlanetService
from api.config.cache import cache

planet_blueprint = Blueprint("planet_blueprint", __name__)

service = PlanetService()


@planet_blueprint.route("/planets",  methods=['GET'])
@cache.cached(timeout=300)
def planets():
    print("teste Cache")
    planets = service.get_planets()
    return planets, 200


@planet_blueprint.route("/planets/<string:id>",  methods=['GET'])
@cache.cached(timeout=3600)
def planet_by_id(id):
    planet = service.get_planet_by_id(id)
    return planet, 200


@planet_blueprint.route("/planets/name/<string:name>",  methods=['GET'])
@cache.cached(timeout=3600)
def planet_by_name(name):
    planet = service.get_planet_by_name(name)
    return planet, 200


@planet_blueprint.route("/planets/<string:id>",  methods=['DELETE'])
def delete(id):
    service.delete_planet_by_id(id)
    return jsonify(), 204


@planet_blueprint.route("/planets",  methods=['POST'])
def add_planet():
    planet = request.json
    planet_id = service.create_planet(planet)
    return jsonify(planet_id), 201


@planet_blueprint.errorhandler(Exception)
def api_error_handler(error):
    return error.to_response()
