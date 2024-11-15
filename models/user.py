#!/usr/bin/python3

"""
user.py

A class that inherits the `BaseModel` class.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines a class that inherits the class `BaseModel.

    Attributes:
        email (string) - Email of the user
        password (string) - Password of the user
        first_name (string) - First name of the user
        last_name (string) - Last name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
