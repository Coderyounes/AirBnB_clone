#!/usr/bin/python3

import uuid
import datetime


class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        classname = self.__class__.__name__
        return f"[{classname}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = str(datetime.datetime.now())

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__

        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.created_at.isoformat()

        return obj_dict
