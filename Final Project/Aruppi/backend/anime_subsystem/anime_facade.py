"""
This module contains a Facade class that provides a simple interface to the complex logic about
Anime Subsystem.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

from .anime import Anime
from .anime_types import Series, Ovas, Specials, Movies

ANIME_MENU="""
        ......   ...  .... ....... ....   ....  ........
        |  _  |  |  \\ |  | |_   _| |   \\ /   |  |  __  |
        | |_| |  |   \\|  |   | |   |         |  |   ___|
        |  _  |  |       |  _| |_  |   |\ /|  |  |  |___
        |_| |_|  |__|\\___| |_____| |___|  |__|  |______|
                 >>> A R U P P I <<< 
        What do you want to do? 
        1). Search Anime.
        2). Watch Series.
        3). Watch Movies.
        4). Watch Ovas's.
        5). Watch Especials.
        6). Back to principal menu.
        """


def anime_menu():
    """This method shows the principal anime menu"""

    print(ANIME_MENU)
    op=input(print("Please, select an option:"))

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
    def get_user_profile(self)->dict:
        """This method get the user profile information"""