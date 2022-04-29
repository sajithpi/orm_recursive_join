from requests import Session
from sqlalchemy import Column, ForeignKey,String,Integer,DateTime,create_engine,exc,desc
# from sqlalchemy.ext.declarative import declarative_base       
from sqlalchemy.orm import declarative_base,sessionmaker,relationship
from datetime import datetime


Base = declarative_base()

# Specifying database connection url
engine = create_engine("mysql+pymysql://root:password@localhost/orm_recursive",echo=True)

Session = sessionmaker()

# Table creation
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(),primary_key=True)
    username = Column(String(25),nullable=False,unique=True)
    email = Column(String(75),unique=True,nullable=False)
    date_created = Column(DateTime(),default=datetime.utcnow)
    treepath = relationship('Treepath',back_populates='usr')

class Treepath(Base):
    __tablename__='treepaths'
    id = Column(Integer(),primary_key=True)
    sponser_id = Column(Integer(),ForeignKey('users.id'))
    user_id = Column(Integer())
    usr = relationship('User',back_populates='treepath')                                                                        