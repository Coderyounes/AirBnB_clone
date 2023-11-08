#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        s_obj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(s_obj, f)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="UTF-8") as f:
                data = json.load(f)
            for key, value in data.items():
                class_name, obj_id = key.split('.')
                class_obj = eval(class_name)
                instance = class_obj(**value)
                self.__objects[key] = instance
        except FileNotFoundError:
            pass
