from sqlalchemy.orm import Session
from .. import models

def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request,db):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

