#!/usr/bin/python3

import models.engine.file_storage as fs

model_classes = {
        'BaseModel': models.base_model.BaseModel,
        'User': models.user.User,
        'Amenity': models.amenity.Amenity,
        'City': models.city.City,
        'Place': models.place.Place,
        'State': models.state.State,
        'Review': models.review.Review
        }

storage = fs.FileStorage()
storage.reload()
