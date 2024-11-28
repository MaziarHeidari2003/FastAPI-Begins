from fastapi import APIRouter
from .. import schemas,database,models,hashing
from typing import List
from fastapi import Depends,status,HTTPException
from sqlalchemy.orm import Session
from blog.repository import user

router = APIRouter(
    tags=['User'],
    prefix='/user'
)


@router.post('/',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db: Session = Depends(database.get_db)):
    return user.create(request,db)



@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db: Session = Depends(database.get_db)):
   return user.show(id,db)