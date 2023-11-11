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


class FileStorageTests(unittest.TestCase):
    """ all File Storage Tests """

    my_model = BaseModel()

    def test__objects(self):
            self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all(self):
            self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
            base_model = BaseModel()
            models.storage.new(base_model)
            models.storage.new(base_model)
            self.assertIn("BaseModel." + base_model.id,
                          models.storage.all().keys())

    def test_save(self):
            self.my_model.save()
            self.assertEqual(
                os.path.exists(models.storage._FileStorage__file_path),
                True)

    def test_reload(self):
            base_model = BaseModel()
            models.storage.new(base_model)
            models.storage.save()
            models.storage.reload()
            objs = FileStorage._FileStorage__objects
            self.assertIn("BaseModel." + base_model.id, objs)

    def test_init(self):
            self.assertIsInstance(models.storage, FileStorage)

    def test_save(self):
            with self.assertRaises(TypeError):
                models.storage.save(None)


if __name__ == "__main__":
    unittest.main()
