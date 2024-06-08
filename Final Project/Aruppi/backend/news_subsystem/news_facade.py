"""
This is a main file of Aruppi project (initial point).
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

NEWS_MENU="""
        ...  .... ........ .....    ..... .........
        |  \\ |  | |  __  | |   |    |   | |   _____|
        |   \\|  | |   ___|  \\   \\/\\/   /  |_____   |
        |       | |  |___    \\        /    _____|  |
        |__|\\___| |______|    \\__/\\__/    |_______ |
                 >>> A R U P P I <<< 
        What do you want to do? 
        1). Search Anime.
        2). Watch Series.
        3). Watch Movies.
        4). Watch Ovas's.
        5). Watch Especials.
        6). Back to principal menu.
        """

def news_menu():
    """This method shows the principal radio menu"""

    print(NEWS_MENU)
    op=input(print("Please, select an option:"))
    print(op)
