#!/usr/bin/python3
"""
This module defines a class definition of a State and an instance
Base = declarative_base() of the SQLAlchemy library
This is used to for the ORM mapping and configuration

Attribute:
    State: function
    Base: declareative base class instance
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import City

Base = declarative_base()


class State(Base):
    """State class mapped to states table

    Attributes:
        id: primary key
        name: name of the state
        cities: foriegn key
    """

    __tablename__ = 'states'

    id = Column(Integer,
                primary_key=True,
                unique=True,
                nullable=False,
                )
    name = Column(String(128),
                  nullable=False)
    cities = relationship("City", backref="state", cascade="all delete-orphan")
