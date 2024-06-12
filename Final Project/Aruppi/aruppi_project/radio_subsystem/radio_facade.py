"""
This file is a radio facade thar includes the important functions for te user.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

from typing import List
from .radio import Radio, Station
from .radio_dao import RadioDAO


class RadioFacade:
    """
    This class acts as a facade for the Radio class.
    """

    def __init__(self, stations: List[Station]):
        """
        Initialize the RadioFacade object.

        Args:
            stations (List[Station]): A list of radio stations.
        """
        self.radio = Radio()
        self.radio_dao = RadioDAO(stations)

    def action(self):
        """
        Perform an action on the current radio station.

        Raises:
            ValueError: If no current station is set.
        """
        station = self.radio_dao.get_current_station()
        if station:
            self.radio.action(station)
        else:
            raise ValueError("No current station set")

    def set_state(self, state):
        """
        Set the state of the radio.

        Args:
            state: The state to set for the radio.
        """
        self.radio.set_state(state)

    def get_all_stations(self) -> List[Station]:
        """
        Get all available radio stations.

        Returns:
            List[Station]: A list of all available radio stations.
        """
        return self.radio_dao.get_all_stations()

    def set_current_station(self, station_name: str) -> bool:
        """
        Set the current radio station.

        Args:
            station_name (str): The name of the station to set as current.

        Returns:
            bool: True if the station was found and set as current, False otherwise.
        """
        return self.radio_dao.set_current_station(station_name)
