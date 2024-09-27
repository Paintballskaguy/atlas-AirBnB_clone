#!/usr/bin/python3


from uuid import uuid4

class BaseModel: 

    def __init__(self):
        self.id = str(uuid4())
        print(self.id)

    def __str__(self):
        """ [<class name>] (<self.id>) <self.__dict__>
        """
        obj_str = "[{}] ({}) {}"
        return obj_str.format(type(self), self.id, self.__dict__)

    @property
    def id(self):
        return self.__id

    @property
    def created_at(self):
        return self.__created_at

    @property
    def updated_at(self):
        return self.__updated_at

    @id.setter
    def id(self, new):
        self.__id = new

    @created_at.setter
    def created_at(self, new):
        self.__created_at = new

    @created_at.setter
    def updated_at(self, new):
        self.__updated_at = new

    def save(self):
        pass

    def to_json(self):
        pass
