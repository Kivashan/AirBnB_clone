#!/usr/bin/python3
"""Test module for BaseModel class for the airbnb_clone project"""

from models.base_model import BaseModel
from datetime import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """Test module for Basemodel class"""

    def setUp(self):
        """Set up instances for testing"""
        self.obj1 = BaseModel()
        self.obj2 = BaseModel()

    def tearDown(self):
        """clean up action to be taken once tests are done"""
        pass

    def test_instantiation(self):
        """Tests instantiation of a BaseModel instance"""
        self.assertIsInstance(self.obj1, BaseModel)
        self.assertIsInstance(self.obj2, BaseModel)

    def test_instantiation_with_args(self):
        """Tests instantiation of a BaseModel instance with *args. *args are
        not used in intialization by the __init__ method. Instead BaseModel is
        called as if *args were not passed and will create a valid instance of
        BaseModel"""
        self.obj = BaseModel(25)
        self.assertIsInstance(self.obj, BaseModel)
        self.assertIsInstance(self.obj.id, str)
        self.assertIsInstance(self.obj.created_at, datetime)
        self.assertIsInstance(self.obj.updated_at, datetime)

    def test_instantiation_with_kwargs(self):
        """Tests instantiation of a BaseModel instance with **kwargs, if a
        dictionary representation of an object is passed to BaseModel. The
        object should be created with values equal to that of the dictionary
        representation, hence recreating the object"""
        my_dict = self.obj1.to_dict()
        self.obj = BaseModel(**my_dict)

        """check if BaseModel instance created using **kwargs"""
        self.assertIsInstance(self.obj, BaseModel)

        """check if public instance attributes are equal"""
        self.assertEqual(self.obj1.id, self.obj.id)
        self.assertEqual(self.obj1.created_at, self.obj.created_at)
        self.assertEqual(self.obj1.updated_at, self.obj.updated_at)

        """check if one instance is the same as the other, ie. share same
        memory location and equal"""
        self.assertNotEqual(self.obj1, self.obj)

    def test_type_of_public_instance_attributes(self):
        """Tests public instance attributes of a BaseModel instance"""
        self.assertIsInstance(self.obj1.id, str)
        self.assertIsInstance(self.obj2.id, str)
        self.assertIsInstance(self.obj1.created_at, datetime)
        self.assertIsInstance(self.obj2.created_at, datetime)
        self.assertIsInstance(self.obj1.updated_at, datetime)
        self.assertIsInstance(self.obj2.updated_at, datetime)

    def test_save_instance_method(self):
        """Tests the instance method save"""
        my_obj_updated_at = self.obj1.updated_at
        self.obj1.save()
        self.assertNotEqual(my_obj_updated_at, self.obj1.updated_at)

    def test_to_dict_instance_method(self):
        """Tests the instance method to_dict"""
        self.assertIsInstance(self.obj1.to_dict(), dict)
        my_dict = self.obj1.to_dict()
        self.assertIsInstance(my_dict['created_at'], str)
        self.assertIsInstance(my_dict['updated_at'], str)
        self.assertIn('__class__', my_dict.keys())

    def test_if_two_objects_are_the_same(self):
        """Test if two objects are the same"""
        self.assertNotEqual(self.obj1, self.obj2)


if __name__ == '__main__':
    unittest.main()
