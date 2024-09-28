#!/usr/bin/python3


import json

class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return self.__objects

    def new(self, obj):
        key = type(obj).__name__ 
        key = key + obj.id
        self.__objects.update({key: str(obj) })
 
    def save(self):
        # serialize __objects to json in __file_path
        pass
  
    def reload(self):
        # de-serialize __objects from json in __file_path if it exist
        pass
