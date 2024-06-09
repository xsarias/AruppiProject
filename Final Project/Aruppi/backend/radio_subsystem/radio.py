"""
This file has some classes related to radio.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from abc import ABC, abstractmethod

class RadioState(ABC):
    """This abstract class represent the actuals states of object"""

    @abstractmethod
    def Action(self,radio,station):
        pass

class Play(RadioState):
    """This class is play state of the object"""

    def Action(self, radio, station):
        print(f"The {station.name} is playing")

class Pause(RadioState):
    """This class is pause state of the object"""
    def Action(self, radio, station):
        print(f"The {station.name} is paused")


class Station:
    """This class defines the object that has states"""

    def __init__(self):
        self.name="Olympica"

    def Next_station(self):
        pass
    def Previous_station(self):
        pass
class Radio:
    """This class is the context of the radio states"""
    def __init__(self):
        self.state=Play()       

    def Action(self, station):
        self.state.Action(self, station)

    def set_state(self, state:RadioState):
        self.state=state
