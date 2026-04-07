
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

import pytest
import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if not text:
        return None
    md5_hash = hashlib.md5(text.encode('utf-8'))
    return md5_hash.hexdigest()

class TestStringtoMD5:
    """
    Pytest class for testing the string_to_md5 function.
    """

    def test_valid_string(self):
        """Tests with a standard string."""
        assert string_to_md5("Hello world") == "3e25960a79dbc69b674cd4ec67a72c62"

    def test_empty_string(self):
        """Tests with an empty string."""
        assert string_to_md5("") is None

    def test_string_with_spaces(self):
        """Tests with a string containing spaces."""
        assert string_to_md5("  ") == "da510318b3c64e9a19994c1999534993"

    def test_string_with_special_characters(self):
        """Tests with a string containing special characters."""
        assert string_to_md5("!@#$%^&*()") == "99e43599999999999999999999999999"

    def test_string_with_unicode_characters(self):
        """Tests with a string containing unicode characters."""
        assert string_to_md5("你好世界") == "b10a8db164e0754105b7a99be72e3fe5"

    def test_string_with_numbers(self):
        """Tests with a string containing numbers."""
        assert string_to_md5("12345") == "e10adc3949ba59abbe56e057f20f883e"

    def test_string_with_mixed_characters(self):
        """Tests with a string containing a mix of characters."""
        assert string_to_md5("Hello123World!") == "92990229999999999999999999999999"

    def test_long_string(self):
        """Tests with a long string to ensure no issues with length."""
        long_string = "This is a very long string to test the md5 hash function."
        expected_hash = "a94a8fe5ccb19ba61c4c0873d391e987"
        assert string_to_md5(long_string) == expected_hash

    def test_string_with_newlines(self):
        """Tests with a string containing newline characters."""
        assert string_to_md5("Hello\nWorld") == "99499999999999999999999999999999"

    def test_string_to_md5_valid(self):
        """Tests with valid, non-empty strings."""
        assert string_to_md5("test") == "098f6bcd4621d373cade4e832627b4f6"
        assert string_to_md5("a") == "0cc175b9c0f1b6a831c3901b9a67afe7"
        assert string_to_md5("12345") == "5d41402abc4b2a76b9719d911017c592"
        assert string_to_md5("This is a longer string.") == "99e52999610919799965969399996596"

    def test_string_to_md5_unicode(self):
        """Tests with Unicode strings."""
        assert string_to_md5("你好世界") == "a94a8fe5ccb19ba61c4c0873d391e987"
        assert string_to_md5("éàçüö") == "92996996996996996996996996996996"

    def test_string_to_md5_special_characters(self):
        """Tests with strings containing special characters."""
        assert string_to_md5("!@#$%^&*()") == "99999999999999999999999999999999"
        assert string_to_md5("string with spaces") == "99999999999999999999999999999999"

    def test_string_to_md5_mixed_case(self):
        """Tests with strings containing mixed case letters."""
        assert string_to_md5("MiXeDcAsE") == "62a99999999999999999999999999999"

    def test_string_to_md5_numbers_and_letters(self):
        """Tests with strings containing numbers and letters."""
        assert string_to_md5("a1b2c3d4e5") == "99999999999999999999999999999999"

    def test_string_to_md5_long_string(self):
        """Tests with a very long string."""
        long_string = "This is a very long string to test the md5 hash function. It should handle long strings without issues." * 10
        assert len(string_to_md5(long_string)) == 32  # MD5 hash is always 32 characters long

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

class TestPalindrome:
    def test_palindrome_basic(self):
        assert is_palindrome('radar') == True
        assert is_palindrome('hello') == False

    def test_palindrome_empty(self):
        assert is_palindrome('') == True

class TestGetMax:
    def test_max_positive(self):
        assert get_max([1, 2, 3]) == 3

    def test_max_empty(self):
        assert get_max([]) == None