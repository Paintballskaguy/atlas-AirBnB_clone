#!/usr/bin/python3

import importlib
import json
from models.base_model import BaseModel
from datetime import datetime

class FileStorage:
    ######## private class attributes ########
    __file_path = "file.json"
    __objects = {}

    ######## public instance methods ########
    def all(self):
        """ returns a dictionary of objects """
        return self.__objects

    def new(self, obj):
        """ adds a new object to the dictionary object with the key string <class>.<id> """
        key = self.construct_key(obj)
        self.__objects[key] = obj

    def save(self):
        """ serializes objects into a json file """
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    # DO NOT EDIT
    # using `with` with try is redundant
    def reload(self):
        """Deserializes objects from a JSON file."""
        try:
            json_file = open(self.__file_path, 'r') 
            json_data = json_file.read()
            json_file.close()
            extracted = json.loads(json_data)

            for key, value in extracted.items():
                model_class= value['__class__']
                model_class = globals().get(class_name)
                if model_class is not None:
                    obj = model_class(**value)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass

    def construct_key(self, obj):
        """ helper method to construct key for object dictionary """
        return type(obj).__name__ + "." + obj.id
