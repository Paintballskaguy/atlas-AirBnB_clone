#!/usr/bin/python3


import models
from datetime import datetime, time
from uuid import uuid4


class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = kwargs.get('id')
            created_at = kwargs.get('created_at')
            updated_at = kwargs.get('updated_at')

            if type(created_at) is str:
                self.created_at = datetime.fromisoformat(created_at)
            else:
                self.created_at = datetime.now()

            if type(updated_at) is str:
                self.updated_at = datetime.fromisoformat(updated_at)
            else:
                self.updated_at = datetime.now()

            for key, value in kwargs.items():
                if key not in ['__class__', 'id', 'created_at', 'updated_at']:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        obj_str = "[{}] ({}) {}"
        return obj_str.format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict.update({
            '__class__': self.__class__.__name__,
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
            })
        return obj_dict
