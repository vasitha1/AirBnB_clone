#!/usr/bin/python3

"""
test_amenity.py

This module provides a unit test `Amenity` class of
`amenity.py`
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up a new Amenity instance for testing"""

        self.amenity = Amenity()

    def test_inheritance(self):
        """Test if Amenity class inherits from BaseModel"""

        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes_exist(self):
        """Test that Amenity has the required attribute"""

        self.assertTrue(hasattr(self.amenity, "name"))

    def test_default_attributes(self):
        """Test the default value of Amenity's attributes"""

        self.assertEqual(self.amenity.name, "")

    def test_instance_creation(self):
        """Test if Amenity instance is created with unique ID and timestamps"""
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_to_dict(self):
        """Test to_dict method to include Amenity attributes and base ones"""

        amenity_dict = self.amenity.to_dict()
        self.assertIn("name", amenity_dict)
        self.assertIn("__class__", amenity_dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")

    def test_str(self):
        """Test __str__ method returns the correct format"""

        expected = f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(str(self.amenity), expected)

    def test_save(self):
        """Test if save method updates the updated_at attribute"""

        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(self.amenity.updated_at, old_updated_at)
        self.assertTrue(self.amenity.updated_at > old_updated_at)


if __name__ == '__main__':
    unittest.main()
