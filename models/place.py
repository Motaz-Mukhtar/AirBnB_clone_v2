#!/usr/bin/python3
""" Places class file """
import models
from models.base_model import BaseModel
from models.base_model import Base
from models.review import Review
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ Places where user can search for services """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")

    @property
    def reviews(self):
        review_list = []

        for review in list(models.storage.all(Review)):
            if review.place_id == self.id:
                review_list.append(review)
        return review_list
