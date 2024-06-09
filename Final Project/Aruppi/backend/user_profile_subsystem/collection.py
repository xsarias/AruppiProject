"""
This is a main file of Aruppi project (initial point).
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

from .collection_strategy import CollectionStrategy

class Collection:
    """
    Represents a collection of items managed by a specific strategy.

    Args:
        strategy (CollectionStrategy): The strategy used to manage the collection.
    """
    def __init__(self, strategy: CollectionStrategy):
        """
        Initializes a Collection instance with a given strategy.

        Args:
            strategy (CollectionStrategy): The strategy used to manage the collection.
        """
        self.strategy = strategy

    def set_strategy(self, strategy: CollectionStrategy):
        """
        Sets a new strategy for managing the collection.

        Args:
            strategy (CollectionStrategy): The new strategy to be set.
        """
        self.strategy = strategy

    def add_to_collection(self, anime_id):
        """
        Adds an item to the collection using the current strategy.

        Args:
            anime_id: The ID of the anime to be added to the collection.
        """
        self.strategy.add_to(anime_id)

    def show_collection(self):
        """
        Displays the contents of the collection.
        """
