"""
This is a main file of Aruppi project (initial point).
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from .news import News

class NewsFacade:
    def __init__(self):
        
        self.news=News()
 
    def read_news(self):
        pass