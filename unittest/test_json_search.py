import unittest
from recursive_json_search import *
from test_data import *


class json_search_test(unittest.TestCase):
    '''test module to test search function in recursive_json_search.py'''

    def test_search_found(self):
        '''key should be found, return list should not be empty'''
        self.assertTrue([] != json_search(key1, data))

    def test_search_not_found(self):
        '''key should not be found, should return an empty list'''
        self.assertTrue([] == json_search(key2, data))

    def test_is_a_list(self):
        '''Should return a list'''
        self.assertIsInstance(json_search(key1, data), list)

    def test_api_key_is_limited_to_admin(self):
        '''Only admin may read apiKey (SR1)'''
        self.assertEqual([], json_search("apiKey", data, role="viewer"))
        self.assertEqual([], json_search("apiKey", data, role="operator"))
        self.assertNotEqual([], json_search("apiKey", data, role="admin"))

    def test_management_ip_allows_operator_but_not_viewer(self):
        '''Operator may read managementIpAddress, viewer may not (SR2)'''
        self.assertEqual([], json_search("managementIpAddress", data, role="viewer"))
        self.assertNotEqual([], json_search("managementIpAddress", data, role="operator"))

    def test_unknown_role_gets_nothing(self):
        '''Unknown role must get empty result, not an error (SR3)'''
        self.assertEqual([], json_search("issueSummary", data, role="guest"))
        self.assertEqual([], json_search("apiKey", data, role="guest"))
