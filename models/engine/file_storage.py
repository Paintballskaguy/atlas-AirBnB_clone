#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:
    ######## private class attributes ########
    __file_path = "file.json"
    __objects = {}

    ######## public instance methods ########
    def all(self):
        """ returns a dictionary of objects """
        print(f"Returning all objects from storage: {self.__objects}")
        return self.__objects

    def new(self, obj):
        """ adds a new object to the dictionary object with the key string <class>.<id> """
        key = self.construct_key(obj)
        print(f"Adding object to storage: {key}")
        self.__objects[key] = obj
        print(f"Storage after adding object: {self.__objects}")

    def save(self):
        """ serializes objects into a json file """
        print(f"Saving objects to {self.__file_path}")
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """ deserializes string from a json file into a dictionary of objects """
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value['__class__']
                    cls = globals()[class_name]  # Convert class name to class reference
                    obj = cls(**value)
                    self.__objects[key] = obj
            print(f"Data loaded from {self.__file_path}: {self.__objects}")
        except FileNotFoundError:
            print(f"{self.__file_path} not found. No data loaded.")
            pass

    def construct_key(self, obj):
        """ helper method to construct key for object dictionary """
        return type(obj).__name__ + "." + obj.id
