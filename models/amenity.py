#!/usr/bin/python3

"""
amenity.py

This module provides a `Amenity` class whcich inherits the
'BaseModel' class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Defines a class that inherits the `BaseModel` class

    Attribute:
        name (string) - Name of the Amenity
    """

    name = ""
