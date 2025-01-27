from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models
from ..database import get_db
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.get("/blog", response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    return blog.get_all(db)

@router.get("/blog/{id}", response_model=schemas.ShowBlog)
def show(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not fount asshole"
        )
    return blog


@router.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, session=Depends(get_db)):
    band = session.query(models.Blog).get(id)
    if not band:
        raise HTTPException(status_code=404, detail="Blog not found")
    session.delete(band)
    session.commit()
    return {"message": f"Band with ID {id} deleted successfully"}


@router.put("/blogs/{id}")
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog_query.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="not found honey"
        )

    # Extract only valid fields for the Blog model
    update_data = request.dict(
        exclude_unset=True
    )  # Excludes fields not provided in the request

    blog_query.update(update_data)
    db.commit()
    return {"detail": "Blog updated successfully"}


@router.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
   return blog.create(request,db)