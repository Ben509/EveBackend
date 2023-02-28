from flask import Flask
from pymongo import MongoClient
from auth import auth as auth_blueprint
from main import main as main_blueprint
from flask_login import LoginManager

app = Flask(__name__)

client = MongoClient('172.22.58.1', 27017)

app.config['SECRET_KEY'] = 'secret-key-goes-here'

login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)

