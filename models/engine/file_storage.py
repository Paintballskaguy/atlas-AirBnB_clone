#!/usr/bin/python3

import importlib
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from datetime import datetime


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns a dictionary of objects """
        return self.__objects

    def new(self, obj):
        """ adds a new object to the dictionary object with
        the key string <class>.<id>
        """
        key = self.construct_key(obj)
        self.__objects.update({key: obj})

    def save(self):
        """ serializes objects into a json file """
        decomposed = {}
        for key, obj in self.__objects.items():
            obj_dict = obj.to_dict()
            decomposed.update({key: obj_dict})

        json_string = json.dumps(decomposed)
        try:
            json_file = open(self.__file_path, "w")
            json_file.write(json_string)
            json_file.close()
        except FileNotFoundError:
            pass

    def reload(self):
        """Deserializes objects from a JSON file."""
        try:
            json_file = open(self.__file_path, 'r')
            json_data = json_file.read()
            json_file.close()
            extracted_data = json.loads(json_data)

            for key, value in extracted_data.items():
                model_class = value['__class__']
                model_class = globals().get(model_class)
                if model_class is not None:
                    obj = model_class(**value)
                    self.__objects.update({key: obj})

        except FileNotFoundError:
            pass

    def construct_key(self, obj):
        """ helper method to construct key for object dictionary """
        return type(obj).__name__ + "." + obj.id
