"""
This module contains the DAO (Data Access Object) for managing radio data.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from typing import List
from .radio import Station

class RadioDAO:
    """This class provides data access for managing station data"""
    def __init__(self, stations: List[Station]):
        self.stations = stations
        self.current_station = None

    def get_all_stations(self) -> List[Station]:
        return self.stations

    def set_current_station(self, station_name: str) -> bool:
        for station in self.stations:
            if station.name == station_name:
                self.current_station = station
                return True
        return False

    def get_current_station(self) -> Station:
        return self.current_station