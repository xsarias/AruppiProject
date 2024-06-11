"""
This file contains classes about anime types.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

from .anime import Anime


class Series(Anime):
    """This class represents the behavior of anime series"""

    def __init__(
        self,
        anime_id: str,
        title: str,
        description: str,
        category: str,
        anime_type: str,
        producer: str,
        episodes_amount: int,
    ):
        super().__init__(anime_id, title, description, category, anime_type, producer)
        self.episodes_amount = episodes_amount

    def get_details(self):
        """Returns detailed information about the series."""
        return (
            f"Title: {self.title}\n"
            f"ID: {self.anime_id}\n"
            f"Description: {self.description}\n"
            f"Category: {self.category}\n"
            f"Type: {self.anime_type}\n"
            f"Producer: {self.producer}\n"
            f"Episodes: {self.episodes_amount}\n"
            "-------------------------------------"
        )


class Movies(Anime):
    """This class represents the behavior of anime movies"""

    def __init__(
        self,
        anime_id: str,
        title: str,
        description: str,
        category: str,
        anime_type: str,
        producer: str,
        running_time: float,
    ):
        super().__init__(anime_id, title, description, category, anime_type, producer)
        self.running_time = running_time

    def get_details(self):
        """Returns detailed information about the movie."""
        return (
            f"Title: {self.title}\n"
            f"ID: {self.anime_id}\n"
            f"Description: {self.description}\n"
            f"Category: {self.category}\n"
            f"Type: {self.anime_type}\n"
            f"Producer: {self.producer}\n"
            f"Running Time: {self.running_time} minutes\n"
            "-------------------------------------"
        )


class Ovas(Anime):
    """This class represents the behavior of anime OVA'S"""

    def __init__(
        self,
        anime_id: str,
        title: str,
        description: str,
        category: str,
        anime_type: str,
        producer: str,
        running_time: float,
    ):
        super().__init__(anime_id, title, description, category, anime_type, producer)
        self.running_time = running_time

    def get_details(self):
        """Returns detailed information about the OVA."""
        return (
            f"Title: {self.title}\n"
            f"ID: {self.anime_id}\n"
            f"Description: {self.description}\n"
            f"Category: {self.category}\n"
            f"Type: {self.anime_type}\n"
            f"Producer: {self.producer}\n"
            f"Running Time: {self.running_time} minutes\n"
            "-------------------------------------"
        )
