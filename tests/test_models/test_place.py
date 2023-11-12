#!/usr/bin/python3
"""Unit test for the class Place
"""
import unittest
# import json
from models.place import Place
from models.base_model import BaseModel


class TestPlaceClass(unittest.TestCase):
    """TestPlaceClass test suit for the place class
    """

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        my_place = Place()
        self.assertTrue(isinstance(my_place, BaseModel))

    def test_field_types(self):
        """ Test field attributes of user """
        self.assertTrue(type(Place.city_id) == str)
        self.assertTrue(type(Place.user_id) == str)
        self.assertTrue(type(Place.name) == str)
        self.assertTrue(type(Place.description) == str)
        self.assertTrue(type(Place.number_rooms) == int)
        self.assertTrue(type(Place.number_bathrooms) == int)
        self.assertTrue(type(Place.max_guest) == int)
        self.assertTrue(type(Place.price_by_night) == int)
        self.assertTrue(type(Place.latitude) == float)
        self.assertTrue(type(Place.longitude) == float)


if __name__ == '__main__':
    unittest.main()
