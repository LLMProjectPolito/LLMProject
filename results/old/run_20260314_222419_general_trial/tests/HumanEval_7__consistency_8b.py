import unittest
from unittest.mock import MagicMock
from io import StringIO
import sys

class TestFilterBySubstring(unittest.TestCase):

    def test_empty_input_list(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_empty_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], ''), ['abc', 'bacd', 'cde', 'array'])

    def test_substring_not_found(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'xyz'), [])

    def test_substring_found_in_every_string(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'cde', 'array'])

    def test_substring_found_in_some_strings(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'bc'), ['abc', 'bacd'])

    def test_substring_containing_special_characters(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a*'), ['abc', 'bacd', 'array'])

    def test_large_input_list(self):
        large_list = ['abc' for _ in range(1000)] + ['bacd' for _ in range(500)] + ['cde' for _ in range(200)] + ['array' for _ in range(300)]
        self.assertEqual(filter_by_substring(large_list, 'a'), large_list[:1000] + large_list[1000 + 500:])

    def test_empty_input(self):
        self.assertEqual(filter_by_substring([], 'a'), [])

    def test_no_substring_found(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'b'), [])

    def test_multiple_substrings_found(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])

    def test_multiple_strings_no_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'def'], 'a'), [])

    def test_single_string_with_substring(self):
        self.assertEqual(filter_by_substring(['abc'], 'a'), ['abc'])

    def test_single_string_no_substring(self):
        self.assertEqual(filter_by_substring(['cde'], 'a'), [])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            filter_by_substring('abc', 'a')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            filter_by_substring([1, 2, 3], 'a')

    def test_non_substring_input(self):
        with self.assertRaises(TypeError):
            filter_by_substring(['abc', 'bacd', 'cde', 'array'], 1)

    def test_substring_found_in_all_strings(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'), ['abc', 'bacd', 'array'])

    def test_substring_found_in_some_strings(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'cd'), ['bacd'])

    def test_substring_found_in_first_string(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'ab'), ['abc'])

    def test_substring_found_in_last_string(self):
        self.assertEqual(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'ry'), ['array'])

if __name__ == '__main__':
    unittest.main()