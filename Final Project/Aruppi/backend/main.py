"""
This is a main file of Aruppi project (initial point).
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .anime_subsystem import AnimeFacade, Series, Ovas, Movies
from .news_subsystem import NewsFacade, News
from .core_subsystem import Authentication
from .radio_subsystem import RadioFacade, Station, Play, Pause

app = FastAPI(
    title="Aruppi API",
    description="This is an Aruppi aplication.",
    version="1.0.0"
)
anime_facade = AnimeFacade()
news_facade = NewsFacade()

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


class MoviesBase(BaseModel):
    """Base model for anime movies."""
    anime_id: str
    title: str
    description: str
    category: str
    anime_type: str
    producer: str
    running_time: float
@app.post("/admin/anime/add_movies/")
async def create_movies(movies_base: MoviesBase):
    """
    Route to create a new series.

    Parameters:
        series_base (MoviesBase): Data of the movies series.

    Returns:
        dict: A message indicating successful creation of the series.
    """
    series_data = movies_base.dict()
    anime_facade.add_anime(
        Movies(
            series_data["anime_id"],
            series_data["title"],
            series_data["description"],
            series_data["category"],
            series_data["anime_type"],
            series_data["producer"],
            series_data["running_time"]
        )
    )
    return {"message": "Movies created successfully"}


class OvasBase(BaseModel):
    """Base model for anime movies."""
    anime_id: str
    title: str
    description: str
    category: str
    anime_type: str
    producer: str
    running_time: float

@app.post("/admin/anime/add_ovas/")
async def create_movies(ovas_base: OvasBase):
    """
    Route to create a new Ovas

    Parameters:
        series_base (OvasBase): Data of the ovas.

    Returns:
        dict: A message indicating successful creation of the ovas.
    """
    series_data = ovas_base.dict()
    anime_facade.add_anime(
        Ovas(
            series_data["anime_id"],
            series_data["title"],
            series_data["description"],
            series_data["category"],
            series_data["anime_type"],
            series_data["producer"],
            series_data["running_time"]
        )
    )
    return {"message": "Ovas created successfully"}

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

@app.post("/user/anime/watch_series")
async def watch_series():
    """
    Route to search anime by type.

    Parameters:
        search_params (Search): Search parameters.

    Returns:
        dict: A list of anime titles matching the type.
    """
 
    titles_matching_type = anime_facade.search_anime_by_type("Series")
    return {"matching_titles": titles_matching_type}

@app.post("/user/anime/watch_movies")
async def watch_movies():
    """
    Route to search anime by type.

    Parameters:
        search_params (Search): Search parameters.

    Returns:
        dict: A list of anime titles matching the type.
    """
 
    titles_matching_type = anime_facade.search_anime_by_type("Movies")
    return {"matching_titles": titles_matching_type}

@app.post("/user/anime/watch_ovas")
async def watch_ovas():
    """
    Route to search anime by type.

    Parameters:
        search_params (Search): Search parameters.

    Returns:
        dict: A list of anime titles matching the type.
    """
 
    titles_matching_type = anime_facade.search_anime_by_type("Ovas")
    return {"matching_titles": titles_matching_type}

class NewsBase(BaseModel):
    """Base model for news ."""
    title : str
    info: str


@app.post("/admin/news/add_news/")
async def create_news(news_base: NewsBase):
    """
    Route to create news

    Parameters:
        news_base (NewsBase): Data of the newss.

    Returns:
        dict: A message indicating successful creation of the news.
    """
    news = News(title=news_base.title, info=news_base.info)
    news_facade.add_news(news)
    return {"message": "News created successfully"}

@app.post("/user/news/show_news")
async def view_news():
    """
    Route to show news

    Returns:
        List[News]: A list of all news.
    """
    news = news_facade.show_news()
    return {"news ":news}
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

stations = [Station(name="Olympica"), Station(name="Radio Uno"), Station(name="La Mega")]
radio_facade = RadioFacade(stations)

@app.get("/radio/stations/")
async def get_all_stations():
    stations = radio_facade.get_all_stations()
    return {"stations": [station.name for station in stations]}

@app.post("/radio/play/")
async def play(station_name: str):
    success = radio_facade.set_current_station(station_name)
    if not success:
        raise HTTPException(status_code=404, detail="Station not found")
    radio_facade.set_state(Play())
    radio_facade.action()
    return {"message": f"Station {station_name} is now playing"}

@app.post("/radio/pause/")
async def pause(station_name:str):
    success = radio_facade.set_current_station(station_name)
    if not success:
        raise HTTPException(status_code=404, detail="No current station set")
    radio_facade.set_state(Pause())
    radio_facade.action()
    return {"message": f"Station {station_name} is now paused"}
