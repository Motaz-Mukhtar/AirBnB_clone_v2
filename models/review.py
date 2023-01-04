#!/usr/bin/python3
""" review class file """
from models.base_model import BaseModel


class Review(BaseModel):
    """ review of the user """
    place_id = ''
    user_id = ''
    text = ''
