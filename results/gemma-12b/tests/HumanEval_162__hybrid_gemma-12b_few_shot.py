
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

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


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
        assert string_to_md5("  ") == "da569e294d2999999999999999999999"

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
        assert string_to_md5("Hello123World!") == "9299053a399999999999999999999999"

    def test_long_string(self):
        """Tests with a long string to ensure no issues with length."""
        long_string = "This is a very long string to test the md5 hash function."
        assert string_to_md5(long_string) == "99999999999999999999999999999999"

    def test_case_sensitivity(self):
        """Tests to ensure case sensitivity is handled correctly."""
        assert string_to_md5("Hello") != string_to_md5("hello")

    @pytest.mark.parametrize(
        "input_string, expected_md5",
        [
            ("abc", "90015024c0bca1b6e93d3a3b574d34e0"),
            ("def", "7c2164a0b39c62976a39399999999999"),
            ("ghi", "90015024c0bca1b6e93d3a3b574d34e0"),
        ],
    )
    def test_parametrized_strings(self, input_string, expected_md5):
        """Tests using pytest.mark.parametrize for multiple inputs."""
        assert string_to_md5(input_string) == expected_md5


def test_palindrome_basic():
    """Tests basic palindrome cases."""
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    """Tests with an empty string."""
    assert is_palindrome('') == True

def test_palindrome_case_insensitive():
    """Tests case-insensitive palindrome."""
    assert is_palindrome("Racecar") == True

def test_get_max_positive():
    """Tests with a list of positive numbers."""
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    """Tests with an empty list."""
    assert get_max([]) is None

def test_get_max_negative():
    """Tests with a list of negative numbers."""
    assert get_max([-1, -2, -3]) == -1

def test_get_max_mixed():
    """Tests with a list of mixed positive and negative numbers."""
    assert get_max([-1, 2, -3, 4]) == 4