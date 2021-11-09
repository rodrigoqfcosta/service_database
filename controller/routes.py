from log import app
from flask import render_template
from flask import jsonify

import mariadb
from model.tabela import Log


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


@app.route('/select')
def select_db():
    lista=[]
    calculos = Log.query.all()
    for linha in calculos:
        lista.append(f'Data e hora: {linha.data_oper} - Tipo da operação: {linha.tipo_oper} - Operação: {linha.operacao} - Argumento utilizado: {linha.args}')
    lista_parsed = {'result': lista}
    return jsonify(lista_parsed)


@app.route('/insert')
def insert_db():
    ...
