"""
This module contains database connection parameters and creation tables.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_URL')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()
series = Table ("series",
                metadata,
                Column("anime_id", Integer(10), primary_key=True, autoincrement=True),
                Column("title", String(50)),
                Column("description", String(100)),
                Column("category", String(50)),
                Column("anime_type", String(50)),
                Column("producer", String(50)),
                Column("episodes_amount", Integer(10))
             )
movies = Table ("movies",
                metadata,
                Column("anime_id", Integer(10), primary_key=True, autoincrement=True),
                Column("title", String(50)),
                Column("description", String(50*2)),
                Column("category", String(50)),
                Column("anime_type", String(50)),
                Column("producer", String(50)),
                Column("running_time", Float(10))
                )
ovas = Table("ovas",
                metadata,
                Column("anime_id", Integer(10), primary_key=True, autoincrement=True),
                Column("title", String(50)),
                Column("description", String(100)),
                Column("category", String(50)),
                Column("anime_type", String(50)),
                Column("producer", String(50)),
                Column("episodes_amount", Integer(10))
            )
user = Table("user",
                metadata,
                Column("username", String(50), primary_key=True),
                Column("password", String(50)),
                Column("grants", String(50))
            )
station = Table("station",
                metadata,
                Column("station", String, primary_key=True),
                )
news = Table("news",
                metadata,
                Column("title", String, primary_key=True),
                Column("info", String)
            )
metadata.create_all(engine)