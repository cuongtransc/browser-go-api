import os
from database import db, ma

from flask import Flask

from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# ! Environment Variable
# TODO export CONFIGURATION_OBJECT='configuration.config.ProductionConfig'
app.config.from_object(os.getenv('CONFIGURATION_OBJECT'))

# ! Environment Variable
# TODO export ALLOWED_ORIGIN= whatever the react server is
# TODO cors_allowed_origins=os.getenv('ALLOWED_ORIGIN')
socketio = SocketIO(app, cors_allowed_origins=os.getenv('ALLOWED_ORIGIN'))

def create_app():
    CORS(app, resources={
        r"/api/*": {"origins": os.getenv('ALLOWED_ORIGIN')},
        r"/auth/*": {"origins": os.getenv('ALLOWED_ORIGIN')},
    })
    db.init_app(app)
    ma.init_app(app)

    return app
