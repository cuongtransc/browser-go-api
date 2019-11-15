from flask import Blueprint, request, jsonify, session
from .users.api_users import api_users
from .rooms.api_rooms import api_rooms
from .games.api_games import api_games

from auth.auth import auth

api = Blueprint('api', __name__, url_prefix='/api')

def register_api_endpoints(app):
    app.register_blueprint(api_users)
    app.register_blueprint(api_rooms)
    app.register_blueprint(api_games)
    app.register_blueprint(api)
    app.register_blueprint(auth)

    return app

@api.route('/home', methods=['GET'])
def api_home():
    response = {"message": "home page"}
    return jsonify(response)


