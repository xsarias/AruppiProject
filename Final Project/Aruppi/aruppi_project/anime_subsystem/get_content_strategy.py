"""
This module implements strategies to get japanese culture content.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from abc import ABC, abstractmethod
from .anime_dao import AnimeDAO


class GetContentStrategy(ABC):
    """
    This abstract class defines the strategy interface for getting anime content.
    """

    @abstractmethod
    def get_content(self, search_parameter):
        """This method get content anime"""


class GetAnimeByTitle(GetContentStrategy):
    """
    This method concrete strategy for getting an anime by title.
    """

    def get_content(self, search_parameter):
        return AnimeDAO.get_anime_by_title(search_parameter)


class GetAnimeByCategory(GetContentStrategy):
    """
     This method concrete strategy for getting anime by category.
    """

    def get_content(self, search_parameter):
        return AnimeDAO.get_anime_by_category(search_parameter)


class GetAnimeByType(GetContentStrategy):
    """
    This methos concrete strategy for getting anime by type.
    """

    def get_content(self, search_parameter):
        return AnimeDAO.get_anime_by_type(search_parameter)


class GetNews(GetContentStrategy):
    """
    This method concrete strategy for get news
    """

    def get_content(self, search_parameter):
        pass


class GetRadioStation(GetContentStrategy):
    """
    This method oncrete strategy for get radio station
    """

    def get_content(self, search_parameter):
        pass
