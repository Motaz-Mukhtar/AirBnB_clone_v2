#!/usr/bin/python3

"""Unittest FileStorage"""

import unittest
import os

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class test_filestore(unittest.TestCase):
    """test file_storage"""
    @classmethod
    def setup(self):
        self.review1 = Review()
        self.review1.user_id = "Adam"
        self.review1.place_id = "5d55d5"
        self.review1.text = "it was anice place"

    def test_new(self):
        file1 = FileStorage()
        inst_dic = file1.all()
        adam = User()
        adam.id = 55889
        adam.name = "Adam"
        file1.new(adam)
        key = adam.__class__.__name__ + "." + str(adam.id)
        self.assertIsNotNone(inst_dic[key])

    def test_all(self):
        file2 = FileStorage()
        instances_dic = file2.all()
        self.assertIsNotNone(inst_dic)
        self.assertEqual(type(inst_dic), dict)
        self.assertIs(inst_dic, file2._FileStorage__objects)

    def test_reload(self):
        file3 = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass

if __name__ = "__main__":
    unittest.main()
