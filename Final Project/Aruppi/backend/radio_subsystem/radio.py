"""
This file has some classes related to radio.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

class Radio:
    """This class represent the context of radio state"""

    def __init__(self, station:str) -> None:
        self.station=station
        self._state=Play(self)

    def ChangeState(self,state):
        """This method define the changes of state"""
        self.state=state
