from flask import jsonify, request
from log import app

@app.route('/')
def list_all():
    from model.entity_log import Log

    lista=[]
    calculos = Log.query.all()
    for linha in calculos:
        lista.append(f'Data e hora: {linha.data_oper} - Tipo da operação: {linha.tipo_oper} - Operação: {linha.operacao} - Argumento utilizado: {linha.args}')

    lista_parsed = {'result': lista}
    return jsonify(lista_parsed)


""" @app.route('/cadastrar', methods=['POST'])
def list_all($):
    int_input_1 = request.getJ
    int_input_2 = request.args.get('arg2', type=int)
    int_output = {'result': (int_input_1 + int_input_2)}
    return jsonify(int_output) """


@app.route('/connect_db')
def test_connect():
    # Connect to MariaDB Platform
    try:
        conn = mariadb.connect(user='root',
                               password='root',
                               host='localhost',
                               port=3307,
                               database='calculadora')
    except:
        return 'Error connecting to MariaDB'
    return 'Connecting to MariaDB OK'