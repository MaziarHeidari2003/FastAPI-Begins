from enum import Enum 
from pydantic import BaseModel,validator
from datetime import date

class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HIP_HOP = 'hip-hop'



class GenreChoices(Enum):
    ROCK = 'Rock'
    ELECTRONIC = 'Electronic'
    METAL = 'Metal'
    HIP_HOP = 'Hip-Hop'



    

class Album(BaseModel):
    title: str
    release_date: date



class BandBase(BaseModel):
    # id: int
    name: str
    genre: GenreChoices
    album: list[Album] = []

class BandCreate(BandBase):
    @validator('genre',pre=True)
    def title_case_genre(cls,value):
        return value.title()

class BandwithID(BandBase):
    id: int
