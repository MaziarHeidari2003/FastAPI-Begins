from enum import Enum 
from pydantic import BaseModel,validator
from datetime import date
from sqlmodel import SQLModel,Field,Relationship

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



    

class AlbumBase(SQLModel):
    title: str
    release_date: date
    band_id: int | None =Field(foreign_key='band.id')
 
class Album(AlbumBase,table=True):
    id: int = Field(default=None,primary_key=True)
    band : "Band" = Relationship(back_populates='albums')



class BandBase(SQLModel):
    # id: int
    name: str
    genre: GenreChoices

class BandCreate(BandBase):
    albums: list[Album] = []
    @validator('genre',pre=True)
    def title_case_genre(cls,value):
        return value.title()

class Band(BandBase,table=True):
    id: int = Field(default=None,primary_key=True)
    albums: list[Album] = Relationship(back_populates='band')
