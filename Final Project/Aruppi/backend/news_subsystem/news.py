"""
This file has the classes that control the news.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

class News:
    """This class control of news links about Japanese cultur"""
    def __init__(self, info):
        self.information=info
    
    def read_news(self):
        """This method shows a list of news"""        
        list_news=[]
        if not list_news :
            print("no news for the moment")
            return
        for info in list_news:
            print(info)       


