import unittest
from palindrome import is_palindrome, make_palindrome  # Assuming the functions are in a palindrome module

class TestMakePalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(make_palindrome(''), '')

    def test_single_character_string(self):
        self.assertEqual(make_palindrome('a'), 'a')

    def test_palindrome_string(self):
        self.assertEqual(make_palindrome('radar'), 'radar')
        self.assertEqual(make_palindrome('madam'), 'madam')
        self.assertEqual(make_palindrome('catac'), 'catac')

    def test_non_palindrome_string(self):
        self.assertEqual(make_palindrome('hello'), 'hellollah')
        self.assertEqual(make_palindrome('cat'), 'catac')
        self.assertEqual(make_palindrome('c!@t'), 'c!@tac!@t')
        self.assertEqual(make_palindrome('c1at'), 'c1atc1at')

    def test_two_character_string(self):
        self.assertEqual(make_palindrome('ab'), 'abba')

    def test_three_character_string(self):
        self.assertEqual(make_palindrome('abc'), 'abcba')

    def test_edge_cases(self):
        self.assertEqual(make_palindrome("cata."), "catapac")
        self.assertEqual(make_palindrome("abba"), "abba")

    def test_long_string(self):
        self.assertEqual(make_palindrome('a' * 10000), 'a' * 10000)
        self.assertEqual(make_palindrome('catacatta'), 'catacatta')

if __name__ == '__main__':
    unittest.main()