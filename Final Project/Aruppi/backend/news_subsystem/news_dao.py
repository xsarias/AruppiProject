"""
This module contains the DAO (Data Access Object) for managing news data.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from typing import List
from .news import News
class NewsDAO:
    """This class provides data access for managin news data"""

    def __init__(self):
        self.news_list=[]

    def add_news(self, news):
        """This method adds news to the database"""

        self.news_list.append(news)

    def remove_news_by_title(self, title:str ) -> bool:
        """This method remove news by title"""
        for news in self.news_list:
            if news.title == title:
                self.news_list.remove(news)
                return True
        return False

    def get_all_news(self)-> List[News]:
        """This method shows the news"""
        return self.news_list