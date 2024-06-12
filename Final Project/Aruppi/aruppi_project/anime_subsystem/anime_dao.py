"""
This module contains the DAO (Data Access Object) for managing anime data.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
from ..config import engine, movies, ovas, series
Session = sessionmaker(bind=engine)



class AnimeDAO:
    """
    This class provides data access methods for managing anime data.
    """

    @classmethod
    def add_series(cls, anime):
        """
        Adds an anime object to the respective table.

        Parameters:
        anime: The anime object to be added.
        """
        series_data = {
            "title": anime.title,
            "description": anime.description,
            "category": anime.category,
            "anime_type": anime.anime_type,
            "producer": anime.producer,
            "episodes_amount": anime.episodes_amount,
        }
        session = Session()
        try:
            session.execute(series.insert().values(series_data))
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error inserting series: {e}")
        finally:
            session.close()

    @classmethod
    def add_movies(cls, anime):
        """
        Adds an anime object to the respective table.

        Parameters:
        anime: The anime object to be added.
        """
        movies_data = {
            "title": anime.title,
            "description": anime.description,
            "category": anime.category,
            "anime_type": anime.anime_type,
            "producer": anime.producer,
            "running_time": anime.running_time,
        }
        session = Session()
        try:
            session.execute(movies.insert().values(movies_data))
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error inserting series: {e}")
        finally:
            session.close()

    @classmethod
    def add_ovas(cls, anime):
        """
        Adds an anime object to the respective table.

        Parameters:
        anime: The anime object to be added.
        """
        
        ovas_data = {
            "title": anime.title,
            "description": anime.description,
            "category": anime.category,
            "anime_type": anime.anime_type,
            "producer": anime.producer,
            "running_time": anime.running_time,
        }
        session = Session()
        try:
            session.execute(ovas.insert().values(ovas_data))
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error inserting series: {e}")
        finally:
            session.close()

    @classmethod
    def get_content(cls, title):
        """
        Retrieves anime objects that match the given title.

        Parameters:
        title (str): The title to search for.

        Returns:
        list: A list of anime objects matching the title.
        """
        results = []
        with engine.connect() as conn:
            for table in [series, ovas, movies]:
                query = select([table]).where(table.c.title.ilike(f"%{title}%"))
                result_set = conn.execute(query).fetchall()
                # Convertir cada fila del resultado en un diccionario y agregarlo a los resultados
                for row in result_set:
                    anime_dict = dict(row)
                    results.append(anime_dict)
        return results

    @classmethod
    def get_anime_by_category(cls, category):
        """
        Retrieves anime objects that match the given category.

        Parameters:
        category (str): The category to search for.

        Returns:
        list: A list of anime objects matching the category.
        """
        results = []
        with engine.connect() as conn:
            for table in [series, ovas, movies]:
                query = select([table]).where(table.c.category.ilike(f"%{category}%"))
                results.extend(conn.execute(query).fetchall())
        return results

    @classmethod
    def get_anime_by_type(cls, anime_type):
        """
        Retrieves anime objects that match the given type.

        Parameters:
        anime_type (str): The type to search for.

        Returns:
        list: A list of anime objects matching the type.
        """
        results = []
        with engine.connect() as conn:
            for table in [series, ovas, movies]:
                query = select([table]).where(
                    table.c.anime_type.ilike(f"%{anime_type}%")
                )
                results.extend(conn.execute(query).fetchall())
        return results
