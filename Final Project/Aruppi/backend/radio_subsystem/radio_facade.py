"""
This file is a radio facade thar includes the important functions for te user.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from backend.radio_subsystem.radio import Radio

class RadioFacade:
    """This class acts as a facade for the Radio class"""
    def __init__(self, station: str):
        self.radio = Radio(station)

    def play(self):
        """This method sets the state to Play and performs the action"""
        self.radio.play()

    def pause(self):
        """This method sets the state to Pause and performs the action"""
        self.radio.pause()

    def next(self):
        """This method sets the state to Next and performs the action"""
        self.radio.next()

    def previous(self):
        """This method sets the state to Previous and performs the action"""
        self.radio.previous()

# Ejemplo de uso
if __name__ == "__main__":
    radio_facade = RadioFacade("Station 1")
    print("start facade")
    radio_facade.play()     # La estación ya está en estado Play
    radio_facade.pause()    # Cambia el estado a Pause
    radio_facade.next()     # Cambia al siguiente estación y establece el estado a Play
    radio_facade.previous() # Cambia al estación anterior y establece el estado a Play
    radio_facade.pause()    # Cambia el estado a Pause
    radio_facade.play()     # Cambia el estado a Play
    print("end facade")