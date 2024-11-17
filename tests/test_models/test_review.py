#!/usr/bin/python3

"""
test_user.py

This module provides a test class to test the `Review` class
`review.py` module.
"""

import unittest
from models.review import Review
from datetime import datetime
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test the Review class"""

    def test_instance_creation(self):
        """Test if an instance of Review can be created"""

        review = Review()
        self.assertIsInstance(review, Review)

        # Review should inherit from BaseModel
        self.assertIsInstance(review, BaseModel)

    def test_default_values(self):
        """Test if the default values of Review are correct"""

        review = Review()

        # Default value for place_id should be an empty string
        self.assertEqual(review.place_id, "")

        # Default value for user_id should be an empty string
        self.assertEqual(review.user_id, "")

        # Default value for text should be an empty string
        self.assertEqual(review.text, "")

    def test_inherited_attributes(self):
        """Test if the Review class correctly inherits from BaseModel"""

        review = Review()

        # BaseModel has id and created_at, so those should be inherited
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_attribute_assignment(self):
        """Test if we can set attributes for Review instances"""

        review = Review()
        review.place_id = "12345"
        review.user_id = "67890"
        review.text = "Great place!"
        self.assertEqual(review.place_id, "12345")
        self.assertEqual(review.user_id, "67890")
        self.assertEqual(review.text, "Great place!")

    def test_save(self):
        """
        Test if the save method works for Review
        (inherited from BaseModel)
        """

        review = Review()
        prev_updated_at = review.updated_at
        review.save()

        # updated_at should be updated after save
        self.assertNotEqual(prev_updated_at, review.updated_at)


if __name__ == '__main__':
    unittest.main()
