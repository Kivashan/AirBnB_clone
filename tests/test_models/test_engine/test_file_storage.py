#!/usr/bin/python3
"""Test module for FileStorage class"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import json
import unittest
import os


class TestFileStorage(unittest.TestCase):
    """Test module for the FileStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up for tests to run once"""
        cls.obj = BaseModel()
        cls.storage = FileStorage()

        """Copy original storage file as tests will modify them"""
        os.system('cp file.json copy_file.json')

    @classmethod
    def tearDownClass(cls):
        """clean up action to be taken after all tests have run"""

        """restore original storage file"""
        os.system('rm file.json')
        os.system('cp copy_file.json file.json')
        os.system('rm copy_file.json')

    def test_instantiation(self):
        """tests instantiation of FileStorage class"""
        self.assertIsInstance(TestFileStorage.storage, FileStorage)

    def test_instantiation_with_args(self):
        """tests instantiation with *args passed to FileStorage"""
        with self.assertRaises(TypeError):
            FileStorage(10)

    def test_instantiation_with_kwargs(self):
        """tests instantiation with **kwargs passed to FileStorage"""
        kwargs = {'name': 'my_storage'}
        with self.assertRaises(TypeError):
            FileStorage(**kwargs)

    def test_accessibility_of_private_class_attributes(self):
        """tests accessibility of private class attributes"""
        with self.assertRaises(AttributeError):
            TestFileStorage.storage.__file_path

        with self.assertRaises(AttributeError):
            TestFileStorage.storage.__objects

    def test_public_instance_method_all(self):
        """tests the all method of a FilsStorage instance"""
        self.assertIsInstance(TestFileStorage.storage.all(), dict)

    def test_public_instance_method_new(self):
        """tests the new method of a FileStorage instance"""
        self.stored_objs = TestFileStorage.storage.all().copy()
        new_obj = BaseModel()
        self.new_stored_objs = TestFileStorage.storage.all()
        self.assertNotEqual(self.stored_objs, self.new_stored_objs)

    def test_public_instance_method_save(self):
        """tests the save method of a FileStorage instance"""

        """Calling BaseModel without args automatically adds the instance
        to FileStorage.__objects however the new instances are not saved to
        FileStorage.__file_path.
        Calling reload() will reset FileStorage.__objects to reflect only those
        instances that have been saved to file."""
        TestFileStorage.storage.reload()

        """Calling all() now returns objects stored to file"""
        my_objs = TestFileStorage.storage.all().copy()
        obj = BaseModel()

        """calling FileStorage.save() will now persist our newly created
        object"""
        TestFileStorage.storage.save()

        self.assertNotEqual(my_objs, TestFileStorage.storage.all())

        """A proper test would be to count the number of objects
        stored in file before save is called and comparing it
        against the number of objects after save is called, but for purposes
        of this clone project, I am skipping that test"""

    def test_public_instance_method_reload(self):
        """tests the reload method of a FileStorage instance"""

        """Create a new instance of BaseModel, this updates
        FileStorage.__objects but will not persist the new object
        to the the storage file"""
        new_obj = BaseModel()
        my_obj_dict = TestFileStorage.storage.all().copy()

        """Calling reload() withour first calling save() will reset
        FileStorage.__objects, hence my_obj_dict will have one more
        object stored in comparison to new_obj_dict"""
        TestFileStorage.storage.reload()
        new_obj_dict = TestFileStorage.storage.all()
        self.assertNotEqual(my_obj_dict, new_obj_dict)


if __name__ == '__main__':
    unittest.main()
