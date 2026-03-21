import unittest
from typing import List, Optional

class TestLongestFunction(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_element_list(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_elements_list(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'c')  # Corrected the expected value

    def test_multiple_elements_list_same_length(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_duplicate_strings(self):
        self.assertEqual(longest(['a', 'a', 'c']), 'a')

    def test_empty_string(self):
        self.assertEqual(longest(['']), '')

    def test_string_with_single_character(self):
        self.assertEqual(longest(['a', '']), 'a')

    def test_string_followed_by_empty_string(self):
        self.assertEqual(longest(['a', '']), 'a')

    def test_two_empty_strings(self):
        self.assertEqual(longest(['', '']), '')

    def test_input_not_a_list(self):
        with self.assertRaises(TypeError):
            longest('hello')

    def test_input_not_a_list_of_strings(self):
        with self.assertRaises(TypeError):
            longest([1, 2, 3])

    def test_input_with_none(self):
        with self.assertRaises(TypeError):
            longest([None, 'hello'])

if __name__ == '__main__':
    unittest.main()