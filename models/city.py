#!/usr/bin/python3

"""
city.py

This module provides a `City` class whcich inherits the
'BaseModel' class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines a class that inherits the `BaseModel` class

    Attributes:
        state_id (string) - Will store the state ID
        name (string) - Name of the city
    """

    state_id = ""
    name = ""
