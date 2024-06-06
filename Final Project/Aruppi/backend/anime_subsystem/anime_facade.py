"""
This module contains a Facade class that provides a simple interface to the complex logic about
Anime Subsystem.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

from .anime import Anime
from .anime_types import Series, Ovas, Specials, Movies
class AnimeFacade:
    """
    This class represents the Facade of Anime content.
    
    Methods:
        
    """
    def __init__(self):
        pass
    def watch_anime(self, anime_type:str):
        """This method asks the user about the type of content he/she want to watch"""
        return None
    def add__to_favorite(self):
        """This method lets users add anime content to their own favorite list """
        return None
    def add_to_queue(self):
        """This method lets users add anime content to their own queue list """
        return None
    def add_to_recommended(self):
        """This method lets users add anime content to their own recommended list """
        return None
    def search_anime_by_type(self):
        """This method lets user to find anime content by type"""
        return None
    def search_anime_by_tittle(self):
        """This method lets user to find anime content by tittle"""
        return None
    def search_anime_by_category(self):
        """This method lets user to find anime content by category"""
        return None