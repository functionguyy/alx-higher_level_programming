#!/usr/bin/python3
"""module contains the class definition of a City object"""
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """Class"""

    __tablename__ = 'cities'

    id = Column(Integer,
                primary_key=True,
                unique=True,
                )
    name = Column(String(128),
                  nullable=False,
                  )
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    # state = relationship("State", back_populates="cities")
