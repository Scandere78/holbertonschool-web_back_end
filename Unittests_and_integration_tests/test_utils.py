#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map
"""

from utils import get_json
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test case for the access_nested_map function"""
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        # Crée un mock pour la réponse de requests.get
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Appelle la fonction get_json
        result = get_json(test_url)

        # Vérifie que requests.get a été appelé une fois avec test_url
        mock_get.assert_called_once_with(test_url)

        # Vérifie que la fonction retourne bien test_payload
        self.assertEqual(result, test_payload)
