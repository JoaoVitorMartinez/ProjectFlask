from http.client import ImproperConnectionState


import os

SECRET_KEY = "asdhiadpjkqw"
SQLALCHEMY_DATABASE_URI =\
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'Mudar123',
        servidor = 'localhost',
        database = 'jogoteca'
    )
    
# SQLALCHEMY_TRACK_MODIFICATIONS = True

IMG_PATH =  os.path.dirname(os.path.abspath(__file__)) + '/img'
