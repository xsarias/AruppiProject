"""
This module efines abstract classes for episode states and concrete implementations
for states such as watched and not watched.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""


from abc import ABC, abstractmethod

class EpisodeState(ABC):
    """This class provides the state of every series' episodes"""
    @abstractmethod
    def watch(self, episode: int):
        """This method transitions the episode to a watched state"""

class NotWatched(EpisodeState):
    """This class changes the state to not watched to watched"""
    def watch(self, episode):
        """This method marks the episode as watched"""
        print("Watch the episode number " + str(episode))
        return Watched()

class Watched(EpisodeState):
    """This class provides the watched status of an episode"""
    def watch(self, episode):
        """This method notifies that the episode is already watched"""
        print("Episode number " + str(episode) + " is already watched")

class Episode:
    """This class represents an episode of an anime series"""
    def __init__(self, episode):
        """Initializes an episode with a given number"""
        self.episode = episode
        # Initial episode state
        self.state = NotWatched()

    def watch(self):
        """Transitions the episode to a watched state"""
        self.state = self.state.watch(self.episode)


# Example usage:
# Creating an episode
episode1 = Episode(1)

# Watching the episode
episode1.watch()

# Trying to watch the same episode again
episode1.watch()