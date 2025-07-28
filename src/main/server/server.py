from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.conection import db_connection_handler
from src.main.routes.pets_routes import pet_route_bp

db_connection_handler.conect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(pet_route_bp, url_prefix="/api/v1")
