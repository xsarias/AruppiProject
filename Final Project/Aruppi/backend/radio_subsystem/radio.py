"""
This file has some classes related to radio.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from abc import ABC, abstractmethod

class RadioState(ABC):
    """This class provides the radio states"""
    @abstractmethod
    def play(self, radio):
        """This method defines the action to play the station"""

    @abstractmethod
    def pause(self, radio):
        """This method defines the action to pause the station"""

    @abstractmethod
    def next(self, radio):
        """This method defines the action to go to the next station"""

    @abstractmethod
    def previous(self, radio):
        """This method defines the action to go to the previous station"""

class Play(RadioState):
    """This class changes the state to play"""
    def play(self, radio):
        print("The station " + radio.station + " is already playing")
        return False
    def pause(self, radio):
        print("Pausing the station " + radio.station)
        radio.set_state(radio.pause_state)

    def next(self, radio):
        print("Skipping to the next station from " + radio.station)
        radio.station = "Next Station"  # Example logic for changing station
        radio.set_state(radio.play_state)

    def previous(self, radio):
        print("Going back to the previous station from " + radio.station)
        radio.station = "Previous Station"  # Example logic for changing station
        radio.set_state(radio.play_state)

class Pause(RadioState):
    """This class changes the state to pause"""
    def play(self, radio):
        print("Resuming the station " + radio.station)
        radio.set_state(radio.play_state)

    def pause(self, radio):
        print("The station " + radio.station + " is already paused")
        return False
    def next(self, radio):
        print("Skipping to the next station from " + radio.station)
        radio.station = "Next Station"  # Example logic for changing station
        radio.set_state(radio.play_state)

    def previous(self, radio):
        print("Going back to the previous station from " + radio.station)
        radio.station = "Previous Station"  # Example logic for changing station
        radio.set_state(radio.play_state)

class Radio:
    """This class represents the context of radio state"""

    def __init__(self, station) -> None:
        self.play_state = Play()
        self.pause_state = Pause()
        self.station = station
        self.state = self.play_state  # Default state

    def set_state(self, state: RadioState) -> None:
        """This method sets the state of the radio"""
        self.state = state

    def play(self):
        """This method sets the state to Play and performs the action"""
        self.state.play(self)

    def pause(self):
        """This method sets the state to Pause and performs the action"""
        self.state.pause(self)

    def next(self):
        """This method sets the state to Next and performs the action"""
        self.state.next(self)

    def previous(self):
        """This method sets the state to Previous and performs the action"""
        self.state.previous(self)

# Ejemplo de uso
