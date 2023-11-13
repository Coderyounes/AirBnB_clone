#!/usr/bin/python3
"""Unit test for the class city
"""
import unittest
from models import city
from models.city import City
from models.base_model import BaseModel


class TestCityClass(unittest.TestCase):
    """TestCityClass test for the city class
    """

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        my_city = City()
        self.assertTrue(isinstance(my_city, BaseModel))

    def test_field_types(self):
        """ Test field attributes of user """
        my_city = City()
        self.assertTrue(type(my_city.name) == str)
        self.assertTrue(type(my_city.state_id) == str)


if __name__ == '__main__':
    unittest.main()
