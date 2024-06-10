import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql+psycopg2://aruppiuser:aruppipassword@db/aruppi')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
