#!/usr/bin/python3


import json

class FileStorage:


    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = type(obj).__name__ 
        key = key + obj.id
        self.__objects.update({key: str(obj) })
 
    def save(self):
        json_string = json.dumps(self.__objects)
        try: 
            json_file = open(self.__file_path, "w") 
            json_file.write(json_string)
        except FileNotFoundError:
            pass
  
    def reload(self):
        try: 
            json_file = open(self.__file_path, "r") 
            json_string = json_file.read()
            self.__objects = json.loads(json_string)
        except FileNotFoundError:
            self.__objects = {}
