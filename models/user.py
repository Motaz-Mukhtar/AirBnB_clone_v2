#!/usr/bin/python3
"""User Class File"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class That inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
