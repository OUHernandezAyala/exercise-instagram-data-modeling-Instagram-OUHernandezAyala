import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, primary_key=True,unique=True, nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True, nullable=False)
    user_from_id = Column(Integer,ForeignKey("user.id"))
    user_to_id = Column(Integer,ForeignKey("user.id"))
    user = relationship("User")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, nullable=False)
    coment_text = Column(String)
    author_id = Column(Integer,ForeignKey("user.id"), nullable=False)
    user = relationship("User")
    post_id = Column(Integer,ForeignKey("post.id"), nullable=False)
    post = relationship("Post")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, nullable=False)
    author_id = Column(Integer,ForeignKey("user.id"), nullable=False)
    user = relationship("User")

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True, nullable=False)
    post_id = Column(Integer,ForeignKey("post.id"), nullable=False)
    post = relationship("Post")
    type = Column(Integer, nullable=False)
    url = Column(String)
    text = Column(String)




    

    def to_dict(self):
        return {}
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
