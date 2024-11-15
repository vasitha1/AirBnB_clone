#!/usr/bin/python3

"""
place.py

This module provides a `Place` class whcich inherits the
'BaseModel' class
"""


class Place(BaseModel):
    """
    Defines a class that inherits the `BaseModel` class

    Attribute:
        city_id (string) - Will store the city ID
        user_id (string) - Will store the user ID
        name (string) - Name of the place
        description (string) - Description about the place
        number_rooms (integer) - Number of rooms
        number_bathroom (integer) - Number of bathrooms
        max_guest (integer) - Maximum gust allowed
        price_by_night (integer) - Price for night
        latitude (float) - Latitude of the place
        longitude (float) - Longitude of the place
        amenity_ids (list) - Will store list of strings
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
