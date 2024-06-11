"""
This module contains database connection parameters and creation tables.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

from sqlalchemy import create_engine, MetaData
import os


MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

URL_CONNECTION = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_ROOT_PASSWORD}@{MYSQL_HOST}:3306/{MYSQL_DATABASE}"

meta = MetaData()

engine = create_engine(URL_CONNECTION)
conn = engine.connect()