#!/usr/bin/python3
"""Test module for BaseModel class for the airbnb_clone project"""

from models.base_model import BaseModel
from datetime import datetime
import unittest
import os


class TestBaseModel(unittest.TestCase):
    """Test module for Basemodel class"""

    @classmethod
    def setUpClass(cls):
        """Set up instances for testing"""
        cls.obj1 = BaseModel()
        cls.obj2 = BaseModel()

        """copy storage file as tests will modify file"""
        os.system('cp file.json copy_file.json')

    @classmethod
    def tearDownClass(cls):
        """clean up action to be taken once tests are done"""

        """restore storage file as it were before tests were run"""
        os.system('rm file.json')
        os.system('cp copy_file.json file.json')
        os.system('rm copy_file.json')

    def test_instantiation(self):
        """Tests instantiation of a BaseModel instance"""
        self.assertIsInstance(TestBaseModel.obj1, BaseModel)
        self.assertIsInstance(TestBaseModel.obj2, BaseModel)

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
        my_dict = TestBaseModel.obj1.to_dict()
        self.obj = BaseModel(**my_dict)

        """check if BaseModel instance created using **kwargs"""
        self.assertIsInstance(self.obj, BaseModel)

        """check if public instance attributes are equal"""
        self.assertEqual(TestBaseModel.obj1.id, self.obj.id)
        self.assertEqual(TestBaseModel.obj1.created_at, self.obj.created_at)
        self.assertEqual(TestBaseModel.obj1.updated_at, self.obj.updated_at)

        """check if one instance is the same as the other, ie. share same
        memory location and equal"""
        self.assertNotEqual(TestBaseModel.obj1, self.obj)

    def test_type_of_public_instance_attributes(self):
        """Tests public instance attributes of a BaseModel instance"""
        self.assertIsInstance(TestBaseModel.obj1.id, str)
        self.assertIsInstance(TestBaseModel.obj2.id, str)
        self.assertIsInstance(TestBaseModel.obj1.created_at, datetime)
        self.assertIsInstance(TestBaseModel.obj2.created_at, datetime)
        self.assertIsInstance(TestBaseModel.obj1.updated_at, datetime)
        self.assertIsInstance(TestBaseModel.obj2.updated_at, datetime)

    def test_save_instance_method(self):
        """Tests the instance method save"""
        my_obj_updated_at = TestBaseModel.obj1.updated_at
        TestBaseModel.obj1.save()
        self.assertNotEqual(my_obj_updated_at, TestBaseModel.obj1.updated_at)

    def test_to_dict_instance_method(self):
        """Tests the instance method to_dict"""
        self.assertIsInstance(TestBaseModel.obj1.to_dict(), dict)
        my_dict = TestBaseModel.obj1.to_dict()
        self.assertIsInstance(my_dict['created_at'], str)
        self.assertIsInstance(my_dict['updated_at'], str)
        self.assertIn('__class__', my_dict.keys())

    def test_if_two_objects_are_the_same(self):
        """Test if two objects are the same"""
        self.assertNotEqual(TestBaseModel.obj1, TestBaseModel.obj2)

    def test_str_instance_method(self):
        """Tests the __str__ instance method"""
        self.assertIsInstance(TestBaseModel.obj1.__str__(), str)


if __name__ == '__main__':
    unittest.main()
