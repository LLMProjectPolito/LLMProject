
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

    def test_multiple_words(self):
        assert find_max(["name", "of", "string"]) == "string"

    def test_same_unique_chars(self):
        assert find_max(["name", "enam", "game"]) == "enam"

    def test_all_same_chars(self):
        assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    def test_mixed_unique_chars(self):
        assert find_max(["abc", "def", "ghi"]) == "abc"

    def test_empty_string(self):
        assert find_max(["", "abc"]) == "abc"

    def test_duplicate_words(self):
        assert find_max(["abc", "abc", "def"]) == "abc"

    def test_longer_words(self):
        assert find_max(["abcdefg", "abc"]) == "abcdefg"

    def test_words_with_spaces(self):
        assert find_max(["hello world", "world hello"]) == "hello world"

    def test_words_with_special_characters(self):
        assert find_max(["!@#", "$%^", "abc"]) == "!@#"

    def test_words_with_numbers(self):
        assert find_max(["123", "abc", "456"]) == "123"

    def test_complex_case(self):
        assert find_max(["apple", "banana", "orange", "grape"]) == "orange"

    def test_lexicographical_tie(self):
        assert find_max(["abc", "bca"]) == "abc"