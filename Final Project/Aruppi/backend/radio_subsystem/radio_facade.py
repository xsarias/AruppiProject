"""
This file is a radio facade thar includes the important functions for te user.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from .radio import Radio

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
<<<<<<< HEAD
    
=======


# Ejemplo de uso
>>>>>>> ec2ecf67562ae228c807ce4c4107be8cab5580e4
