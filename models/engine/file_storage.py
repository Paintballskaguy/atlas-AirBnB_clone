#!/usr/bin/python3


import json
from models.base_model import BaseModel

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
        repr_dict = {}
        for obj in self.objects:
            repr_dict.update(obj.to_dict())

        json_string = json.dumps(repr_dict)
        try:
            json_file = open(self.file_path, "w") 
            json_file.write(json_string)
        except FileNotFoundError:
            pass

    def reload(self):
        try: 
            json_file = open(self.file_path, "r") 
            json_string = json_file.read()
            json_dict = json.loads(json_string)
            for representation in json_dict:
                reconstruction = BaseModel(**representation)
                key = type(reconstruction).__name__ + reconstruction.id
                self.objects.update({key: reconstruction})
        except FileNotFoundError:
            self.objects = {}
