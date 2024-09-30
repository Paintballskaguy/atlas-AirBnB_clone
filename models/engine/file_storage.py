#!/usr/bin/python3

import importlib
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
                    cls = self.get_class_by_name(class_name)
                    if cls:
                        obj = cls(**value)
                        self.__objects[key] = obj
                    else:
                        print(f"Class {class_name} not found.")
        except FileNotFoundError:
            print(f"{self.__file_path} not found. No data loaded.")
            pass
        
    def get_class_by_name(self, class_name):
        """Dynamically fetch the class by name from models."""
        try:
            module_name = f"models.{class_name.lower()}"
            module = importlib.import_module(module_name)

            cls = getattr(module, class_name)
            return cls
        except (ModuleNotFoundError, AttributeError) as e:
            print(f"Error loading class {class_name}: {e}")
            return None

    def construct_key(self, obj):
        """ helper method to construct key for object dictionary """
        return type(obj).__name__ + "." + obj.id
