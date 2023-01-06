#!/usr/bin/python3
""" Define City Class """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ Define City Class

        name Column: string(128) and can't be null
        state_id Column: string(60) Foreignkey to
                         states.id and can't be null
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
