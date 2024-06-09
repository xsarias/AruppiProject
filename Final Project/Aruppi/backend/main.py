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

@app.post("/user/anime/search_by_type")
async def search_by_type(search_params: Search):
    """
    Route to search anime by type.

    Parameters:
        search_params (Search): Search parameters.

    Returns:
        dict: A list of anime titles matching the type.
    """
    search_type = search_params.search
    titles_matching_type = anime_facade.search_anime_by_type(search_type)
    return {"matching_titles": titles_matching_type}