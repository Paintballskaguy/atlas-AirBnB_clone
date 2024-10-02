#!/usr/bin/python3
""" user class
"""

import models.base_model as basemodel


class User(basemodel.BaseModel):
    # public class
    # update FileStorage to manange de/serialization of this class
    # update console.py commands to use this class
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(*args, **kwargs)
            self.email = kwargs.get('email')
            self.password = kwargs.get('password')
            self.first_name = kwargs.get('first_name')
            self.last_name = kwargs.get('last_name')
        else:
            super().__init__()
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
