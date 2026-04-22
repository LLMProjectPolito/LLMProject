
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
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
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


@pytest.suite()
class TestFindMax:

    def test_empty_list(self):
        assert find_max([]) == ""

    def test_single_word(self):
        assert find_max(["hello"]) == "hello"

    def test_basic_case(self):
        assert find_max(["name", "of", "string"]) == "string"

    def test_tie_lexicographical(self):
        assert find_max(["name", "enam", "game"]) == "enam"

    def test_all_same_unique_chars(self):
        assert find_max(["abc", "bca", "cab"]) == "abc"

    def test_repeated_characters(self):
        assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    def test_mixed_cases(self):
        assert find_max(["abc", "def", "ghi", "abc"]) == "def"

    def test_empty_string(self):
        assert find_max(["", "abc", "def"]) == "abc"

    def test_multiple_ties(self):
        assert find_max(["abc", "bca", "cab", "def"]) == "abc"

    def test_long_words(self):
        assert find_max(["abcdefg", "abcde", "abcdf"]) == "abcdefg"

    def test_numbers_as_strings(self):
        assert find_max(["123", "45", "6789"]) == "6789"

    def test_special_characters(self):
        assert find_max(["!@#", "$%^", "&*()"]) == "!@#"

    def test_mixed_characters(self):
        assert find_max(["a1b2c", "a12b", "a1b"]) == "a1b2c"