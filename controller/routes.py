import sqlalchemy
from log import app, engine
from flask import render_template, jsonify, request

import mariadb
from model.entity_log import Log
from datetime import datetime


@app.route('/')
def list_all():
    lista=[]
    calculos = Log.query.all()
    for linha in calculos:
        lista.append(f'Data e hora: {linha.data_oper} - Tipo da operação: {linha.tipo_oper} - Operação: {linha.operacao} - Argumento utilizado: {linha.args}')

    lista_parsed = {'result': lista}
    return jsonify(lista_parsed)


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    content = request.json
    print(content)

    tipo_oper = content["tipo_oper"]
    operacao = content["operacao"]
    args = content["args"]

    newLog = Log(tipo_oper, operacao, args)

    Session = sqlalchemy.orm.sessionmaker()
    Session.configure(bind=engine)
    Session = Session()

    Session.add(newLog)
    Session.commit()

    return "Sucesso"


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
