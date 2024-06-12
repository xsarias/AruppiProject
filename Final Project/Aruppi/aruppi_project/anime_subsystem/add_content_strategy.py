"""
This module implements strategies to get japanese culture content.
"""

from abc import ABC, abstractmethod
from .anime_dao import AnimeDAO
from .anime_types import Series, Movies, Ovas


class AddContentStrategy(ABC):
    """
    This abstract class defines the strategy interface for adding anime content.
    """

    @abstractmethod
    def add_content(self, content):
        """Add content"""


class AddMoviesAnime(AddContentStrategy):
    """
    Concrete strategy for adding movies.
    """

    def add_content(self, content:Movies):
        AnimeDAO.add_movies(content)


class AddOvasAnime(AddContentStrategy):
    """
    Concrete strategy for adding OVAs.
    """

    def add_content(self, content: Ovas):
        AnimeDAO.add_ovas(content)


class AddSeriesAnime(AddContentStrategy):
    """
    Concrete strategy for adding series.
    """

    def add_content(self, content: Series):
        AnimeDAO.add_series(content)