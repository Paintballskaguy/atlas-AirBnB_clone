#!/usr/bin/python3


import json, importlib
from models.base_model import BaseModel

class FileStorage:

    ######## private class attributes ########
    __file_path = "test_file.json"
    __objects = {}

    ######## public instance methods ########
    def all(self):
        """ returns a dictionary of objects
        """
        print(f"Returning all objects from storage: {self.__objects}")
        return self.__objects

    def new(self, obj):
        """ adds a new object to the dictionary object
        with the key string <class>.<id>
        """
        key = self.construct_key(obj)
        print(f"Adding object to storage: {key}")
        self.__objects[key] = obj
        print(f"Storage after adding object: {self.__objects}")

    def save(self):
        """ serializes objects into a json file
        """
        with open(self.test_file, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """ deserializes string from a json file into
        a dictionary of objects
        """
        try: 
            with open(self.test_file, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value['__class__']
                    cls = globals()[class_name]
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def construct_key(self, obj):
        return type(obj).__name__ + "." + obj.id
