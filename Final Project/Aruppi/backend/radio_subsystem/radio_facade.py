"""
This file is a radio facade thar includes the important functions for te user.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from .radio import Radio, Station, Play, Pause
from .radio_dao import RadioDAO
from typing import List

class RadioFacade:
    """This class acts as a facade for the Radio class"""
    def __init__(self, stations: List[Station]):
        self.radio = Radio()
        self.radio_dao = RadioDAO(stations)
    
    def action(self):
        station = self.radio_dao.get_current_station()
        if station:
            self.radio.Action(station)
        else:
            raise ValueError("No current station set")

    def set_state(self, state):
        self.radio.set_state(state)

    def get_all_stations(self) -> List[Station]:
        return self.radio_dao.get_all_stations()

    def set_current_station(self, station_name: str) -> bool:
        return self.radio_dao.set_current_station(station_name)
