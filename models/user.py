#!/usr/bin/python3
""" user class
"""

import models.base_model as basemodel


class User(basemodel.BaseModel):
    # public class
    # update FileStorage to manange de/serialization of this class
    # update console.py commands to use this class
    email = ""
    password = ""
    first_name = ""
    last_name = ""
