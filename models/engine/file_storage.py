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
        key = self.construct_key(new_obj)
        self.__objects.update({ key: new_obj })

    def save(self):
        """ serializes objects into a json file
        """
        decomp_objects = {}
        for key, obj in self.__objects.items():
            obj_dict = obj.to_dict()
            decomp_objects.update({ key: obj_dict })

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
            json_file.close()

            decomp_objects = json.loads(json_string)
            for key, value in decomp_objects.items():
                obj = models.base_model.BaseModel(**value)
                key = self.construct_key(obj)
                self.__objects.update({key: obj})
        except FileNotFoundError:
            self.__objects = {}

    def construct_key(self, obj):
        return type(obj).__name__ + "." + obj.id
