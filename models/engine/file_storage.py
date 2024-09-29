#!/usr/bin/python3


import json, importlib, models.base_model

class FileStorage:

    ######## private class attributes ########
    __file_path = "file.json"
    __objects = {}

    ######## public instance methods ########
    def all(self):
        """ returns a dictionary of objects
        """
        return self.__objects

    def new(self, new_obj):
        """ adds a new object to the dictionary object
        with the key string <class>.<id>
        """
        key = type(new_obj).__name__ 
        key = key + new_obj.id
        self.__objects.update({key: new_obj })

    def save(self):
        """ serializes objects into a json file
        """
        decomp_objects = {}
        for key, obj in self.__objects.items():
            decomp_objects.update({key: obj.to_dict()})

        json_string = json.dumps(decomp_objects)
        try:
            json_file = open(self.__file_path, "w") 
            json_file.write(json_string)
            json_file.close()
        except FileNotFoundError:
            pass

    def reload(self):
        """ deserializes string from a json file into
        a dictionary of objects
        """
        try: 
            json_file = open(self.__file_path, "r") 
            json_string = json_file.read()
            decomp_objects = json.loads(json_string)
            for key, value in decomp_objects.items():
                obj = models.base_model.BaseModel(**value)
                key = type(obj).__name__ + obj.id
                self.__objects.update({key: obj})
        except FileNotFoundError:
            self.__objects = {}
