#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
import datetime
import uuid


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_unique_ids(self):
        another_base_model = BaseModel()
        self.assertNotEqual(self.base_model.id, another_base_model.id)

    def test_created_at_is_datetime(self):
        test_created = self.base_model.created_at
        self.assertIsInstance(test_created, datetime.datetime)

    def test_updated_at_is_datetime(self):
        test_update = self.base_model.updated_at
        self.assertIsInstance(test_update, datetime.datetime)

    def test_save_method(self):
        original = self.base_model.updated_at
        new = self.base_model.save()
        self.assertNotEqual(original, new)

    def test_to_dict_method(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_str_method(self):
        i_id = self.base_model_id
        idict = self.base_model.__dict__
        self.assertEqual(str(self.base_model), f"[BaseModel] ({i_id}) {idict}")
