#!/usr/bin/python3

"""
base_model.py

This module provides a class 'BaseModel' that defines all the common
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
- save(): Updates the `updated_at` attribute whenever an instance is
  modified.
- __str__(): Provides a string representation of the instance, including
  the class name, unique identifier, and instance attributes.

Usage:
This class is intended to be inherited by other classes to provide common
attributes and behavior, such as unique identification and timestamp
management.

Design Notes:
- The `created_at` and `updated_at` attributes are stored as ISO-formatted
  strings.
- The `__setattr__` method ensures that `updated_at` is updated automatically
  every time an instance’s attribute is modified.
- The `uuid` module is used to generate a universally unique identifier
  (UUID) for the `id`.
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
        self.created_at = str(datetime.now().isoformat())
        self.updated_at = str(datetime.now().isoformat())

    def save(self):
        """Updates the 'updated_at' attribute when an object is modified."""

        self.updated_at = str(datetime.now().isoformat())

    def __str__(self):
        """Returns a string representation of an object"""

        return ("[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__))
