#!/usr/bin/python3
"""
    For serialization and deserialization of
    data using file
"""
from seniors.base_seniors import BaseSenior
import json


all_classes = {"BaseSenior": BaseSenior}

class FileStorage:
    """
        For file storage
    """
    __objects = dict()
    __file_path = "seniors.json"

    def all(self, obj_class=None):
        """
            Returns all instances            
        """
        new_dict = dict()
        if obj_class and obj_class in all_classes:
            all_instances = FileStorage.__objects
            for key, value in all_instances.items():
                if key.split('.')[0] == obj_class:
                    new_dict[key] = value
            return new_dict 
        else:
            return FileStorage.__objects
    
    def new(self, obj):
        """
            Adds the obj in __objects
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
            Serializes to the seniors.json
        """
        new_dict = dict()
        for key, val in FileStorage.__objects.items():
            new_dict[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w') as new_file:
            json.dump(new_dict, new_file)

    def reload(self):
        """
            Deserializes the file to each class instance
        """
        try:
            with open(self.__file_path, 'r') as file:
                all_dict = json.load(file)
                for key, value in all_dict.items():
                    class_name = value["__class__"]
                    if class_name in all_classes:
                        FileStorage.__objects[key] = \
                            all_classes[class_name](**value)
            return FileStorage.__objects
        except:
            pass

    def delete(self, obj_key):
        """
            Delete an instance base on its key
        """
        if FileStorage.__objects.get(obj_key):
            del FileStorage.__objects[obj_key]
            FileStorage.save(self)

        
