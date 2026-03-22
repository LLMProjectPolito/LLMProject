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

    def test_single_word(self):
        assert find_max(["hello"]) == "hello"

    def test_multiple_words_different_unique_chars(self):
        assert find_max(["name", "of", "string"]) == "string"

    def test_multiple_words_same_unique_chars(self):
        assert find_max(["name", "enam", "game"]) == "enam"

    def test_words_with_duplicates(self):
        assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    def test_empty_string_in_list(self):
        assert find_max(["name", "", "string"]) == "string"

    def test_mixed_empty_and_non_empty_strings(self):
        assert find_max(["", "abc", ""]) == "abc"

    def test_words_with_special_characters(self):
        assert find_max(["!@#", "abc", "$%^"]) == "!@#"

    def test_words_with_unicode_characters(self):
        assert find_max(["你好", "世界", "abc"]) == "你好"

    def test_case_sensitivity(self):
        assert find_max(["apple", "Apple"]) == "apple"

    def test_with_numbers(self):
        assert find_max(["a1b2", "abc"]) == "a1b2"

    def test_with_mixed_characters(self):
        assert find_max(["a!1b", "abc"]) == "a!1b"

    def test_with_very_long_string(self):
        long_string = "a" * 1000
        assert find_max([long_string, "abc"]) == long_string

    def test_identical_strings(self):
        assert find_max(["abc", "abc", "abc"]) == "abc"

    def test_all_empty_strings(self):
        assert find_max(["", "", ""]) == ""

    def test_empty_and_long_string(self):
        long_string = "a" * 1000
        assert find_max(["", long_string]) == long_string

    def test_lexicographical_tie(self):
        assert find_max(["abc", "abc"]) == "abc"