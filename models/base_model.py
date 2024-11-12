#!/usr/bin/python3

"""
base_model.py

This module provides a class `BaseModel` that defines all the common
attributes and methods for other classes.

Attributes:
- id (str): A unique identifier assigned to the instance using the
  `uuid` module.
- created_at (datetime): A timestamp representing the creation time of
  the instance.
- updated_at (datetime): A timestamp representing the last modification
  time of the instance.

Methods:
- __init__(): Initializes the instance with a unique `id`, and sets both
  `created_at` and `updated_at` attributes to the current datetime.
- __str__(): Provides a string representation of the instance, including
  the class name, unique identifier, and instance attributes.
- save(): Updates the `updated_at` attribute to the current date and time
  whenever an instance is modified.
- to_dict(): Converts the `created_at` and `updated_at` attributes to ISO
  format and returns a dictionary containing all key/values of an instance.

Usage:
This class is intended to be inherited by other classes to provide common
attributes and behavior, such as unique identification and timestamp
management.

Design Notes:
- The `uuid4` class of `uuid` module is used to generate a universally unique
  identifier (UUID) for the `id`.
- The `save` method ensures that `updated_at` is updated automatically
  everytime an instance attribute is modified.
- The `to_dict` method makes a copy of the instance's __dict__ to avoid
  direct modification of `created_at` and `updated_at` attributes.
"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines common attributes/methods for other classes."""

    def __init__(self):
        """
        Instantiates public instance attributes.

        id (string) - A unique ID assigned by UUID
        created_at (datetime) - The current datetime when an instance
                                is created
        updated_at (datetime) - The current datetime when an isnatnce
                                is updated
        """

        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = str(datetime.now())

    def __str__(self):
        """Returns a string representation of an object"""

        return ("[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__))

    def save(self):
        """Updates the 'updated_at' attribute when an object is modified."""

        self.updated_at = str(datetime.now())

    def to_dict(self):
        """
        Converts 'created_at' and 'updated_at' attributes to ISO format and
        returns a dictionary containing all key/values of an instance.
        """

        # Make a copy of __dict__
        dict_rep = self.__dict__.copy()

        # Convert 'created_at' and 'updated_at' to ISO format
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()

        # Add the class name as __class__
        dict_rep['__class__'] = self.__class__.__name__
        return dict_rep
