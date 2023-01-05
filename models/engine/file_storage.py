#!/usr/bin/python3
""" the storage engine """
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """ serializes instances to a JSON file and deserializes
    JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """ returns the dictionary __objects if it's None
            else returns the list of objects of one type class
        """
        if cls is None:
            return (self.__objects)
        else:
            my_dict = {}
            for key, value in self.__objects.items():
                if cls in key:
                    my_dcit[key] = value
            return my_dict

    def new(self, instance):
        """ add in __objects the obj with key <obj class name>.id """
        if instance:
            key = "{}.{}".format(instance.__class__.__name__, instance.id)
            self.__objects[key] = instance

    def save(self):
        s_dict = {}
        s_dict.update(FileStorage.__objects)
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            for key, value in s_dict.items():
                s_dict[key] = value.to_dict()
            json.dump(s_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists, otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised) """
        # excutes only if file exists
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            with open(self.__file_path, 'r') as f:
                temp = json.load(f)
                for key, value in temp.items():
                    self.all()[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ Delete the obj from __objects if it's insied
            if obj is equal to None, the method should
            not do anything
        """
        if obj is not None:
            if obj in FileStorage.__objects:
                del FileStroage.__objects[obj]
