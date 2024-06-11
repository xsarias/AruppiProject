"""
This file has some classes related to radio.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from .radio_state import RadioState, Play

class Station:
    """
    This class represent the station, its has states
    """

    def __init__(self, name):
        """
        initialize the class with a name of station.

        Args:
            name (str): station name.
        """
        self.name = name

    def next_station(self):
        """go to the next station"""

    def previous_station(self):
        """go to the previous station"""

class Radio:
    """
    This class is the context for the radio states.
    """

    def __init__(self):
        """Initializes the Radio object with a default state of Play."""
        self.state = Play()

    def action(self, station):
        """
        Performs an action based on the current state.

        Args:
            station: The current station object.
        """
        self.state.Action(self, station)

    def set_state(self, state: RadioState):
        """
        Sets the state of the radio.

        Args:
            state (RadioState): The state object to set.
        """
        self.state = state
