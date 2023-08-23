#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
    def test_delete(self):
        """Testing delete method"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        i.delete()  # Delete the instance
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertNotIn(key, j)  # Key should not be present in JSON

    def test_equality_after_dict(self):
        """Test equality after converting to/from dictionary"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            loaded_instance_dict = j[key]
            loaded_instance = self.value(**loaded_instance_dict)
            self.assertEqual(i.to_dict(), loaded_instance.to_dict())

    def test_json_format(self):
        """Test JSON format in file"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertIsInstance(j[key], dict)
            self.assertIn('id', j[key])
            self.assertIn('created_at', j[key])
            self.assertIn('updated_at', j[key])
            # ... check other attributes ...

    def test_str_format(self):
        """Test string representation format"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id, i.__dict__))

    def test_id_uniqueness(self):
        """Test uniqueness of generated IDs"""
        instances = [self.value() for _ in range(10)]
        id_set = set(instance.id for instance in instances)
        self.assertEqual(len(instances), len(id_set))

    def test_updated_at_after_save(self):
        """Test updated_at after calling save"""
        i = self.value()
        created_time = i.created_at
        i.save()
        updated_time = i.updated_at
        self.assertNotEqual(created_time, updated_time)
