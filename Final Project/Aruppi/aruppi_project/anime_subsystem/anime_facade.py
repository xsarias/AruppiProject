"""
This module contains a Facade class that provides a simple interface to the complex logic
about Anime Subsystem.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

from .add_content_strategy import (
    AddMoviesAnime,
    AddOvasAnime,
    AddSeriesAnime,
    AddContentStrategy,
)
from .get_content_strategy import GetAnimeByCategory, GetAnimeByType, GetAnimeByTitle
from .anime_types import Movies, Ovas, Series


class AnimeFacade:
    """
    This class represents the Facade of Anime content.

    Methods:
        add_anime: Adds an anime to the database.
        search_anime_by_title: Searches for anime by title.
        search_anime_by_category: Searches for anime by category.
        search_anime_by_type: Searches for anime by type.
        watch_series: Retrieves and displays all series anime.
        watch_movies: Retrieves and displays all movies anime.
        watch_ovas: Retrieves and displays all OVAs anime.
        get_anime_info: Displays information of a specific anime.
    """

    def __init__(self):
        pass

    def add_anime_series(self, anime_data):
        """
        Adds an anime object to the anime list.

        Parameters:
        anime (Anime): The anime object to be added.
        """
        strategy = AddSeriesAnime()
        strategy.add_content(
            Series(
                anime_data["anime_id"],
                anime_data["title"],
                anime_data["description"],
                anime_data["category"],
                anime_data["anime_type"],
                anime_data["producer"],
                anime_data["episodes_amount"],
            )
        )
        return "Anime added successfully"

    def add_anime_ovas(self, anime_data):
        """
        Adds an anime object to the ovas data base.
        """
        strategy = AddOvasAnime()
        strategy.add_content(
            Ovas(
                anime_data["anime_id"],
                anime_data["title"],
                anime_data["description"],
                anime_data["category"],
                anime_data["anime_type"],
                anime_data["producer"],
                anime_data["running_time"],
            )
        )
        return "Anime added successfully"

    def add_anime_movies(self, anime_data):
        """
        Add an anime object to the movies data base
        """
        strategy = AddOvasAnime()
        strategy.add_content(
            Movies(
                anime_data["anime_id"],
                anime_data["title"],
                anime_data["description"],
                anime_data["category"],
                anime_data["anime_type"],
                anime_data["producer"],
                anime_data["running_time"],
            )
        )
        return "Movies added successfully"

    def search_anime_by_title(self, title):
        """
        Searches for anime by title.

        Parameters:
        title (str): The title to search for.

        Returns:
        list: A list of anime objects matching the title.
        """
        strategy = GetAnimeByTitle()
        return strategy.get_content(title)

    def search_anime_by_category(self, category):
        """
        Searches for anime by category.

        Parameters:
        category (str): The category to search for.

        Returns:
        list: A list of anime objects matching the category.
        """
        strategy = GetAnimeByCategory()
        return strategy.get_content(category)

    def search_anime_by_type(self, anime_type):
        """
        Searches for anime by type.

        Parameters:
        anime_type (str): The type to search for.

        Returns:
        list: A list of anime objects matching the type.
        """
        strategy = GetAnimeByType()
        return strategy.get_content(anime_type)
