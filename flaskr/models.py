from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
 
 
Base = declarative_base()

engine = create_engine('sqlite:///database.sqlite')
Session = sessionmaker()
Session.configure(bind=engine)

sess = Session()
 
 
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    admin = Column(Integer, default=0)


def initialize_database():
    Base.metadata.create_all(engine)