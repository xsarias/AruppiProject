"""
This file has some classes related with Radio States.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

from abc import ABC, abstractmethod


class RadioState(ABC):
    """This abstract class represent the actuals states of object"""

    @abstractmethod
    def action(self, station):
        """This abstract method represent an action inside radio"""


class Play(RadioState):
    """This class is play state of the object"""

    def action(self, station):
        print(f"The {station.name} is playing")


class Pause(RadioState):
    """This class is pause state of the object"""

    def action(self, station):
        print(f"The {station.name} is paused")
