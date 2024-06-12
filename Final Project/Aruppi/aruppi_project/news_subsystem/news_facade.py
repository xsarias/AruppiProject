"""
This is module news facade (initial point).
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

from typing import List
from .news_dao import NewsDAO
from .news import News

class NewsFacade:
    """This class is facade of news"""

    def __init__(self):
        self.newsdao = NewsDAO()

    def add_news(self, news_data:News):
        """This method adds news to the database"""
        self.newsdao.add_news(
            News(
                news_data["title"],
                news_data["info"],
            )

        )
        return "News added successfully"

    # def delete_news_by_title(self, title: str) -> bool:
    #     """This Class remove news by title"""
    #     return self.newsdao.remove_news_by_title(title)

    # def show_news(self) -> List[dict]:
    #     """This methos shows the news"""
    #     return self.newsdao.get_all_news()
