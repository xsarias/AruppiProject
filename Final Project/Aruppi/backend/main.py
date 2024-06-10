"""
This is a main file of Aruppi project (initial point). Where web services
are defined to interact with external users (also front-end clients)
Authors:
-> Xiomara Salome Arias Arias < xsariasa@udistrital.edu.co >
-> Carlos Andres Celis Herrera < cacelish@udistrital.edu.co >
"""
from .anime_subsystem import AnimeFacade, Series, Ovas, Movies
from .radio_subsystem import RadioFacade, Radio
from .core_subsystem import Authentication
from fastapi import FastAPI
from pydantic import BaseModel, SecretStr

app = FastAPI(
    title="Aruppi API", description="This is an Aruppi aplication.", version="1.0.0"
)
anime_facade = AnimeFacade()

class Login(BaseModel):
    """Base Model for Login"""
    username: str
    password: str

@app.post("/login")
def login(user_info: Login) -> bool:
    """This service lets authenticate an user using username and password."""
    user=user_info.dict()
    auth = Authentication(user["username"], user["password"])
    return auth.authenticate()

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
            series_data["episodes_amount"],
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
def create_movies(movies_base: MoviesBase):
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
            series_data["running_time"],
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
def create_ovas(ovas_base: OvasBase):
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
            series_data["running_time"],
        )
    )
    return {"message": "Ovas created successfully"}


class Search(BaseModel):
    """Base model for searching anime."""

    search: str


@app.post("/user/anime/search_by_title")
def search_by_title(search_params: Search):
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


@app.get("/user/anime/watch_series")
def watch_series():
    """
    Route to search anime by type.

    Parameters:
        search_params (Search): Search parameters.

    Returns:
        dict: A list of anime titles matching the type.
    """

    titles_matching_type = anime_facade.search_anime_by_type("Series")
    return {"avalaible series": titles_matching_type}


@app.get("/user/anime/watch_movies")
def watch_movies():
    """
    Route to search anime by type.

    Parameters:
        search_params (Search): Search parameters.

    Returns:
        dict: A list of anime titles matching the type.
    """

    titles_matching_type = anime_facade.search_anime_by_type("Movies")
    return {"avalaible movies": titles_matching_type}


@app.get("/user/anime/watch_ovas")
def watch_ovas():
    """
    Route to search anime by type.

    Parameters:
        search_params (Search): Search parameters.

    Returns:
        dict: A list of anime titles matching the type.
    """

    titles_matching_type = anime_facade.search_anime_by_type("Ovas")
    return {"ovas avalaible to watch": titles_matching_type}

