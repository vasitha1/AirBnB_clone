#!/usr/bin/python3

"""
test_state.py

This module provides a test class to test the `State` class
`state.py`.
"""


import unittest
from models.state import State
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Tests cases for the User class"""

    def setUp(self):
        """Set up a new User instance for testing"""

        self.state = State()

    def test_inheritance(self):
        """Tests if State class inherits from BaseModel"""

        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """Tests that State has all required attributes"""

        self.assertTrue(hasattr(self.state, "name"))

    def test_default_attributes(self):
        """Tests the default value of State attributes"""

        self.assertEqual(self.user.name, "")

    def test_instance_creation(self):
        """Tests if State instance is created with unique ID and timestamps"""

        self.assertIsInstance(self.state.id, atr)
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_to_dict(self):
        """Tests to_dict method to include State attributes and base ones"""

        State_dict = self.state.to_dict()
        self.assertIn("name", state_dict)
        self.assertIn("__class__", state_dict)
        self.assertEqual(state_dict["__class__"], "State")

    def test_str(self):
        """Tests if __str__ method returns the correct format"""

        expected = f"[State] ({self.state.id}) {self.state.__dict__}"
        self.assertEqual(str(self.state), expected)

    def test_save(self):
        """Tests if save method updates the updated_at attribute"""

        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(self.state.updated_at, old_updated_at)
        self.assertTrue(self.state.updated_at > old_updated_at)


if __name__ == '__main__':
    unittest.main()
