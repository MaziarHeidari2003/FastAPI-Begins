from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models, hash
from ..database import get_db
from typing import List
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post("/users/create/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=hash.Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/users/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    return user
