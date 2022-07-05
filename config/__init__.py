from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values
import os

# Obtiene valores del .env
config = dotenv_values(".env")

host = 'localhost'

if os.environ.get('DOCKER_COMPOSE'):
    host = config['PSQL_HOST']

SQLALCHEMY_DATABASE_URL = "postgresql://{user}:{pasw}@{host}:{port}/{db}".format(
    user=config['PSQL_USER'],
    pasw=config['PSQL_ROOT_PASSWORD'],
    host=host,
    port=config['PSQL_PORT'],
    db=config['PSQL_DATABASE']
)

print(SQLALCHEMY_DATABASE_URL)

# Conexion a la BD
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear Sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea un Base de la base de datos
Base = declarative_base()
