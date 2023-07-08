import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String,Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

class postEnum(enum.Enum):
    single_photo = "single photo"
    carousel = "carousel"
    videos = "videos"

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id= Column(Integer, primary_key=True)
    username = Column(String(50), nullable= False)
    firstname = Column(String(250),nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable= False)

    
class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key = True)
    user = Column(Integer,ForeignKey("user"))

class Media(Base):
    __tablename__ = "media"
    id= Column(Integer,primary_key=True)
    type = Column(Enum(postEnum))
    url = Column(String(250), nullable=False)
    post = Column(Integer,ForeignKey("post"))

class Comment(Base):
    __tablename__ ="comment"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    user = Column(Integer, ForeignKey("user"))
    post = Column(Integer, ForeignKey("post"))

class Follower(Base):
    __tablename__ ="follower"
    user_from = Column(Integer, primary_key=True)
    user_to = Column(Integer, ForeignKey("user"))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
