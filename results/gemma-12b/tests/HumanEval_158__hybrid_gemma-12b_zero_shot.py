
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

import pytest
from your_module import find_max  # Replace your_module

class TestFindMax:
    """
    Test suite for the find_max function.
    """

    def test_empty_list(self):
        """Test with an empty list."""
        assert find_max([]) == ""

    def test_single_word(self):
        """Test with a list containing a single word."""
        assert find_max(["hello"]) == "hello"

    def test_multiple_words_different_unique_chars(self):
        """Test with multiple words having different unique character counts."""
        assert find_max(["name", "of", "string"]) == "string"

    def test_multiple_words_same_unique_chars_lexicographical_order(self):
        """Test with multiple words having the same unique character count,
        verifying lexicographical order."""
        assert find_max(["name", "enam", "game"]) == "enam"

    def test_words_with_repeated_characters(self):
        """Test with words containing repeated characters."""
        assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    def test_words_with_special_characters(self):
        """Test with words containing special characters."""
        assert find_max(["!@#", "abc", "xyz"]) == "!@#"

    def test_words_with_mixed_case(self):
        """Test with words containing mixed-case characters."""
        assert find_max(["Hello", "world", "Python"]) == "Python"

    def test_words_with_numbers(self):
        """Test with words containing numbers."""
        assert find_max(["123", "abc", "456"]) == "123"

    def test_words_with_spaces(self):
        """Test with words containing spaces."""
        assert find_max(["hello world", "abc", "def"]) == "hello world"

    def test_words_with_unicode_characters(self):
        """Test with words containing Unicode characters."""
        assert find_max(["你好", "abc", "世界"]) == "你好"

    def test_words_with_empty_string(self):
        """Test with a list containing an empty string."""
        assert find_max(["", "abc", "def"]) == ""

    def test_all_words_empty(self):
        """Test when all words in the list are empty strings."""
        assert find_max(["", "", ""]) == ""

    def test_words_with_same_length_and_unique_chars(self):
        """Test when words have the same length and unique chars."""
        assert find_max(["abc", "def", "ghi"]) == "abc"

    def test_words_with_same_unique_chars_and_length(self):
        """Test when words have the same unique chars and length."""
        assert find_max(["abc", "bac", "cab"]) == "abc"

    def test_long_words(self):
        """Test with long words to ensure efficiency."""
        assert find_max(["abcdefghijklmnopqrstuvwxyz", "1234567890"]) == "abcdefghijklmnopqrstuvwxyz"

    def test_words_with_duplicates_and_same_unique_count(self):
        """Test with words containing duplicates and same unique character count."""
        assert find_max(["aabbcc", "ddeeff", "gghhii"]) == "aabbcc"