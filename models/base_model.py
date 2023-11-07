#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    """base models which hold the common atributes 
    (id, updated_at, created_at )and function (save, to_dict...)
	"""

    def __init__(self, *args, **kwargs):

        dformat = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    """ Review
                    hna you checked for created_at or updated_at keys
                    but fl'assignment darti 4ir self.created_at but updated_at mabants liya
                    """
                    self.created_at = datetime.strptime(value, dformat)
                elif key == '__class__':
                    #dead code
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.created_at.isoformat()

        return obj_dict
