#!/usr/bin/python3
"""Unit test for the file storage class
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestStateClass(unittest.TestCase):
    """TestStateClass checks for the use of
    """

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        my_state = State()
        self.assertTrue(isinstance(my_state, BaseModel))

    def test_field_types(self):
        """ Test field attributes of user """
        my_state = State()
        self.assertTrue(type(my_state.name) == str)


if __name__ == '__main__':
    unittest.main()
