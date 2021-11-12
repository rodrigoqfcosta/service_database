# Micro-Serviço database
### Repositório exclusivo para o micro-serviço banco de dados MariaDB

O micro-serviço database possui a função de persistência dos dados no banco de dados MariaDB,
recebendo os parâmetros utilizados na GUI e retorno do serviço requisitado. 

### INICIALIZANDO MICRO-SERVIÇO:

Antes de iniciar o micro-serviço, certifique-se de habilitar o seu ambiente virtual (VENV):
###### MacOS/Linux:
```
$ source venv/bin/activate
```
###### Windows:
```
> venv\Scripts\activate
```

</br>Em seguida efetue a instalação dos requirements:
```
> pip install -r requirements.txt
```

</br>Após a instalação do requirements, crie na raiz do micro-serviço o arquivo .env com os seguintes parâmetros:
```
USER=<nome de usuário do banco>
PASSWORD=<senha do bando>
HOST=<local host do banco>
PORT=<porta utilizada do banco>
DATABASE=<nome do banco de dados>
```
Com o intuito de facilitar as coisas, a pasta model possui um script chamado create_db.py, execute o script:
```
> python create_db.py
```
Crie manualmente a tabela de log conforme o padrão da class Log, localizado no script entity_log.py

Feito isso, o micro-serviço estará pronto para ser executado :
```
> python log.py
```
