"""
This module contains different types of anime content.
This abstract class represents all types of anime in the application.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

from abc import ABC, abstractmethod


class Anime(ABC):
    """
    This class represents anime behaviors in the application.

    Args:
        anime_id (str): Unique identifier for the anime.
        title (str): Title of the anime.
        description (str): A brief summary of the anime's plot or storyline.
        category (str): The genre or genres the anime belongs to (e.g., action, romance, sci-fi).
        anime_type (str): The format of the anime, such as OVA, movie, or series.
        producer (str): The company or studio responsible for creating the anime.
    """

    def __init__(
        self,
        anime_id: str,
        title: str,
        description: str,
        category: str,
        anime_type: str,
        producer: str,
    ):
        self.anime_id = anime_id
        self.title = title
        self.description = description
        self.category = category
        self.anime_type = anime_type
        self.producer = producer

    def is_category(self, category):
        """
        This method checks if the anime belongs to the specified category.

        Parameters:
        category (str): The category to check.

        Returns:
        bool: True if the anime belongs to the specified category, False otherwise.
        """
        return self.category.lower() == category.lower()

    def is_type(self, anime_type):
        """
        This method checks if the anime is of the specified type.

        Parameters:
        anime_type (str): The type to check.

        Returns:
        bool: True if the anime is of the specified type, False otherwise.
        """
        return self.anime_type.lower() == anime_type.lower()

    def is_title(self, title):
        """
        This method checks if the anime title matches the specified title.

        Parameters:
        title (str): The title to check.

        Returns:
        bool: True if the anime title matches the specified title, False otherwise.
        """
        return self.title.lower() == title.lower()

    @abstractmethod
    def get_details(self):
        """
        This Abstract method to get the details of the anime. Must be implemented by subclasses.

        Returns:
        str: A string representation of the anime details.
        """
