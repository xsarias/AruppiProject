"""Expose classes of the subsystem user_profile_subsystem."""
from .collection import Collection, CollectionStrategy
from .collection_strategy import FavoritesStrategy, RecommendedStrategy, QueueStrategy
from .user import User