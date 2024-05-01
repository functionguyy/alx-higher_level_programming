#!/usr/bin/python3
"""This module defines a class definition of a City
and an instance declarative_base() of the SQLAlchemy library
This is used to for the ORM mapping and configuration

Attributes:
    City: function
"""
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):
    """Class definition for City object

    Attributes:
        id: primary key
        name: name of the state
        state_id: foriegn key
    """

    __tablename__ = 'cities'

    id = Column(Integer,
                primary_key=True,
                unique=True,
                )
    name = Column(String(128),
                  nullable=False,
                  )
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
