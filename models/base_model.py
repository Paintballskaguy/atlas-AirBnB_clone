#!/usr/bin/python3


from datetime import datetime
from uuid import uuid4
from models import storage

class BaseModel: 

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            self.id = kwargs.get('id')
            self.created_at = kwargs.get('created_at')
            self.updated_at = kwargs.get('updated_at')
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        # [<class name>] (<self.id>) <self.__dict__>
        obj_str = "[{}] ({}) {}"
        return obj_str.format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        obj_dict = self.__dict__
        obj_dict.update({
            '__class__': type(self).__name__,
            'id': self.id,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at) 
            })
        return self.__dict__
