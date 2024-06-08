"""
This is a main file of Aruppi project (initial point).
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from fastapi import FastAPI
from pydantic import BaseModel
from .anime_subsystem import AnimeFacade


menuAnime=AnimeFacade()
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

def main():
    """This if the main file of the project."""
    print(MENU)
    op=input(print("Please, select an option:"))
    if op=="1":
        anime_menu()
    elif op=="2":
        pass
    elif op=="3":
        pass

if __name__ == "__main__":
    main()

