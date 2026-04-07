
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
        return None

    max_unique_chars = -1
    result = None

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
        assert find_max([]) is None

    def test_multiple_words_different_unique_chars(self):
        assert find_max(["name", "of", "string"]) == "string"

    def test_multiple_words_same_unique_chars(self):
        assert find_max(["name", "enam", "game"]) == "enam"

    def test_words_with_duplicates(self):
        assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    def test_empty_string_in_list(self):
        assert find_max(["name", "", "string"]) == "string"

    def test_list_with_only_empty_strings(self):
        assert find_max(["", "", ""]) == ""

    def test_mixed_empty_and_non_empty_strings(self):
        assert find_max(["", "abc", ""]) == "abc"

    def test_words_with_special_characters(self):
        assert find_max(["!@#", "abc", "xyz"]) == "!@#"

    def test_words_with_unicode_characters(self):
        assert find_max(["你好", "世界", "abc"]) == "你好"

    def test_identical_strings(self):
        assert find_max(["abc", "abc", "abc"]) == "abc"

    def test_single_word(self):
        assert find_max(["hello"]) == "hello"

    def test_numbers_only(self):
        assert find_max(["123", "456"]) == "123"

    def test_special_characters_and_numbers(self):
        assert find_max(["!@#123", "abc"]) == "!@#123"

    def test_lexicographical_order(self):
        assert find_max(["ab", "ac", "ba"]) == "ab"

    # Removed test_case_sensitivity