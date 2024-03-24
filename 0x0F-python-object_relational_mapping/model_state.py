#!/usr/bin/python3
"""module contains the class definition of a State class and SQLAlchemy
declarative base class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Class"""

    __tablename__ = 'states'

    id = Column(Integer,
                primary_key=True,
                unique=True,
                nullable=False,
                )
    name = Column(String(128),
                  nullable=False)
