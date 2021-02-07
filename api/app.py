from flask import Flask

from api.routes.planets_routes import planet_blueprint
from api.config.cache import cache
app = Flask(__name__)

app.register_blueprint(planet_blueprint)
cache.init_app(app)
