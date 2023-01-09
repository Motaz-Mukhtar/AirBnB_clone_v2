#!/usr/bin/python3
""" Test File for DBStorage class """
import models
import pep8
from os import getenv
import unittest
import pep8
import MySQLdb
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine


class TestDBStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if type(models.storage) == DBStorage:
            cls.storage = DBStorage()
            Base.metadata.create_all(cls.storage._DBStorage__engine)
            Session = sessionmaker(bind=cls.storage._DBStorage__engine)
            cls.storage._DBStorage__session = Session()
            cls.user = User(email="jmaes@alxswe.com", password="james123")
            cls.storage._DBStorage__session.add(cls.user)
            cls.state = State(name="jack")
            cls.storage._DBStorage__session.add(cls.state)
            cls.city = City(name="Joe", state_id=cls.state.id)
            cls.storage._DBStorage__session.add(cls.city)
            cls.amenity = Amenity(name="Wifi")
            cls.storage._DBStorage__session.add(cls.amenity)
            cls.place = Place(city_id=cls.city.id, user_id=cls.user.id, name="jack"
                              ,number_rooms=3, number_bathrooms=2, max_guest=12
                              ,price_by_night=200)
            cls.storage._DBStorage__session.add(cls.place)
            cls.review = Review("Reviews", place_id=cls.place.id
                                ,user_id=cls.user.id)
            cls.storage._DBStorage__session.commit()

    @classmethod
    def tearDownClass(self):
        if type(models.storage) == DBStorage:
            self.storage._DBStorage__session.delete(self.user)
            self.storage._DBStorage__session.delete(self.city)
            self.storage._DBStorage__session.delete(self.review)
            self.storage._DBStorage__session.delete(self.place)
            self.storage._DBStorage__session.delete(self.amenity)
            self.storage._DBStorage__session.delete(self.state)
            self.storage._DBStorage__session.commit()

            del self.user
            del self.city
            del self.place
            del self.amenity
            del self.state
            del self.storage

    def test_doc_string(self):
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
    
    def test_attributes(self):
        self.assertTrue(hasattr(DBStorage, "all"))
        self.assertTrue(hasattr(DBStorage, "delete"))
        self.assertTrue(hasattr(DBStorage, "new"))
        self.assertTrue(hasattr(DBStorage, "reload"))
        self.assertTrue(hasattr(DBStorage, "save"))
        self.assertTrue(hasattr(DBStorage, "engine"))
        self.assertTrue(hasattr(DBStorage, "session"))