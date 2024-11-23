from fastapi import FastAPI,HTTPException
from enum import Enum
from schemas import GenreURLChoices,Band

app = FastAPI()

BANDS = [
    {'id':1,'name':'The Kinks','genre':'Rock',},
    {'id':2,'name':'Aphex Twin','genre':'Electronic'},
    {'id':3,'name':'Black Sabbath','genre':'Metal'},
    {'id':4,'name':'wu-Tang clan','genre':'Hip-Hop','album':[
        {'title':'Master of reality','release_date':'1997-01-01',}
    ]}

]

class GenreURLChoices(Enum):
    ROCK = 'rock'
    ELECTRONIC = 'electronic'
    METAL = 'metal'
    HIP_HOP = 'hip-hop'



@app.get('/bands')
async def bands(genre: GenreURLChoices | None = None,
                has_albums: bool = False) -> list[Band]: # this is called a handles func
    band_list = [Band(**b) for b in BANDS ]
    
    if genre:
        return [
            # Band(**b) for b in BANDS if b['genre'].lower() == genre.value
            b for b in band_list if b.genre.lower() == genre.value
        ]
    if has_albums:
        band_list = [b for b in band_list if len(b.album) > 0]

        
    return band_list

@app.get('/bands/{band_id}')
async def band(band_id:int) -> Band:
    band = next((Band(**b) for b in BANDS if b['id']==band_id),None)
    if band is None:
        return HTTPException(status_code=404,detail='Band not found')
    return band
    

@app.get('/band/genre/{genre}')
async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
    return [
                 b for b in BANDS if b['genre'].lower() == genre.value
    ] 


#the path param will have some ref in the url 
# if we define an arg to these functions that is not persent in the path params, then
# by default what fast is ganna do is interpert them as q params