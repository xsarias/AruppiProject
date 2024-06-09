"""
This file is a radio facade thar includes the important functions for te user.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from .radio import Radio, Station

class RadioFacade:
    """This class acts as a facade for the Radio class"""
    def __init__(self):
        self.radio=Radio()
        self.station=Station()
    
    def Action(self, station):
        """"""
        self.radio.Action(station)
    def set_state(self, state):
        self.radio.set_state(state)
    def Next_station(self):
        pass
    def Previous_station(self):
        pass
    
