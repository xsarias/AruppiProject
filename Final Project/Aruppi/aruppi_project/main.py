"""
This is a main file of Aruppi project (initial point). Where web services
are defined to interact with external users (also front-end clients)
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""

from .news_subsystem import NewsFacade, News
from .core_subsystem import Authentication
from .radio_subsystem import RadioFacade, Station, Play, Pause
from .anime_subsystem import AnimeFacade
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Aruppi API", description="This is an Aruppi aplication.", version="1.0.0"
)
anime_facade = AnimeFacade()
news_facade = NewsFacade()



class Login(BaseModel):
    """Base Model for Login"""

    username: str
    password: str


class SeriesBase(BaseModel):
    """Base model for anime series."""
    anime_id: str
    title: str
    description: str
    category: str
    anime_type: str
    producer: str
    episodes_amount: int


class MoviesBase(BaseModel):
    """Base model for anime movies."""

    anime_id: str
    title: str
    description: str
    category: str
    anime_type: str
    producer: str
    running_time: float


class OvasBase(BaseModel):
    """Base model for anime movies."""

    anime_id: str
    title: str
    description: str
    category: str
    anime_type: str
    producer: str
    running_time: float


class Search(BaseModel):
    """Base model for searching anime."""

    search: str


class NewsBase(BaseModel):
    """Base model for news ."""

    title: str
    info: str


# -------------------------->>>> Routes and CRUD operations definitions


@app.post("/login")
def login(user_info: Login) -> bool:
    """This service lets authenticate an user using username and password."""
    user = user_info.dict()
    auth = Authentication(user["username"], user["password"])
    return auth.authenticate()


# -------------------------Services for ADMIN -------------------------------
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
    anime_facade.add_anime_series(series_data)
    return {"message": "Series created successfully"}


@app.post("/admin/anime/add_movies/")
def create_movies(movies_base: MoviesBase):
    """
    Route to create a new series.

    Parameters:
        movies_base (MoviesBase): Data of the movies.

    Returns:
        dict: A message indicating successful creation of the series.
    """
    movies_data = movies_base.dict()

    anime_facade.add_anime_movies(movies_data)
    return {"message": "Movies created successfully"}


@app.post("/admin/anime/add_ovas/")
def create_ovas(ovas_base: OvasBase):
    """
    Route to create a new Ovas

    Parameters:
        series_base (OvasBase): Data of the ovas.

    Returns:
        dict: A message indicating successful creation of the ovas.
    """
    ovas_data = ovas_base.dict()
    anime_facade.add_anime_ovas(ovas_data)
    return {"message": "Ovas created successfully"}


@app.post("/admin/news/add_news/")
async def create_news(news_base: NewsBase):
    """
    Route to create news

    Parameters:
        news_base (NewsBase): Data of the newss.

    Returns:
        dict: A message indicating successful creation of the news.
    """
    news_data = news_base.dict()
    news_facade.add_news(news_data)
    return {"message": "News created successfully"}


# ----------------------- Services for USER ---------------------------------


@app.post("/user/anime/search_by_title")
def search_by_title(search_params: Search):
    """
    Route to search anime by title.

    Parameters:
        search_params (Search): Search parameters.

    Returns:
        dict: A list of anime titles matching the title.
    """
    print(search_params)
    results = anime_facade.search_anime_by_title(search_params)
    print(results)
    return results


@app.post("/user/anime/search_by_category")
def search_by_category(search_params: Search):
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


@app.post("/user/news/show_news")
async def view_news():
    """
    Route to show news

    Returns:
        List[News]: A list of all news.
    """
    news = news_facade.show_news()
    return {"news ": news}


@app.delete("/admin/news/delete_news/")
async def delete_news(title: str):
    """
    Route to delete news by title

    Parameters:
        title (str): The title of the news to delete.

    Returns:
        dict: A message indicating the result of the deletion.
    """
    success = news_facade.delete_news_by_title(title)
    if not success:
        raise HTTPException(status_code=404, detail="News not found")
    return {"message": "News deleted successfully"}


# test
stations = [
    Station(name="Olympica"),
    Station(name="Radio Uno"),
    Station(name="La Mega"),
]
radio_facade = RadioFacade(stations)


@app.get("/radio/stations/")
async def get_all_stations():
    """
    Route to retrieve all radio stations.

    Returns:
        dict: A list of all available radio stations.
    """
    stations = radio_facade.get_all_stations()
    return {"stations": [station.name for station in stations]}


@app.post("/radio/play/")
async def play(station_name: str):
    """
    Route to play a radio station.

    Parameters:
        station_name (str): The name of the station to play.

    Returns:
        dict: A message indicating the station is now playing.
    """
    success = radio_facade.set_current_station(station_name)
    if not success:
        raise HTTPException(status_code=404, detail="Station not found")
    radio_facade.set_state(Play())
    radio_facade.action()
    return {"message": f"Station {station_name} is now playing"}


@app.post("/radio/pause/")
async def pause(station_name: str):
    """
    Route to pause the currently playing radio station.

    Parameters:
        station_name (str): The name of the station to pause.

    Returns:
        dict: A message indicating the station is now paused.
    """
    success = radio_facade.set_current_station(station_name)
    if not success:
        raise HTTPException(status_code=404, detail="No current station set")
    radio_facade.set_state(Pause())
    radio_facade.action()
    return {"message": f"Station {station_name} is now paused"}
