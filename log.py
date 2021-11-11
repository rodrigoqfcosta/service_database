from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config.database import database_infos

app = Flask(__name__)
CORS(app)

# Variaveis de ambiente database
user = database_infos['user']
password = database_infos['password']
host = database_infos['host']
port = database_infos['port']
database = database_infos['database']

# Define the MariaDB engine using MariaDB Connector/Python
engine = create_engine(f'mariadb+mariadbconnector://{user}:{password}@{host}:{port}/{database}')
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()                                         

from controller.routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
