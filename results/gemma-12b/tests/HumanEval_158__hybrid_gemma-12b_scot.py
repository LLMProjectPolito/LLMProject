
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

    max_unique_chars = -1
    result = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            result = word
        elif unique_chars == max_unique_chars and word < result:
            result = word

    return result


class TestFindMax:
    def test_empty_list(self):
        assert find_max([]) == ""

    def test_single_word(self):
        assert find_max(["hello"]) == "hello"

    def test_multiple_words_different_unique_chars(self):
        assert find_max(["name", "of", "string"]) == "string"

    def test_multiple_words_same_unique_chars_lexicographical(self):
        assert find_max(["name", "enam", "game"]) == "enam"

    def test_words_with_repeated_chars(self):
        assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    def test_empty_string_in_list(self):
        assert find_max(["", "abc"]) == "abc"

    def test_mixed_empty_and_nonempty_strings(self):
        assert find_max(["", "abc", "def"]) == "abc"

    def test_all_same_unique_chars(self):
        assert find_max(["abc", "bca", "cab"]) == "abc"

    def test_long_strings(self):
        assert find_max(["abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"]) == "abcdefghijklmnopqrstuvwxyz"

    def test_all_empty_strings(self):
        assert find_max(["", "", ""]) == ""

    def test_unicode_characters(self):
        assert find_max(["你好", "世界", "Python"]) == "Python"