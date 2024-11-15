#!/usr/bin/python3

"""
file_storage.py

This module provides a class 'FileStorage' that
serializes instances to JSON file and deserializes
JSON file to instances.

Attributes:
- __file_path (string): a private class attribute that stores
  the JSON file where serialized data will be saved.
- __objects (dictionary): a private class attribute which is empty
  initially. It will store all objects in memory in the following format:
        - key: '<class_name>.<id>'
        - Value: The corresponding object instance

Methods:
- all(): returns the value of `__objects` attribute. It provides
  a way to access all currently stored objects.
- new(): Sets its `obj` argument in `__objects` attribute with a
  specific key format.
- save(): Serializes `__objects` to the JSON file defined by the
  `__file_path` attribute.
- reload(): Deserializes the JSON file back to `__objects`.

Usage:
This class serializes instances to JSON file and deserializes JSON
file to instances. It is intended to store and load objects in a
persistence way using JSON files.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Serializes and deserializes JSON file.

    Private class attributes:
        __file_path (string) - Path to the JSON file for storage
        __objects (dictionary) - Will store all objects as <class_name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj.class_name>.id"""

        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (__file_path)"""

        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)

            # Convert the dictionary back into objects
            for key, value in obj_dict.items():
                class_name = value['__class__']

                # Fetch the class dynamically using `globals()`
                cls = globals().get(class_name)
                if cls:
                    self.__objects[key] = cls(**value)
