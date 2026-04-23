
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
        assert string_to_md5("   ") == "d41d8cd98f00b204e9800998ecf8427e"

    def test_string_with_special_characters(self):
        """Tests with a string containing special characters."""
        assert string_to_md5("!@#$%^&*()") == "9469a999999999999999999999999999"

    def test_string_with_unicode_characters(self):
        """Tests with a string containing unicode characters."""
        assert string_to_md5("你好世界") == "b10a8db164e0754105b7a99be72e3fe5"

    def test_string_with_numbers(self):
        """Tests with a string containing numbers."""
        assert string_to_md5("12345") == "5a105e8b9d40e1329780d62ea2265d8a"

    def test_string_with_mixed_characters(self):
        """Tests with a string containing a mix of characters."""
        assert string_to_md5("Hello123World!") == "92990229999999999999999999999999"

    def test_long_string(self):
        """Tests with a long string to ensure no overflow issues."""
        long_string = "This is a very long string to test the md5 hash function. It should handle long strings without any issues."
        expected_hash = hashlib.md5(long_string.encode('utf-8')).hexdigest()
        assert string_to_md5(long_string) == expected_hash

    def test_case_sensitivity(self):
        """Tests to ensure the function is case-sensitive."""
        assert string_to_md5("Hello") != string_to_md5("hello")

    @pytest.mark.parametrize(
        "input_string, expected_md5",
        [
            ("abc", "0cc175b9c0f1b6a831c399e269772661"),
            ("def", "7d7930e5d3664c63f346a9c3f8e50867"),
            ("ghi", "e8b0b313333333333333333333333333"),
        ],
    )
    def test_parametrized_strings(self, input_string, expected_md5):
        """Tests using pytest.mark.parametrize for multiple inputs."""
        assert string_to_md5(input_string) == expected_md5


def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

class TestPalindrome:
    def test_palindrome_basic(self):
        assert is_palindrome('radar') == True
        assert is_palindrome('hello') == False

    def test_palindrome_empty(self):
        assert is_palindrome('') == True

    def test_palindrome_with_spaces(self):
        assert is_palindrome("race car") == True

    def test_palindrome_with_punctuation(self):
        assert is_palindrome("A man, a plan, a canal: Panama") == True

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

class TestGetMax:
    def test_max_positive(self):
        assert get_max([1, 2, 3]) == 3

    def test_max_empty(self):
        assert get_max([]) == None

    def test_max_negative(self):
        assert get_max([-1, -2, -3]) == -1

    def test_max_mixed(self):
        assert get_max([-1, 2, -3, 4]) == 4