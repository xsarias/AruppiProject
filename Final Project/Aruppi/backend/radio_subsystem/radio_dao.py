"""
This module contains the DAO (Data Access Object) for managing radio data.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

from typing import List
from .radio import Station


class RadioDAO:
    """
    This class provides data access for managing station data.
    """

    def __init__(self, stations: List[Station]):
        """
        Initialize the RadioDAO object.
        Args:
            stations (List[Station]): A list of radio stations.
        """
        self.stations = stations
        self.current_station = None

    def get_all_stations(self) -> List[Station]:
        """
        Get all available radio stations.

        Returns:
            List[Station]: A list of all available radio stations.
        """
        return self.stations

    def set_current_station(self, station_name: str) -> bool:
        """
        Set the current radio station.

        Args:
            station_name (str): The name of the station to set as current.

        Returns:
            bool: True if the station was found and set as current, False otherwise.
        """
        for station in self.stations:
            if station.name == station_name:
                self.current_station = station
                return True
        return False

    def get_current_station(self) -> Station:
        """
        Get the current radio station.

        Returns:
            Station: The current radio station.
        """
        return self.current_station