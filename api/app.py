from flask import Flask

from api.routes.planets_routes import planet_blueprint

app = Flask(__name__)

app.register_blueprint(planet_blueprint)
