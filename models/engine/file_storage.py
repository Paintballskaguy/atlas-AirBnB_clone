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
            decomp_objects[key] = obj_dict

        with open(self.__file_path, 'w') as json_file:
            json.dump(decomp_objects, json_file)

    def reload(self):
        """ deserializes string from a json file into
        a dictionary of objects
        """
        try: 
            with open(self.__file_path, 'r') as json_file:
                decomp_objects = json.load(json_file)
                for key, value in decomp_objects.items():
                    class_name = value['__class__']
                    module = importlib.import_module(f'models.{class_name.lower()}')
                    cls = getattr(module, class_name)
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def construct_key(self, obj):
        return type(obj).__name__ + "." + obj.id
