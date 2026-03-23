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

    max_unique = -1
    result = None

    for word in words:
        unique_count = len(set(word))
        if unique_count > max_unique:
            max_unique = unique_count
            result = word
        elif unique_count == max_unique and word < result:
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

    def test_mixed_empty_and_nonempty(self):
        assert find_max(["", "abc", ""]) == "abc"

    def test_all_empty_strings(self):
        assert find_max(["", "", ""]) == ""

    def test_long_strings(self):
        long_string1 = "abcdefghijklmnopqrstuvwxyz"
        long_string2 = "zyxwvutsrqponmlkjihgfedcba"
        assert find_max([long_string1, long_string2]) == long_string1

    def test_unicode_characters(self):
        assert find_max(["你好", "世界", "你好世界"]) == "你好世界"