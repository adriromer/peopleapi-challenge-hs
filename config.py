import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import flask_sqlalchemy
#import yaml

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + os.getenv('MYSQL_USER')  + ':' + os.getenv('MYSQL_PASSWORD') + '@' + os.getenv('DB_HOSTNAME') + ':' + os.getenv('DB_PORT', '3306') + '/' + os.getenv('MYSQL_DATABASE')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_SIZE'] = os.getenv('DB_POOL', 200)
app.config['SQLALCHEMY_POOL_RECYCLE'] = os.getenv('DB_POOL_RECYCLE', 280)

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)
