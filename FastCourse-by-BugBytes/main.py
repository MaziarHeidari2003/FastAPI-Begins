from fastapi import FastAPI,HTTPException,Query,Path 
from enum import Enum
from models import GenreURLChoices,BandBase,BandCreate,Band,Album
from typing import Annotated
from db import init_db


from contextlib import asynccontextmanager



@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)

BANDS = [
    {'id':1,'name':'The Kinks','genre':'Rock',},
    {'id':2,'name':'Aphex Twin','genre':'Electronic'},
    {'id':3,'name':'Black Sabbath','genre':'Metal'},
    {'id':4,'name':'wu-Tang clan','genre':'Hip-Hop','album':[
        {'title':'Master of reality','release_date':'1997-01-01',}
    ]}

]



# class GenreURLChoices(Enum):
#     ROCK = 'rock'
#     ELECTRONIC = 'electronic'
#     METAL = 'metal'
#     HIP_HOP = 'hip-hop'



# @app.get('/bands')
# async def bands(genre: GenreURLChoices | None = None,q:Annotated[str | None,Query(max_length=10)]= None) -> list[BandwithID]: # this is called a handles func
#     band_list = [BandwithID(**b) for b in BANDS ]
    
#     if genre:
#         # Band(**b) for b in BANDS if b['genre'].lower() == genre.value
#         band_list= [ b for b in band_list if b.genre.lower() == genre.value ]
        
    
  
#     return band_list

# @app.get('/bands/{band_id}')
# async def band(band_id: Annotated[int,Path('the band id')]) -> BandwithID:
#     band = next((BandwithID(**b) for b in BANDS if b['id']==band_id),None)
#     if band is None:
#         return HTTPException(status_code=404,detail='Band not found')
#     return band
    

# @app.get('/band/genre/{genre}')
# async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
#     return [
#                  b for b in BANDS if b['genre'].lower() == genre.value
#     ] 


# #the path param will have some ref in the url 
# # if we define an arg to these functions that is not persent in the path params, then
# # by default what fast is ganna do is interpert them as q params


# @app.post('/bands')
# async def create_band(band_data: BandCreate) -> BandwithID:
#     id = BANDS[-1]['id'] + 1
#     band = BandwithID(id=id,**band_data.model_dump()).model_dump()
#     BANDS.append(band)
#     return band