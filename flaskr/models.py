from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
 
 
Base = declarative_base()
session = None
 
 
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)


def initialize_database():
    engine = create_engine('sqlite:///database.sqlite')

    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.create_all(engine)