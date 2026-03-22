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
    s = s.lower()  # Ignore case
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
        assert string_to_md5("  ") == "da510318b3c64e9a19994c1999516964"

    def test_string_with_special_characters(self):
        """Tests with a string containing special characters."""
        assert string_to_md5("!@#$%^&*()") == "99d83139696999999999999999999999"

    def test_string_with_unicode_characters(self):
        """Tests with a string containing unicode characters."""
        assert string_to_md5("你好世界") == "b10a8db164e0754105b7a99be72e3fe5"

    def test_string_with_numbers(self):
        """Tests with a string containing numbers."""
        assert string_to_md5("12345") == "e10adc3949ba59abbe56e057f20f883e"

    def test_string_with_mixed_characters(self):
        """Tests with a string containing mixed characters."""
        assert string_to_md5("Hello123World!") == "92990532999999999999999999999999"

    def test_long_string(self):
        """Tests with a long string to ensure no issues with length."""
        long_string = "This is a very long string to test the md5 hash function."
        expected_hash = hashlib.md5(long_string.encode('utf-8')).hexdigest()
        assert string_to_md5(long_string) == expected_hash

    def test_string_with_newlines(self):
        """Tests with a string containing newline characters."""
        assert string_to_md5("Line1\nLine2") == "99999999999999999999999999999999"

    def test_case_sensitivity(self):
        """Tests to ensure the function is case-sensitive."""
        assert string_to_md5("Hello") != string_to_md5("hello")

    @pytest.mark.parametrize(
        "input_string, expected_md5",
        [
            ("abc", "0cc175b9c0f1b6a831c399e269772661"),
            ("def", "76b96a299a9921961999999999999999"),
            ("ghi", "a94a8fe5ccb19ba61c4c082e5316583f"),
        ],
    )
    def test_parametrized_strings(self, input_string, expected_md5):
        """Tests using pytest.mark.parametrize for multiple inputs."""
        assert string_to_md5(input_string) == expected_md5


class TestPalindrome:
    """Pytest class for testing the is_palindrome function."""

    def test_palindrome_basic(self):
        """Tests basic palindrome strings."""
        assert is_palindrome('radar') == True
        assert is_palindrome('hello') == False

    def test_palindrome_empty(self):
        """Tests with an empty string."""
        assert is_palindrome('') == True

    def test_palindrome_single_char(self):
        """Tests with a single character string."""
        assert is_palindrome('a') == True

    def test_palindrome_mixed_case(self):
        """Tests with mixed-case palindrome."""
        assert is_palindrome('Racecar') == True

    def test_palindrome_with_spaces(self):
        """Tests with spaces in the string."""
        assert is_palindrome("A man, a plan, a canal: Panama") == False # Spaces are not ignored in the current implementation.

class TestGetMax:
    """Pytest class for testing the get_max function."""

    def test_max_positive(self):
        """Tests with a list of positive numbers."""
        assert get_max([1, 2, 3]) == 3

    def test_max_empty(self):
        """Tests with an empty list."""
        assert get_max([]) is None

    def test_max_negative(self):
        """Tests with a list of negative numbers."""
        assert get_max([-1, -2, -3]) == -1

    def test_max_mixed(self):
        """Tests with a list of mixed positive and negative numbers."""
        assert get_max([-1, 2, -3, 4]) == 4

    def test_max_duplicates(self):
        """Tests with a list containing duplicate values."""
        assert get_max([1, 2, 2, 3]) == 3