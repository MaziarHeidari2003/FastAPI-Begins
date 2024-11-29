from sqlalchemy import (Column,ForeignKey,Integer,String,create_engine)
from sqlalchemy.orm import declarative_base,relationship,mapped_column,Mapped
from database import Base,engine

class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True
    id = Column(Integer,primary_key=True)


class Address(BaseModel):
    __tablename__ = "addresses"
    city = Column(String)
    state = Column(String)
    zip_code = Column(Integer)
    user_id = Column(Integer,ForeignKey("users.id"))
    user = relationship('User') # getting the user associated with na address

    def __repr__(self):
        return f"<Address(id={self.id}, city={self.city})"

class User(BaseModel):
    __tablename__ = 'users'
    name = Column(String)
    age = Column(Integer)
    addresses = relationship("Address", backref="owner")  # Correctly maps relationship

    def __repr__(self):
        return self.name


# class User(Base):
#     __tablename__='users'
#     __allow_unmapped__ = True

#     id = Column(Integer,primary_key=True)
#     username = Column(String)
#     following_id = Column(Integer,ForeignKey('users.id'))
#     following = relationship('User', remote_side=[id],userlist=True)
