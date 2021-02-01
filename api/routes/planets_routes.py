from flask import Blueprint, request

planet_blueprint = Blueprint("planet_blueprint", __name__)

@planet_blueprint.route("/planets",  methods=['GET'])
def planets():
    return 'planets'