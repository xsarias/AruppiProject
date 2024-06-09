"""
This module contains the DAO (Data Access Object) for managing anime data.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

class AnimeDAO:
    """
    This class provides data access methods for managing anime data.
    
    Methods:
        add_anime: Adds an anime object to the list.
        get_anime_by_title: Retrieves anime objects that match the given title.
        get_anime_by_category: Retrieves anime objects that match the given category.
        get_anime_by_type: Retrieves anime objects that match the given type.
    """
    
    def __init__(self):
        self.anime_list = []

    def add_anime(self, anime):
        """
        Adds an anime object to the list.

        Parameters:
        anime (Anime): The anime object to be added.
        """
        self.anime_list.append(anime)

    def get_anime_by_title(self, title):
        """
        Retrieves anime objects that match the given title.

        Parameters:
        title (str): The title to search for.

        Returns:
        list: A list of anime objects matching the title.
        """
        return [anime for anime in self.anime_list if title.lower() in anime.title.lower()]

    def get_anime_by_category(self, category):
        """
        Retrieves anime objects that match the given category.

        Parameters:
        category (str): The category to search for.

        Returns:
        list: A list of anime objects matching the category.
        """
        return [anime for anime in self.anime_list if category.lower() in anime.category.lower()]

    def get_anime_by_type(self, anime_type):
        """
        Retrieves anime objects that match the given type.

        Parameters:
        anime_type (str): The type to search for.

        Returns:
        list: A list of anime objects matching the type.
        """
        return [anime for anime in self.anime_list if anime.anime_type.lower() == anime_type.lower()]
