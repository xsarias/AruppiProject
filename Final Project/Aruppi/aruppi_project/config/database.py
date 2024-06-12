"""
This module implements database connection and table creation.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, insert
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv



dotenv_path = os.path.join(os.path.dirname(__file__),'.env')
load_dotenv(dotenv_path)

# Obtener las variables de entorno
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')


global_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


engine = create_engine(global_DATABASE_URL)


metadata = MetaData()


series = Table("series", metadata,
    Column("anime_id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(50)),
    Column("description", String(100)),
    Column("category", String(50)),
    Column("anime_type", String(50)),
    Column("producer", String(50)),
    Column("episodes_amount", Integer)
)

movies = Table("movies", metadata,
    Column("anime_id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(50)),
    Column("description", String(100)),
    Column("category", String(50)),
    Column("anime_type", String(50)),
    Column("producer", String(50)),
    Column("running_time", Float)
)

ovas = Table("ovas", metadata,
    Column("anime_id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(50)),
    Column("description", String(100)),
    Column("category", String(50)),
    Column("anime_type", String(50)),
    Column("producer", String(50)),
    Column("running_time", Integer)
)

user = Table("user", metadata,
    Column("username", String(50), primary_key=True),
    Column("password", String(50)),
    Column("grants", String(50))
)

station = Table("station", metadata,
    Column("station", String(50), primary_key=True),
    Column("Name", String(50))
)

news = Table("news", metadata,
    Column("title", String(50), primary_key=True),
    Column("info", String(100))
)

queue = Table("queue", metadata,
    Column("username", String(50)),
    Column("anime_id", Integer)
)

recommended = Table("recommended", metadata,
    Column("username", String(50)),
    Column("anime_id", Integer)
)

favorites = Table("favorites", metadata,
    Column("username", String(50)),
    Column("anime_id", Integer)
)

metadata.create_all(engine)




anime_data = {
    "title": "Example Series",
    "description": "This is an example series.",
    "category": "Action",
    "anime_type": "Series",
    "producer": "Example Producer",
    "episodes_amount": 12
}


insert_statement = insert(series).values(anime_data)

try:
    with engine.connect() as conn:
        conn.execute(insert_statement)
except Exception as e:
    print("Ocurrió un error al insertar datos:", e)
