"""
This module contains a Facade class that provides a simple interface to the complex logic about
Anime Subsystem.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

MENU="""
        ......   ...  .... ....... ....   ....  ........
        |  _  |  |  \ |  | |_   _| |   \ /   |  |  __  |
        | |_| |  |   \|  |   | |   |         |  |   ___|
        |  _  |  |       |  _| |_  |   |\/|  |  |  |___
        |_| |_|  |__|\___| |_____| |___|  |__|  |______|
                 >>> A R U P P I <<< 
        What do you want to do?
        1). Search Anime.
        2). Watch Series.
        3). Watch Movies.
        4). Watch Ovas's.
        5). Watch Especials.
        6). Back to principal menu.
        """
        
class AnimeFacade:
    """
    This class represents the Facade of Anime content
    """
    def __init__(self):
        pass
    
    def anime_menu(self):
        """This method shows the principal anime menu"""
        print(MENU)
        op=input(print("Please, select an option:"))
        if op=="1":
            pass
        elif op=="2":
            self.watch_anime("series")
        elif op=="3":
            self.watch_anime("movies")
        elif op=="4":
            self.watch_anime("ovas")
        elif op=="5":
            self.watch_anime("especials")
        elif op=="6":
            pass
    
    def watch_anime(self, anime_type:str):
        """This method asks the user about the type of content he/she want to watch"""

    def add__to_favorite(self):
        """This method lets users add anime content to their own favorite list """
    
    def add_to_queue(self):
        """This method lets users add anime content to their own queue list """
    
    def add_to_recommended(self):
        """This method lets users add anime content to their own recommended list """
    
    def search_anime(self):
        """This method lets user to find anime content,by diferent categories"""