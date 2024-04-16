#!/usr/bin/python3
"""A module containing the FileStorage class, this module handles the
serialization and deserializatiton of Objects to Json strings and vice versa
and saves and loads this information to and from a Json file"""

from models.base_model import BaseModel
import json


class FileStorage():
    """FileStorage class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """adds the given object to __objects"""
        obj_dict = obj.to_dict()
        key = "{}.{}".format(obj_dict['__class__'], obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:

            """make a copy of the dictionary so that any changes made do not
            affect original dictionary data"""
            objs_copy = FileStorage.__objects.copy()

            """convert objects in objs_copy to dictionary representation by
            calling obj.to_dict() method before serializing data"""
            for key, value in objs_copy.items():
                objs_copy[key] = value.to_dict()
            json.dump(objs_copy, f)

    def reload(self):
        """ deserializes the JSON file to __objects"""

        """Ensure that __objects is empty before deserialization, this ensures
        that reload() can be called multiple times in the same session
        without duplicating data read from FileStorage.__file_path"""
        FileStorage.__objects = {}

        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                file_contents = json.load(f)

                """convert values in file_contents from dictionary
                representations of objects to actual objects"""
            for key, value in file_contents.items():
                FileStorage.__objects[key] = BaseModel(**value)
        except Exception:
            pass
