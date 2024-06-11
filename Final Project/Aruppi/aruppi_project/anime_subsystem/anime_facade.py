"""
This module contains a Facade class that provides a simple interface to the complex logic
about Anime Subsystem.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from .add_content_strategy import AddMoviesAnime, AddOvasAnime, AddSeriesAnime
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

    def add_anime(self, anime):
        """
        Adds an anime object to the anime list.

        Parameters:
        anime (Anime): The anime object to be added.
        """
        if isinstance(anime, Movies):
            strategy = AddMoviesAnime()
        elif isinstance(anime, Ovas):
            strategy = AddOvasAnime()
        elif isinstance(anime, Series):
            strategy = AddSeriesAnime()
        else:
            raise ValueError("Unknown anime type")

        strategy.add_content(anime)
        return "Anime added successfully"

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
