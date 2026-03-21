import unittest
from string_sequence import string_sequence

class TestStringSequenceFunction(unittest.TestCase):

    def test_zero_input(self):
        self.assertEqual(string_sequence(0), '0')

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            string_sequence('a')
        with self.assertRaises(TypeError):
            string_sequence(3.5)

    def test_negative_integer_input(self):
        self.assertEqual(string_sequence(-1), '0')

    def test_positive_integer_input(self):
        self.assertEqual(string_sequence(5), '0 1 2 3 4 5')

    def test_large_input(self):
        n = 10**10000
        self.assertEqual(string_sequence(n), '0 ' + str(n))

    def test_boundary_conditions(self):
        self.assertEqual(string_sequence(1), '0 1')
        self.assertEqual(string_sequence(2), '0 1 2')

if __name__ == '__main__':
    unittest.main()