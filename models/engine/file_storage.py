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

    def all(self):
        """ returns the dictionary __objects """
        return (self.__objects)

    def new(self, instance):
        """ add in __objects the obj with key <obj class name>.id """
        if instance:
            key = "{}.{}".format(instance.__class__.__name__, instance.id)
            self.__objects[key] = instance

    def save(self):
        s_dict = {}
        all_dict = FileStorage.__objects
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            for value in all_dict.values():
                key = "{}.{}".format(value.__class__.__name__, value.id)
                s_dict[key] = value.to_dict()
            json.dump(s_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists, otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised) """
        # excutes only if file exists
        if os.path.isfile(FileStorage.__file_path):
            with open(self.__file_path, 'r') as f:
                des_json = json.load(f)
                for key, value in des_json.items():
                    # to separate class name from class id
                    obj_key = key.split('.')
                    # search "__class__": "BaseModel"
                    class_name = obj_key[0]
                    # add in __objects the key, value
                    self.new(eval("{}".format(class_name))(**value))
