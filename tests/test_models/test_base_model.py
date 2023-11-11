#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classes:
    TestBaseModel_self_id*
    TestBaseModel_self_created_at*
    TestBaseModel__str__(self)*
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
        """
        testing BaseModel
        """

        def test_self_id(self):
                base_model1 = BaseModel()
                base_model2 = BaseModel()
                self.assertNotEqual(base_model1, base_model2)

        def test_created_at(self):
                base_model1 = BaseModel()
                self.assertIsInstance(base_model1.created_at, datetime)

        def test__str_(self):
                b1 = BaseModel()
                my_str = b1.__str__()
                self.assertIn("[BaseModel]", my_str)
                self.assertIn("id", my_str)
                self.assertIn("created_at", my_str)
                self.assertIn("updated_at", my_str)

        def test_to_dict(self):
                base_model = BaseModel()
                self.assertIn("id", base_model.to_dict())
                self.assertIn("created_at", base_model.to_dict())
                self.assertIn("updated_at", base_model.to_dict())
                self.assertIn("__class__", base_model.to_dict())

        def test_save(self):
                """ testing save() method on base_model"""
                base_model = BaseModel()
                cur_updated_at1 = base_model.updated_at
                base_model.save()
                cur_updated_at2 = base_model.updated_at
                self.assertNotEqual(cur_updated_at1, cur_updated_at2)


if __name__ == "__main__":
    unittest.main()
