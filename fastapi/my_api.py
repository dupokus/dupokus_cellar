from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()

anime_titles = {
    1: {
        "name": "akira",
        "year_made": 1994,
        "duration": "162 minutes"
    }
}

class Anime(BaseModel):
    name: str | None = None
    year_made: int | None = None
    duration: str | None = None

@app.get("/")
def index():
    return {"Eugene ZHURAVEL": "lox"}

@app.get("/get-anime/{anime_id}")
def get_anime(anime_id: int = Path(description="The ID of the anime you want to view.", gt=0)):
    return anime_titles[anime_id]

@app.get("/get-anime-by-name/")
def get_anime(name: Optional[str] = None):
    for anime_id in anime_titles:
        if anime_titles[anime_id]["name"] == name:
            return anime_titles[anime_id]
        return {"Data": "Not found"}
    
@app.post("/create-anime/{anime_id}")
def create_anime(anime_id: int, anime: Anime):
    if anime_id in anime_titles:
        return {"Error": "Anime already exists"}
    anime_titles[anime_id] = anime
    return anime_titles[anime_id]

@app.patch("/update-anime/{anime_id}", response_model=Anime)
async def update_anime(anime_id: int, anime: Anime):
    stored_anime_data = anime_titles[anime_id]
    stored_anime_model = Anime(**stored_anime_data.dict())
    update_data = anime.dict(exclude_unset=True)
    updated_anime = stored_anime_model.copy(update=update_data)
    anime_titles[anime_id] = jsonable_encoder(updated_anime)
    return updated_anime

@app.delete("/delete-anime/{anime_id}")
def delete_anime(anime_id: int):
    if anime_id not in anime_titles:
        return {"Error": "Anime does not exist"}
    
    del anime_titles[anime_id]
    return {"Message": "Anime deleted successfully"}