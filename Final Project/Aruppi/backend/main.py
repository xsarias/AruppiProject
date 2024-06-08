"""
This is a main file of Aruppi project (initial point).
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from fastapi import FastAPI
from pydantic import BaseModel
from .anime_subsystem import AnimeFacade
from .radio_subsystem import RadioFacade



app = FastAPI(
    title="Aruppi API",
    description="This is an Aruppi aplication.",
    version="1.0.0"
)


#an example 
class Search(BaseModel):
    """This is an example class"""
    name: str
    category:str

@app.post("/anime/search_by_category")
async def search_by_category(search_category:Search):
    """
    This function search an anime by category.

    Args:
        s.

    Returns:
        .
    """
    return {"find": search_category}

@app.post("/anime/search_by_type")
async def search_by_type(search_type:Search):
    """
    This function search an anime by type.

    Args:
        s.

    Returns:
        .
    """
    return {"find": search_type}

@app.post("/anime/search_by_tittle")
async def search_by_tittle(search_tittle:Search):
    """
    This function search an anime by type.

    Args:
        s.

    Returns:
        .
    """
    return {"find": search_tittle}

@app.get("/anime/watch_series")
async def watch_series():
    """
    This function get series to watch.
    """
    return {"message": "serie"}

@app.get("/anime/watch_ovas")
async def watch_ovas():
    """
    This function get ovas to watch.
    """
    return {"ovas":"ov"}

@app.get("/anime/watch_movies")
async def watch_movies():
    """
    This function get movies to watch.
    """
    return {"user_id": "the current user"}

@app.get("/anime/watch_especials")
async def watch_especials():
    """
    This function get especials to watch.
    """
    return {"user_id": "the current user"}

@app.get("/radio/listen_radio")
async def listen_radio():
    """
    This function get radio station to listen.
    """
    return {"station":"station x"}

@app.get("/news/read_news")
async def read_news():
    """
    This function get news to read.
    """
    return {"news":"noticion"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    """
    This function get user information.
    """
    return {"user_id": user_id}



#----------------------------

MENU="""
......   ......   .... .... ......   ......  .......
|  _  |  |  _  \\  |  | |  | |  _  \\  |  _  \\ |_   _|  
| |_| |  | |_|  | |  | |  | | |_\\  | | |_\\  |  | |
|  _  |  |     /  |  |_|  | |   __/  |   __/  _| |_
|_| |_|  |__|\\_\\  |_______| |__|     |__|    |_____|
        >>>> ALL JAPAN IN A SAME PLACE <<<
What do you want to explore?
1). Anime.
2). Radio.
3). News.
4). View my user profile.
"""

ANIME_MENU="""
        ......   ...  .... ....... ....   ....  ........
        |  _  |  |  \\ |  | |_   _| |   \\ /   |  |  __  |
        | |_| |  |   \\|  |   | |   |         |  |   ___|
        |  _  |  |       |  _| |_  |   |\\ /|  |  |  |___
        |_| |_|  |__|\\___| |_____| |___|  |__|  |______|
                 >>> A R U P P I <<< 
        What do you want to do? 
        1). Search Anime by tittle.
        2). Search Anime by category.
        3). Search Anime by type.
        4). Watch Series.
        5). Watch Movies.
        6). Watch Ovas's.
        7). Back to principal menu.
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

RADIO_MENU="""
        ......   ....... .......   ..........  ......... 
        |  _  \\  |  _  | |   _  \\  |__    __|  |  __   |
        | |_|  | | |_| | |  | \\  |    |  |     |  | |  |
        |     /  |  _  | |  |_/  |  __|  |__   |  |_|  |
        |__|\\_\\  |_| |_| |______/  |________|  |_______|
                 >>> A R U P P I <<< 
        What do you want to do? 
        1). Search Anime.
        2). Watch Series.
        3). Watch Movies.
        4). Watch Ovas's.
        5). Watch Especials.
        6). Back to principal menu.
        """


anime_facade=AnimeFacade()
def anime_menu():
    """This method shows the principal anime menu"""
    print(ANIME_MENU)
    op=input(print("Please, select an option:"))
    print(op)

    while True:
        print(ANIME_MENU)
        option = input("Please, select an option: ").strip()

        if option == '1':
            anime_facade.search_anime_by_tittle()
        elif option == '2':
            anime_facade.search_anime_by_category()
        elif option == '3':
            anime_facade.search_anime_by_type()
        elif option == '4':
            anime_facade.watch_series()
        elif option == '5':
            anime_facade.watch_movies()
        elif option =='6':
            anime_facade.watch_ovas()
        elif option == '7':
            principal_menu()
            break
        else:
            print("Invalid option. Please try again.")

def radio_menu():
    """This method shows the principal radio menu"""
    op=input("Please, select an option:")
    print(op)
    if op == "1":
        print("ya casi")



def news_menu():
    """This method shows the news menu"""
    print(NEWS_MENU)
    op=input("Please, select an option:")
    print(op)

def principal_menu():
    """This method shows the principal Aruppi's menu"""
    print(MENU)
    op=input("Please, select an option:")
    if op=="1":
        anime_menu()
    elif op=="2":
        radio_menu()
    elif op=="3":
        news_menu()
    elif op=="4":
        pass

def main():
    """This if the main file of the project."""
    principal_menu()

if __name__ == "__main__":
    main()