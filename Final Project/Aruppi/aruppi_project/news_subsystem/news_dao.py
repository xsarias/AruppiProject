"""
This module contains the DAO (Data Access Object) for managing news data.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
from ..config import news, engine
from typing import List

Session = sessionmaker(bind=engine)
class NewsDAO:
    """This class provides data access for managin news data"""

    @classmethod
    def add_news(cls, news1):
        """This method adds news to the database"""

        news_data = {
            "title": news1.title,
            "info": news1.info,
        }
        session = Session()
        try:
            session.execute(news.insert().values(news_data))
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error inserting series: {e}")
        finally:
            session.close()


    # def remove_news_by_title(self, title: str) -> bool:
    #     """This method remove news by title"""
    #     for news in self.news_list:
    #         if news.title == title:
    #             self.news_list.remove(news)
    #             return True
    #     return False
    # def  get_all_news(self) -> List[News]:
    #     """This method shows the news"""
    #     return self.news_list