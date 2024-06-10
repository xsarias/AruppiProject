"""
This module contains a Facade class that provides a simple interface to the complex logic
about Anime Subsystem.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

from .anime_dao import AnimeDAO


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
        self.dao = AnimeDAO()

    def add_anime(self, anime):
        """
        Adds an anime object to the anime list.

        Parameters:
        anime (Anime): The anime object to be added.
        """
        self.dao.add_anime(anime)
        return "okey"

    def search_anime_by_title(self, title):
        """
        Searches for anime by title.

        Parameters:
        title (str): The title to search for.

        Returns:
        list: A list of anime titles matching the title.
        """
        return [anime.title for anime in self.dao.get_anime_by_title(title)]

    def search_anime_by_category(self, category):
        """
        Searches for anime by category.

        Parameters:
        category (str): The category to search for.

        Returns:
        list: A list of anime titles matching the category.
        """
        return [anime.title for anime in self.dao.get_anime_by_category(category)]

    def search_anime_by_type(self, anime_type):
        """
        Searches for anime by type.

        Parameters:
        anime_type (str): The type of anime to search for.

        Returns:
        list: A list of anime titles matching the type.
        """
        return [anime.title for anime in self.dao.get_anime_by_type(anime_type)]

    def watch_series(self):
        """
        Retrieves and displays all series anime.
        """
        series_titles = self.search_anime_by_type("series")
        print("Series Available:")
        for i, title in enumerate(series_titles, start=1):
            print(f"{i}. {title}")
        selection = int(
            input("Select a series to view details (enter number): ").strip()
        )
        self.get_anime_info(series_titles[selection - 1])

    def watch_movies(self):
        """
        Retrieves and displays all movies anime.
        """
        movies_titles = self.search_anime_by_type("movies")
        print("Movies Available:")
        for i, title in enumerate(movies_titles, start=1):
            print(f"{i}. {title}")
        selection = int(
            input("Select a movie to view details (enter number): ").strip()
        )
        self.get_anime_info(movies_titles[selection - 1])

    def watch_ovas(self):
        """
        Retrieves and displays all OVAs anime.
        """
        ovas_titles = self.search_anime_by_type("ovas")
        print("OVAs Available:")
        for i, title in enumerate(ovas_titles, start=1):
            print(f"{i}. {title}")
        selection = int(input("Select an OVA to view details (enter number): ").strip())
        self.get_anime_info(ovas_titles[selection - 1])

    def get_anime_info(self, title):
        """
        Displays all information of a specific anime.

        Parameters:
        title (str): The title of the anime whose information is to be displayed.
        """
        anime_found = self.dao.get_anime_by_title(title)
        if anime_found:
            anime = anime_found[
                0
            ]  # Assuming titles are unique and we take the first match
            print("Anime Information:")
            print(anime.get_details())
        else:
            print(f"No anime found with the title '{title}'.")
