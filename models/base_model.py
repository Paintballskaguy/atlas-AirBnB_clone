#!/usr/bin/python3

class Base: 

    @attribute
    def id(self):
        return self.__id

    @attribute
    def created_at(self):
        return self.__created_at

    @attribute
    def updated_at(self):
        return self.__updated_at

    def save(self):
        pass

    def to_json(self):
        pass
