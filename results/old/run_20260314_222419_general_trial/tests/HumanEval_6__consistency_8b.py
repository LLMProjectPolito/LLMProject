from typing import List
import unittest

class TestParseNestedParens(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(parse_nested_parens(""), [])

    def test_single_group(self):
        self.assertEqual(parse_nested_parens("()"), [1])

    def test_multiple_groups(self):
        self.assertEqual(parse_nested_parens("(()()) ((())) () ((())()())"), [2, 3, 1, 3])

    def test_deeply_nested_parens(self):
        self.assertEqual(parse_nested_parens("(()(())))"), [3])

    def test_unbalanced_parens(self):
        with self.assertRaises(ValueError):
            parse_nested_parens("(")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            parse_nested_parens("hello world")

    def test_multiple_groups_with_zero_nesting(self):
        self.assertEqual(parse_nested_parens("( ) ( )"), [0, 0])

    def test_multiple_groups_with_nested_parens(self):
        self.assertEqual(parse_nested_parens("((())) ((()))"), [2, 2])

if __name__ == "__main__":
    unittest.main()