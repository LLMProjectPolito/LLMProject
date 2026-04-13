
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

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    """
    if not words:
        return ""

    max_unique_count = -1
    result = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_count:
            max_unique_count = unique_chars
            result = word
        elif unique_chars == max_unique_count and word < result:
            result = word

    return result

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)


class TestFindMax:
    """
    A comprehensive test suite for the find_max function.
    """

    def test_basic_case(self):
        """Tests a standard case with different words."""
        assert find_max(["name", "of", "string"]) == "string"

    def test_lexicographical_tie(self):
        """Tests when multiple words have the same number of unique characters."""
        assert find_max(["name", "enam", "game"]) == "enam"

    def test_all_same_characters(self):
        """Tests when all words have the same character repeated."""
        assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    def test_empty_list(self):
        """Tests the case when the input list is empty."""
        assert find_max([]) == ""

    def test_single_word(self):
        """Tests the case when the input list contains only one word."""
        assert find_max(["hello"]) == "hello"

    def test_words_with_spaces(self):
        """Tests words containing spaces."""
        assert find_max(["hello world", "good bye"]) == "hello world"

    def test_words_with_special_characters(self):
        """Tests words containing special characters."""
        assert find_max(["!@#", "abc"]) == "!@#"

    def test_mixed_case(self):
        """Tests words with mixed case letters."""
        assert find_max(["Hello", "hello"]) == "Hello"

    def test_numbers_in_words(self):
        """Tests words containing numbers."""
        assert find_max(["123", "abc"]) == "123"

    def test_long_words(self):
        """Tests with longer words to ensure efficiency."""
        assert find_max(["abcdefghijklmnopqrstuvwxyz", "1234567890"]) == "abcdefghijklmnopqrstuvwxyz"

    def test_duplicate_words(self):
        """Tests with duplicate words in the list."""
        assert find_max(["abc", "abc", "def"]) == "abc"

    def test_words_with_unicode_characters(self):
        """Tests with unicode characters."""
        assert find_max(["你好", "世界"]) == "你好"


def test_find_max_all_same_unique_count():
    assert find_max(["abc", "def", "ghi"]) == "abc"

def test_find_max_mixed_lengths_and_unique_chars():
    assert find_max(["a", "ab", "abc", "abcd"]) == "abcd"

def test_find_max_with_duplicates_in_list():
    assert find_max(["abc", "abc", "def"]) == "abc"

def test_find_max_with_empty_string():
    assert find_max(["", "abc", "def"]) == "abc"

def test_find_max_with_special_characters_2():
    assert find_max(["!@#", "abc", "def"]) == "!@#"

def test_find_max_with_numbers_as_strings_2():
    assert find_max(["123", "12", "1"]) == "123"

def test_find_max_with_unicode_characters_2():
    assert find_max(["你好", "世界", "你好世界"]) == "你好世界"

def test_find_max_with_mixed_unicode_and_ascii_2():
    assert find_max(["hello", "你好", "world"]) == "你好"


def test_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_palindrome_empty():
    assert is_palindrome('') == True

def test_palindrome_case_insensitive():
    assert is_palindrome('Racecar') == True

def test_palindrome_with_spaces():
    assert is_palindrome('A man a plan a canal Panama') == False # Spaces are not ignored

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_negative():
    assert get_max([-1, -2, -3]) == -1

def test_max_mixed():
    assert get_max([-1, 2, -3, 4]) == 4

def test_max_duplicates():
    assert get_max([1, 2, 2, 3]) == 3