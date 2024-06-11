"""
This module implements strategies to get japanese culture content.
"""

from abc import ABC, abstractmethod
from .anime_dao import AnimeDAO
from .anime_types import Series, Anime, Ovas
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
    def add_content(self, content):
        AnimeDAO.add_movies(content)

class AddOvasAnime(AddContentStrategy):
    """
    Concrete strategy for adding OVAs.
    """
    def add_content(self, content):
        AnimeDAO.add_ovas(content)

class AddSeriesAnime(AddContentStrategy):
    """
    Concrete strategy for adding series.
    """
    def add_content(self, content):
        if isinstance(content, dict):
            series = Series(
                anime_id=content.get("anime_id"),
                title=content.get("title"),
                description=content.get("description"),
                category=content.get("category"),
                anime_type=content.get("anime_type"),
                producer=content.get("producer"),
                episodes_amount=content.get("episodes_amount"),
            )
            AnimeDAO.add_series(series)
        else:
            raise ValueError("Content must be a dictionary")



class AddNews(AddContentStrategy):
    """
    Concrete strategy for adding news
    """
    def add_content(self, content):
        # Aquí puedes implementar la lógica para añadir noticias si es necesario
        pass
