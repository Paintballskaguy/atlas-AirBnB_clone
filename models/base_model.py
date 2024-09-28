#!/usr/bin/python3


from datetime import datetime
from uuid import uuid4

class BaseModel: 

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """ [<class name>] (<self.id>) <self.__dict__>
        """
        obj_str = "[{}] ({}) {}"
        return obj_str.format(type(self).__name__, self.id, self.__dict__)

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def created_at(self):
        return self.__created_at

    @property
    def updated_at(self):
        return self.__updated_at

    @id.setter
    def id(self, new):
        self.__id = new

    @name.setter
    def name(self, new):
        self.__name = new

    @created_at.setter
    def created_at(self, new):
        self.__created_at = new

    @updated_at.setter
    def updated_at(self, new):
        self.__updated_at = new

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__
        obj_dict.update({'__class__': type(self).__name__})
        obj_dict.update({'id': self.id})
        obj_dict.update({'created_at': datetime.isoformat(self.created_at)})
        obj_dict.update({'updated_at': datetime.isoformat(self.updated_at)})
        return self.__dict__

    def to_json(self):
        pass
