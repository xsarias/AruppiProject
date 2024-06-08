"""
This file is a radio facade thar includes the important functions for te user.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from .radio import Radio
RADIO_MENU="""
        ......   ....... .......   ..........  ......... 
        |  _  \\  |  _  | |   _  \\  |__    __|  |  __   |
        | |_|  | | |_| | |  | \\  |    |  |     |  | |  |
        |     /  |  _  | |  |_/  |  __|  |__   |  |_|  |
        |__|\\_\\  |_| |_| |______/  |________|  |_______|
                 >>> A R U P P I <<< 
        What do you want to do? 
        1). Search Anime.
        2). Watch Series.
        3). Watch Movies.
        4). Watch Ovas's.
        5). Watch Especials.
        6). Back to principal menu.
        """


def radio_menu():
    """This method shows the principal radio menu"""

    print(RADIO_MENU)
    op=input(print("Please, select an option:"))
    print(op)
    
class RadioFacade:
    """This class acts as a facade for the Radio class"""
    def __init__(self, station: str):
        self.radio = Radio(station)

    def play(self):
        """This method sets the state to Play and performs the action"""
        self.radio.play()

    def pause(self):
        """This method sets the state to Pause and performs the action"""
        self.radio.pause()

    def next(self):
        """This method sets the state to Next and performs the action"""
        self.radio.next()

    def previous(self):
        """This method sets the state to Previous and performs the action"""
        self.radio.previous()
    
