#!/usr/bin/python3

"""
review.py

This module provides a `Review` class whcich inherits the
'BaseModel' class
"""


class Review(BaseModel):
    """
    Defines a class that inherits the `BaseModel` class

    Attribute:
        place_id (string) - Will store the place ID
        user_id (string) - Will store the User ID
        text (string) - Review
    """

    place_id = ""
    user_id = ""
    text = ""
