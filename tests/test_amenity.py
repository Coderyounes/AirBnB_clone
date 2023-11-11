#!/usr/bin/python3
"""Unit test for the file storage class
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
import os


class TestAmenityClass(unittest.TestCase):
    """TestAmenityClass test for the inheretit class
    """

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        my_Amenity = Amenity()
        self.assertTrue(isinstance(my_Amenity, BaseModel))

    def test_field_types(self):
        """ Test field attributes of user """
        my_Amenity = Amenity()
        self.assertTrue(type(my_Amenity.name) == str)


if __name__ == '__main__':
    unittest.main()
