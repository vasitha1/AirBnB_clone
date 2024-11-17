#!/usr/bin/python3

"""
test_file_storage.py

This module provides a test class to test the `FileStorage` class
`file_storage`.
"""

import os
import json
import unittest
from models.user import User
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Unit tests for the `FileStorage` class"""

    def setUp(self):
        """Set up for each test"""

        self.storage = FileStorage()
        self.test_file = "test_file.json"
        FileStorage._FileStorage__file_path = self.test_file
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after each test"""

        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all(self):
        """Tests the all() method"""

        self.assertEqual(self.storage.all(), {})
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), self.storage.all())

    def test_new(self):
        """Tests the new() method"""

        obj = User()
        self.storage.new(obj)
        key = "User.{}".format(obj.id)
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_save(self):
        """Test the save() method"""

        obj = State()
        self.storage.new(obj)
        self.storage.save()
        with open(self.test_file, 'r') as file:
            content = json.load(file)

        key = "State.{}".format(obj.id)
        self.assertIn(key, content)

    def test_reload(self):
        """Tests the reload() method"""

        obj = City()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = "City.{}".format(obj.id)
        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], City)

    def test_reload_no_file(self):
        """Tests reload() when no file exists"""

        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})


if __name__ == "__main__":
    unittest.main()
