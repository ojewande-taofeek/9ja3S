#!/usr/bin/python3

"""
    The base model for all subjects and classes
"""
from uuid import uuid4
from datetime import datetime


class BaseSenior:
    """
        Defines all attrs and methods for all subjects and classes
    """

    def __init__(self, *args, **kwargs):
        """
            Instantiation of an object
        """
        from seniors import storage
        if kwargs:
            for key, val in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    val = datetime.strptime(val,"%Y-%m-%dT%H:%M:%S.%f")
                if key == "__class__":
                    continue
                setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
            Informal representation of an object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, 
                self.__dict__)
    
    def save(self):
        """
            Update an instance
        """
        from seniors import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            Converts the created_at, updated_at and id to str
        """
        new_dict = dict()
        new_dict.update(self.__dict__)
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
