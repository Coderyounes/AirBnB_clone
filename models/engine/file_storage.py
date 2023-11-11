#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage():
    """ file storage system """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ retrieve all objects """
        return self.__objects

    def new(self, obj):
        """create new insance

        Args:
            obj (BaseModel): base model instance
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ save new instance """
        s_obj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(s_obj, f)

    def reload(self):
        """ reload existed instances """
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                data = json.load(f)
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                class_obj = globals()[class_name]
                instance = class_obj(**value)
                self.__objects[key] = instance
        except FileNotFoundError:
            pass
