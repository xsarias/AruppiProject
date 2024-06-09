"""
This is the main file for the Aruppi project (entry point).
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

from abc import ABC, abstractmethod

class CollectionStrategy(ABC):
    """
    This abstract class defines a strategy for adding items to a collection.
    Each concrete strategy must implement the add_to method.
    """
    @abstractmethod
    def add_to(self, anime_id):
        """Adds an anime to a collection."""  
    @abstractmethod
    def show_collection(self):
        """Shows collection content"""  

class FavoritesStrategy(CollectionStrategy):
    """
    Concrete strategy for adding an anime to the favorites collection.
    """
    def add_to(self, anime_id):
        pass
    def show_collection(self):
        pass

class RecommendedStrategy(CollectionStrategy):
    """
    Concrete strategy for adding an anime to the recommended collection.
    """
    def add_to(self, anime_id):
        print("Add to")
    def show_collection(self):
        pass

class QueueStrategy(CollectionStrategy):
    """
    Concrete strategy fir adding anime to queue.
    """
    def add_to(self, anime_id):
        pass
    def show_collection(self):
        pass
        