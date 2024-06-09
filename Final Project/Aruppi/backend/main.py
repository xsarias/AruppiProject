"""
This is a main file of Aruppi project (initial point).
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from fastapi import FastAPI
from pydantic import BaseModel
from .anime_subsystem import AnimeFacade, Series, Ovas, Movies
from .radio_subsystem import RadioFacade
from .core_subsystem import Authentication

app = FastAPI(
    title="Aruppi API",
    description="This is an Aruppi aplication.",
    version="1.0.0"
)
anime_facade = AnimeFacade()

class SeriesBase(BaseModel):
    """Base model for anime series."""
    anime_id: str
    title: str
    description: str
    category: str
    anime_type: str
    producer: str
    episodes_amount: int

@app.post("/admin/anime/add_series/")
async def create_series(series_base: SeriesBase):
    """
    Route to create a new series.

    Parameters:
        series_base (SeriesBase): Data of the new series.

    Returns:
        dict: A message indicating successful creation of the series.
    """
    series_data = series_base.dict()
    anime_facade.add_anime(
        Series(
            series_data["anime_id"],
            series_data["title"],
            series_data["description"],
            series_data["category"],
            series_data["anime_type"],
            series_data["producer"],
            series_data["episodes_amount"]
        )
    )
    return {"message": "Series created successfully"}

class Search(BaseModel):
    """Base model for searching anime."""
    search: str

@app.post("/user/anime/search_by_title")
async def search_by_title(search_params: Search):
    """
    Route to search anime by title.

    Parameters:
        search_params (Search): Search parameters.

    Returns:
        dict: A list of anime titles matching the title.
    """
    search_title = search_params.search
    titles_matching_title = anime_facade.search_anime_by_title(search_title)
    return {"matching_titles": titles_matching_title}

@app.post("/user/anime/search_by_category")
async def search_by_category(search_params: Search):
    """
    Route to search anime by category.

    Parameters:
        search_params (Search): Search parameters.

    Returns:
        dict: A list of anime titles matching the category.
    """
    search_category = search_params.search
    titles_matching_category = anime_facade.search_anime_by_category(search_category)
    return {"matching_titles": titles_matching_category}

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

    print(RADIO_MENU)
    op=input("Please, select an option:")
    print(op)


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