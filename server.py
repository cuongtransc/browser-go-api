from app import create_app, db
import os

# Blueprints
from api.api import register_api_endpoints
from auth.auth import auth

# Web sockets
from websockets.socket import socketio

import configuration.models_mount
from flask_migrate import Migrate

from flask import Blueprint, jsonify
import psycopg2

server = Blueprint('server', __name__, url_prefix='/')


@server.route('/', methods=['GET'])
def api_home():
    response = {"message": "hello world"}
    return jsonify(response)


app = create_app()
register_api_endpoints(app)
app.register_blueprint(server)

migrate = Migrate(app, db)

# # added 10/14
# DATABASE_URL = os.environ['DATABASE_URL']
# # conn = psycopg2.connect(DATABASE_URL, sslmode='require')
# conn = psycopg2.connect(DATABASE_URL)

if __name__ == '__main__':
    socketio.run(app, debug=True)
