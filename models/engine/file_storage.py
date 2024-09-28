#!/usr/bin/python3


import json
from os import path

class FileStorage:


    def __init__(self):
        self.file_path = "file.json"
        self.objects = {}

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
        return self.objects

    def new(self, obj):
        key = type(obj).__name__ 
        key = key + obj.id
        self.objects.update({key: str(obj) })
 
    def save(self):
        json_string = json.dumps(self.objects)
        try: 
            json_file = open(self.file_path, "w") 
            json_file.write(json_string)
        except FileNotFoundError:
            pass
  
    def reload(self):
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r') as json_file:
                obj_dict = json.load(json_file)
                from models.base_model import BaseModel
                for key, value in obj_dict.items():
                    cls_name = value['__class__']
                    if cls_name == "BaseModel":
                        self.__object[key] = BaseModel(**value)
