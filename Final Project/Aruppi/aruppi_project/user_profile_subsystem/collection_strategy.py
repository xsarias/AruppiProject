""""
This module implemement strategies for user collections.
"""

from abc import ABC, abstractmethod


class CollectionStrategy(ABC):
    """
    This abstract class defines a strategy for adding items to a collection.
    Each concrete strategy must implement the add_to method.
    """

    def __init__(self):
        self.items = []

    @abstractmethod
    def add_to(self, anime_id):
        """Adds an anime to a collection."""

    def show_collection(self):
        """Shows collection content"""
        print(self.items)


class FavoritesStrategy(CollectionStrategy):
    """
    Concrete strategy for adding an anime to the favorites collection.
    """

    def add_to(self, anime_id):
        self.items.append(anime_id)
        print(f"{anime_id} added to Favorites")

    def show_collection(self):
        print("Favorites:", self.items)


class RecommendedStrategy(CollectionStrategy):
    """
    Concrete strategy for adding an anime to the recommended collection.
    """

    def add_to(self, anime_id):
        self.items.append(anime_id)
        print(f"{anime_id} added to Recommended")

    def show_collection(self):
        print("Recommended:", self.items)


class QueueStrategy(CollectionStrategy):
    """
    Concrete strategy for adding anime to queue.
    """

    def add_to(self, anime_id):
        self.items.append(anime_id)
        print(f"{anime_id} added to Queue")

    def show_collection(self):
        print("Queue:", self.items)
