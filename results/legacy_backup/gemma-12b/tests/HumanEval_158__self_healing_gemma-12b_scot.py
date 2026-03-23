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
        unique_count = len(set(word))
        if unique_count > max_unique_count:
            max_unique_count = unique_count
            result = word
        elif unique_count == max_unique_count and word < result:
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

    def test_multiple_words_same_unique_chars_lexicographical_tie(self):
        assert find_max(["abc", "bca", "cab"]) == "abc"

    def test_words_with_repeated_chars(self):
        assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    def test_words_with_special_chars(self):
        assert find_max(["!@#", "abc", "123"]) == "!@#"

    def test_mixed_case_words(self):
        assert find_max(["Hello", "hello", "World"]) == "World"

    def test_words_with_spaces(self):
        assert find_max(["hello world", "hello", "world"]) == "hello world"

    def test_words_with_numbers(self):
        assert find_max(["123", "abc", "12"]) == "123"

    def test_all_words_same_unique_chars(self):
        assert find_max(["abc", "def", "ghi"]) == "abc"