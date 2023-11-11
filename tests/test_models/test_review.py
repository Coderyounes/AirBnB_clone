#!/usr/bin/python3
"""Unit test for the file storage class
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReviewClass(unittest.TestCase):
    """TestReviewClass test suite for the use
    """

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        my_Review = Review()
        self.assertTrue(isinstance(my_Review, BaseModel))

    def test_field_types(self):
        """ Test field attributes of user """
        my_Review = Review()
        self.assertTrue(type(my_Review.place_id) == str)
        self.assertTrue(type(my_Review.user_id) == str)
        self.assertTrue(type(my_Review.text) == str)


if __name__ == '__main__':
    unittest.main()
