import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener las variables de entorno
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# Configurar la URL de conexión a la base de datos MySQL
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# Crear un objeto MetaData para definir las tablas
metadata = MetaData()

# Define the tables
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
    Column("station", String(50), primary_key=True)
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
# Crear las tablas en la base de datos
metadata.create_all(engine)

