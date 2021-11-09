from flask import Flask, request
from flask import jsonify
from flask_cors import CORS

import mariadb

app = Flask(__name__)
CORS(app)

@app.route('/connect_db')
def test_connect():
    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(user='root',
                               password='pass123',
                               host='localhost',
                               port=3307,
                               database='calculadora')
    except:
        return 'Error connecting to MariaDB'
    return 'Connecting to MariaDB OK'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
