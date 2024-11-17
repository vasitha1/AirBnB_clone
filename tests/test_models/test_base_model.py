#!/usr/bin/python3

"""
test_base_model.py

This module provides a test class to test the `BaseModel` class
`base_model`.
"""

import uuid
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_instance_creation(self):
        """Tests if a BaseModel instance is created correctly"""

        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertTrue(uuid.UUID(instance.id))
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_unique_id(self):
        """Tests if `id` attribute has unique value for each instance"""

        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_str(self):
        """Tests the output of the __str__ method"""

        instance = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(
                            instance.id, instance.__dict__)
        self.assertEqual(str(instance), expected_str)

    def test_save_method(self):
        """Tests if the updated_at attributed refreshes correctly"""

        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(instance.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Tests if to_dict returns the correct dictionary representation"""

        instance = BaseModel()
        instance_dict = instance.to_dict()

        self.assertIsInstance(instance_dict, dict)
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertEqual(instance_dict['created_at'], instance.created_at)
        self.assertEqual(instance_dict['updated_at'], instance.updated_at)

    def test_kwargs(self):
        """Tests instantiation with kwargs"""

        data = {
            'id': str(uuid.uuid4()),
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
        }

        instance = BaseModel(**data)
        self.assertEqual(instance.id, data['id'])
        self.assertEqual(
            instance.created_at, datetime.fromisoformat(data['created_at'])
        )
        self.assertEqual(
            instance.updated_at, datetime.fromisoformat(data['updated_at'])
        )

    def test_missing_kwargs(self):
        """Tests that missing kwargs get default values"""

        instance = BaseModel()
        self.assertIsNotNone(instance.id)
        self.assertIsNotNone(instance.created_at)
        self.assertIsNotNone(instance.updated_at)


if __name__ == '__main__':
    unittest.main()
