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

    @abstractmethod
    def get_details(self):
        """
        This Abstract method to get the details of the anime. Must be implemented by subclasses.

        Returns:
        str: A string representation of the anime details.
        """
