"""
This his module implements strategies to get Japanese culture content.
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

from .get_content_strategy import GetContentStrategy


class GetContent:
    """
    This class represents a context for retrieving Japanese culture content.
    """

    def __init__(self, strategy: GetContentStrategy):
 
        self.strategy = strategy

    def set_strategy(self, strategy: GetContentStrategy):
        """
        Set the strategy for getting content.

        Parameters:
            strategy (GetContentrategy): The strategy to be used for getting content.
        """
        self.strategy = strategy

    def get_content(self, search_parameter):
        """
        Get Japanese culture content using the current strategy.

        Parameters:
            search_parameter: The parameter used for searching content.

        Returns:
            Content: The Japanese culture content.
        """
        return self.strategy.get_content(search_parameter)
