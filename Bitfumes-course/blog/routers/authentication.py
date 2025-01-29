from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,models
from sqlalchemy.orm import Session
from ..database import get_db 
from ..hash import Hash
from ..token import create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import datetime, timedelta, timezone
import token

router = APIRouter(
    tags=['Login'],
    prefix='/auth'
)

@router.post('/login')
def login(request: schemas.Login,db: Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.name == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='not found')
    
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='not found')

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.name},
        expires_delta=access_token_expires,
    )
    return schemas.Token(access_token=access_token, token_type="bearer")

    




