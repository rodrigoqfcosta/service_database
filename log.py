from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://root:root@localhost:3307/calculadora'
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from controller.routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
