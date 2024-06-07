"""
This module contains differents types of anime content.
This abstrac class represent all types of anime in the application.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

from abc import ABC


class Anime(ABC):
    """
    This class represent anime behaviors in the apllication.

    Args:
        description (str): A brief summary of the anime's plot or storyline.
        category (str): The genre or genres the anime belongs to (e.g., action, romance, sci-fi).
        type (str): The format of the anime, such as OVA, movie, or series.
        episodes_amount (int): The total number of episodes in the anime.
        producer (str): The company or studio responsible for creating the anime.

    """

    def __init__(
        self,
        anime_id: str,
        description: str,
        category: str,
        anime_type:str,
        producer: str,
    ):
        self.anime_id=anime_id
        self.description = description
        self.category = category
        self.anime_type = anime_type
        self.producer = producer

    def is_category(self, category):
        """this method return if the category anime has the same one."""
        return self.category==category
    

        