#!/usr/bin/env python3
'''
Test class for utils.access_nested_map
'''
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''Unit testing utils.access_nested_map'''
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
     ({'a': 'str'}, ('b',)),
     ({'a': {'b': 'str'}}, ('a', 'c'))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''test exception raised by wrong input fed into function'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

if __name__ == '__main__':
    unittest.main()
