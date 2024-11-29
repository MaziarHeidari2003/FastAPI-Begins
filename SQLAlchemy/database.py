from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

db_url = 'sqlite:///data.db'

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
