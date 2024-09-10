from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from src.models import db
from src.api import api

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.Config')
    
    db.init_app(app)
    CORS(app)
    app.register_blueprint(api)
    
    socketio.init_app(app)
    
    return app