#!/usr/bin/python3

"""
test_city.py

This module provides a test class to test the `City` class
`city.py`.
"""

import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up a new City instance for testing"""

        self.city = City()

    def test_inheritance(self):
        """Test if City class inherits from BaseModel"""

        self.assertIsInstance(self.city, BaseModel)

    def test_attributes_exist(self):
        """Test that City has all required attributes"""

        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_default_attributes(self):
        """Test the default value of City attributes"""

        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_instance_creation(self):
        """Test if City instance is created with unique ID and timestamps"""

        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_to_dict(self):
        """Test to_dict method to include City attributes and base ones"""

        city_dict = self.city.to_dict()
        self.assertIn("state_id", city_dict)
        self.assertIn("name", city_dict)
        self.assertIn("__class__", city_dict)
        self.assertEqual(city_dict["__class__"], "City")

    def test_str(self):
        """Test __str__ method returns the correct format"""

        expected = f"[City] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(str(self.city), expected)

    def test_save(self):
        """Test if save method updates the updated_at attribute"""

        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(self.city.updated_at, old_updated_at)
        self.assertTrue(self.city.updated_at > old_updated_at)


if __name__ == '__main__':
    unittest.main()
