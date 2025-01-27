from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,models
from sqlalchemy.orm import Session
from ..database import get_db 
from ..hash import Hash

router = APIRouter(
    tags=['/login']
)

def login(request: schemas.Login,db: Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='not found')
    
    if not Hash.verify(user.pasword,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='not found')
    
    return user




    return 'login'
