#!/usr/bin/python3

"""
__init__.py

This module creates a unique instance of `FileStorage`
class and loads objects from JSON file.
"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
