#!/usr/bin/python3
"""Module containing the BaseModel class"""

import uuid
from datetime import datetime


class BaseModel():
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Initialization for BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.fromisoformat(value))
                elif key == '__class__':
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of BaseModel object"""
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """Saves the instance and modifies the updated_at attribute"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """returns a dictionary reprsentation of an instance"""
        my_dict = self.__dict__.copy()
        for key, value in my_dict.items():
            if key in ['created_at', 'updated_at']:
                my_dict[key] = value.isoformat()
        my_dict['__class__'] = 'BaseModel'
        return my_dict


if __name__ == '__main__':
    p = BaseModel()
    print(p)
    print(type(p.id))
    print(type(p.to_dict()))
    print(p.to_dict())
    p.save()
    print('\nObject is')
    print(p)
    print()
    print('\nCreate dictionary of object')
    my_dict = p.to_dict()
    print(my_dict)
    print('\ncreate object again')
    b = BaseModel(**my_dict)
    print(b)
    print()
