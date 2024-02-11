from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os


app = Flask(__name__)


app.config['SECRET_KEY'] = '8dc7e344a750a3ca9f038a9d2946d311'
if os.getenv("DATABASE_URL"):
  app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else: 
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///IB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'


from comunidadeimpressionadora import routes
