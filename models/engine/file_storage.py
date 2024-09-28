#!/usr/bin/python3

import json
from os import path

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file back to instances.
    """

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    @property
    def file_path(self):
        return self.__file_path

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, new):
        self.__objects = new

    @file_path.setter
    def file_path(self, new):
        self.__file_path = new

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj.to_dict()  # Store dictionary representation of the object

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (if the file exists).
        If the file doesn’t exist, do nothing.
        """
        if path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as json_file:
                    obj_dict = json.load(json_file)
                    from models.base_model import BaseModel
                    for key, value in obj_dict.items():
                        cls_name = value['__class__']
                        if cls_name == "BaseModel":
                            self.__objects[key] = BaseModel(**value)  # Correctly store BaseModel instance
            except FileNotFoundError:
                pass
