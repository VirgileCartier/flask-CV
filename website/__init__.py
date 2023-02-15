import os
import secrets
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secrets.token_hex(16)

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app 
