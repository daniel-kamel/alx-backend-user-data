#!usr/bin/env python3
'''User model for the user authentication service.'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    '''User model for the user authentication service.'''
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(128), nullable=False)
    hashed_password = Column(String(256), nullable=False)
    session_id = Column(String(64), nullable=True)
    reset_token = Column(String(256), nullable=True)
