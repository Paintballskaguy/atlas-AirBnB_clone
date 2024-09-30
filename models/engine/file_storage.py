#!/usr/bin/python3


import json, importlib
from models.base_model import BaseModel

class FileStorage:

    ######## private class attributes ########
    __file_path = "file.json"
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
        with open(self.__file_path, 'w') as json_file:
            obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(obj_dict, json_file)

    def reload(self):
        """ deserializes string from a json file into
        a dictionary of objects
        """
        try: 
            with open(self.__file_path, 'r') as json_file:
                decomp_objects = json.load(json_file)
                for key, value in decomp_objects.items():
                    class_name = value['__class__']
                    if class_name == "BaseModel":
                        obj = BaseModel(**value)
                    else:
                        module_name = 'models.' + class_name.lower()
                        try:
                                module = importlib.import_module(module_name)
                                cls = getattr(module, class_name)
                                obj = cls(**value)
                        except ModuleNotFoundError:
                            print(f"Error: Could not find module for class {class_name}")
                            continue
                        except AttributeError:
                            print(f"Error: Could not find class {class_name}")
                            continue
                self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def construct_key(self, obj):
        return type(obj).__name__ + "." + obj.id
