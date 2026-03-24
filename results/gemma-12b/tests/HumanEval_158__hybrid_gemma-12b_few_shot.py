
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

@pytest.mark.parametrize(
    "words, expected",
    [
        (["name", "of", "string"], "string"),
        (["name", "enam", "game"], "enam"),
        (["aaaaaaa", "bb", "cc"], "aaaaaaa"),
        (["abc", "bca", "cab"], "abc"),
        (["abc", "abd", "abe"], "abc"),
        (["a", "aa", "aaa"], "a"),
        (["", "a", "aa"], ""),
        (["abc", "", "def"], "abc"),
        (["abc", "def", ""], "abc"),
        (["abc", "abc", "abc"], "abc"),
        (["xyz", "abc", "def"], "abc"),
        (["abc", "xyz", "def"], "abc"),
    ],
)
def test_find_max(words, expected):
    assert find_max(words) == expected

class TestFindMax:
    """
    A comprehensive test suite for the find_max function.
    """

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
        assert find_max(["abc!", "def@"]) == "abc!"

    def test_mixed_case(self):
        """Tests words with mixed case letters."""
        assert find_max(["AbC", "aBc"]) == "AbC"

    def test_duplicate_words(self):
        """Tests the function with duplicate words in the list."""
        assert find_max(["abc", "abc", "def"]) == "abc"

    def test_long_words(self):
        """Tests with longer words to ensure efficiency."""
        assert find_max(["abcdefghijklmnopqrstuvwxyz", "1234567890"]) == "abcdefghijklmnopqrstuvwxyz"

    def test_unicode_characters(self):
        """Tests with unicode characters."""
        assert find_max(["你好", "世界"]) == "你好"

    def test_empty_string_in_list(self):
        """Tests when an empty string is present in the list."""
        assert find_max(["", "abc"]) == "abc"

    def test_all_empty_strings(self):
        """Tests when the list contains only empty strings."""
        assert find_max(["", "", ""]) == ""

    def test_find_max_same_unique_count_lexicographical(self):
        assert find_max(["apple", "banana", "apricot"]) == "apple"

    def test_find_max_with_duplicates(self):
        assert find_max(["apple", "apple", "banana"]) == "apple"

    def test_find_max_with_special_characters_2(self):
        assert find_max(["!@#", "abc", "$%^"]) == "!@#"

    def test_find_max_unicode_characters_2(self):
        assert find_max(["你好", "世界", "你好世界"]) == "你好世界"


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

    def test_palindrome_case_insensitive(self):
        assert is_palindrome("Racecar") == True

    def test_palindrome_with_spaces(self):
        assert is_palindrome("A man, a plan, a canal: Panama") == False # Spaces are not ignored

class TestGetMax:
    def test_max_positive(self):
        assert get_max([1, 2, 3]) == 3

    def test_max_empty(self):
        assert get_max([]) == None

    def test_max_negative(self):
        assert get_max([-1, -2, -3]) == -1

    def test_max_mixed(self):
        assert get_max([-1, 2, -3, 4]) == 4