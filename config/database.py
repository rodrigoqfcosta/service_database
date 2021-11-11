import os
from dotenv import load_dotenv

load_dotenv()

database_infos = {
    "user": os.getenv('USER'),
    "password": os.getenv('PASSWORD'),
    "host": os.getenv('HOST'),
    "port": os.getenv('PORT'),
    "database": os.getenv('DATABASE'),
}
