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
        description: str,
        category: str,
        anime_type: str,
        producer: str,
        episodes_amount: int,
        ):
        super().__init__(anime_id, description, category, anime_type, producer)
        self.episodes_amount=episodes_amount

class Movies(Anime):
    """This class represents the behavior of anime movies"""
    def __init__(
        self,
        anime_id: str,
        description: str,
        category: str,
        anime_type: str,
        producer: str,
        running_time:float,
        ):
        super().__init__(anime_id, description, category, anime_type, producer)
        self.running_time=running_time
class Ovas(Anime):
    """This class represents the behavior of anime OVA'S"""
    def __init__(
        self,
        anime_id: str,
        description: str,
        category: str,
        anime_type: str,
        producer: str,
        running_time:float,
        ):
        super().__init__(anime_id, description, category, anime_type, producer)
        self.running_time=running_time