#!/usr/bin/python3
"""module contains the class definition of a State class and SQLAlchemy
declarative base class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """State class mapped to states table"""

    __tablename__ = 'states'

    id = Column(Integer,
                primary_key=True,
                unique=True,
                nullable=False,
                )
    name = Column(String(128),
                  nullable=False)
    #cities = relationship("City", back_populates="state")
