#!/usr/bin/python3
""" testing module
all()
new
save
reload
init
save(self)

"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
import os


class FileStorageTests(unittest.TestCase):
    """ all File Storage Tests """

    def test_type_objects(self):
            """ test __objects type """
            self.assertEqual(type(models.storage.all()), dict)
            # self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all(self):
            """ test all function """
            self.assertEqual(type(models.storage.all()), dict)
            # self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
            """ test new functions """
            base_model = BaseModel()
            models.storage.new(base_model)
            models.storage.new(base_model)
            self.assertIn("BaseModel." + base_model.id,
                          models.storage.all().keys())

    def test_save(self):
            """ test save functions """
            self.my_model.save()
            self.assertEqual(
                os.path.exists(models.storage._FileStorage__file_path),
                True)

    def test_reload(self):
            """ test reload function """
            base_model = BaseModel()
            models.storage.new(base_model)
            models.storage.save()
            models.storage.reload()
            objs = FileStorage._FileStorage__objects
            self.assertIn("BaseModel." + base_model.id, objs)

    def test_init(self):
            """ test __init__ function """
            self.assertIsInstance(models.storage, FileStorage)

    def test_save(self):
            """ test save with an arg """
            with self.assertRaises(TypeError):
                models.storage.save(None)


if __name__ == "__main__":
    unittest.main()
