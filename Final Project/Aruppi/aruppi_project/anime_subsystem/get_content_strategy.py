"""
This module implements strategies to get japanese culture content.
"""

from abc import ABC, abstractmethod
from .anime_dao import AnimeDAO
class GetContentStrategy(ABC):
    """
    This abstract class defines the strategy interface for getting anime content.
    """

    @abstractmethod
    def get_content(self, search_parameter):
        """Get content"""


class GetAnimeByTitle(GetContentStrategy):
    """
    Concrete strategy for getting an anime by title.
    """
    def get_content(self, search_parameter):
        return AnimeDAO.get_content(search_parameter)

class GetAnimeByCategory(GetContentStrategy):
    """
    Concrete strategy for getting anime by category.
    """
    def get_content(self, search_parameter):
        return AnimeDAO.get_anime_by_category(search_parameter)

class GetAnimeByType(GetContentStrategy):
    """
    Concrete strategy for getting anime by type.
    """
    def get_content(self, search_parameter):
        return AnimeDAO.get_anime_by_type(search_parameter)

class GetNews(GetContentStrategy):
    """
    Concrete strategy for get news
    """
    def get_content(self, search_parameter):
        pass

class GetRadioStation(GetContentStrategy):
    """
    Concrete strategy for get radio station
    """
    def get_content(self, search_parameter):
        pass
