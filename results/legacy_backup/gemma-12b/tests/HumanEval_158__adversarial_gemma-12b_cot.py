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

    def test_basic_case(self):
        assert find_max(["name", "of", "string"]) == "string"

    def test_lexicographical_tie(self):
        assert find_max(["name", "enam", "game"]) == "enam"

    def test_repeated_characters(self):
        assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    def test_mixed_lengths(self):
        assert find_max(["a", "aa", "aaa", "aaaa"]) == "a"

    def test_all_same_unique_count(self):
        assert find_max(["abc", "bca", "cab"]) == "abc"

    def test_empty_string(self):
        assert find_max(["", "abc", "def"]) == "abc"

    def test_list_with_empty_string(self):
        assert find_max(["abc", "", "def"]) == "abc"

    def test_list_with_only_empty_string(self):
        assert find_max([""]) == ""

    def test_special_characters(self):
        assert find_max(["!@#", "$%^", "&*()"]) == "!@#"

    def test_numbers_in_string(self):
        assert find_max(["123", "12", "1"]) == "123"

    def test_unicode_characters(self):
        assert find_max(["你好", "世界", "你好世界"]) == "你好世界"

    def test_long_strings(self):
        long_string1 = "abcdefghijklmnopqrstuvwxyz"
        long_string2 = "zyxwvutsrqponmlkjihgfedcba"
        assert find_max([long_string1, long_string2]) == long_string1