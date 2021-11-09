import mysql.connector as mariadb

mariadb_connection = mariadb.connect(host='localhost',
                                     user='root',
                                     password='pass123',
                                     port='3307')

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
