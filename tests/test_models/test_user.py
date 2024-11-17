#!/usr/bin/python3

"""
test_user.py

This module provides a test class to test the `User` class
`user`.
"""


import unittest
from models.user import User
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Tests cases for the User class"""

    def setUp(self):
        """Set up a new User instance for testing"""

        self.user = User()

    def test_inheritance(self):
        """Tests if User class inherits from BaseModel"""

        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Tests that User has all required attributes"""

        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_default_attributes(self):
        """Tests the default value of User attributes"""

        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_instance_creation(self):
        """Tests if User instance is created with unique ID and timestamps"""

        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_to_dict(self):
        """Tests to_dict method to include User attributes and base ones"""

        user_dict = self.user.to_dict()
        self.assertIn("email", user_dict)
        self.assertIn("password", user_dict)
        self.assertIn("first_name", user_dict)
        self.assertIn("last_name", user_dict)
        self.assertIn("__class__", user_dict)
        self.assertEqual(user_dict["__class__"], "User")

    def test_str(self):
        """Tests __str__ method returns the correct format"""

        expected = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(str(self.user), expected)

    def test_save(self):
        """Tests if save method updates the updated_at attribute"""

        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(self.user.updated_at, old_updated_at)
        self.assertTrue(self.user.updated_at > old_updated_at)


if __name__ == '__main__':
    unittest.main()
