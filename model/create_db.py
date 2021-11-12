import mysql.connector as mariadb
from config.database import database_infos

mariadb_connection = mariadb.connect(user=database_infos['user'],
                                    password=database_infos['password'],
                                    host=database_infos['host'],
                                    port=database_infos['port'],
                                    database=database_infos['database'])

my_cursor = mariadb_connection.cursor()

## CRIAR BANCO DE DADOS
my_cursor.execute("CREATE DATABASE calculadora")


### LISTAR BANCO DE DADOS EXISTENTES
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db) 

### LISTAR CONTEUDO DA DATABASE
#sql_statement = 'SELECT * FROM calculadora'
#my_cursor.execute(sql_statement)
#result = my_cursor.fetchall()
#print(result)
