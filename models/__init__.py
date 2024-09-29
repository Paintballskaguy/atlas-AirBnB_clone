#!/usr/bin/python3

import models.engine.file_storage as fs
# from models.base_model import BaseModel

valid_classes = (
        'BaseModel', 
        'User',
        'Amenity',
        'City',
        'Place',
        'State',
        'Review'
        )

storage = fs.FileStorage()
storage.reload()
