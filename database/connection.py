from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .information import SQLALCHEMY_DATABASE_URL1, SQLALCHEMY_DATABASE_URL2

data_engine = create_engine(
    SQLALCHEMY_DATABASE_URL1
)

scada_engine = create_engine(
    SQLALCHEMY_DATABASE_URL2
)

DataSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=data_engine)
ScadaSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=scada_engine)

DataBase = declarative_base(bind=data_engine)
ScadaBase = declarative_base(bind=scada_engine)
