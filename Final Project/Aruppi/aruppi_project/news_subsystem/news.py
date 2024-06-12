"""
This file has the classes that control the news.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""


class News:
    """This class provides news information"""

    def __init__(self, info, title):
        self.title = title
        self.info = info

    def read_news(self):
        """This method shows a list of news"""
