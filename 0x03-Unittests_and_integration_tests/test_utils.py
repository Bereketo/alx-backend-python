#!/usr/bin/env python3
"""Parametrized Test
"""
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, Mock
import requests


class TestAccessNestedMap(unittest.TestCase):
    """Unittest for access_nested_map function
    """
    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
            ])
    def test_access_nested_map(self, nested_map, path, expected):
        """tests if the fucntion works as expected"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test that a KeyError is raised
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, input_url, expected):
        mock_response = Mock()
        mock_response.json.return_value = expected
        with patch('utils.requests.get', return_value=mock_response)\
                as mock_get:
            result = get_json(input_url)
            self.assertEqual(result, expected)
            mock_get.assert_called_once_with(input_url)
