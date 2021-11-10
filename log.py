from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
CORS(app)

engine = create_engine('mariadb+mariadbconnector://root:root@localhost:3307/calculadora')
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()                                         

from controller.routes import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
