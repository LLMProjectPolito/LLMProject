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

    max_unique_count = 0
    result = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_count:
            max_unique_count = unique_chars
            result = word
        elif unique_chars == max_unique_count and word < result:
            result = word

    return result

class TestFindMax:
    def test_basic_case(self):
        assert find_max(["name", "of", "string"]) == "string"

    def test_empty_list(self):
        assert find_max([]) == ""

    def test_single_string(self):
        assert find_max(["hello"]) == "hello"

    def test_lexicographical_tie(self):
        assert find_max(["name", "enam", "game"]) == "enam"

    def test_special_characters(self):
        assert find_max(["!@#", "abc", "xyz!"]) == "!@#"

    def test_strings_with_spaces(self):
        assert find_max(["hello world", "abc def", "ghi jkl"]) == "hello world"

    def test_empty_string_in_list(self):
        assert find_max(["", "abc", "def"]) == "abc"

    def test_large_list(self):
        words = ["a" * i for i in range(1, 11)] + ["abc", "defgh", "ijklm"]
        assert find_max(words) == "ijklm"

    def test_duplicate_strings(self):
        assert find_max(["abc", "abc", "def"]) == "abc"

    def test_case_sensitivity(self):
        assert find_max(["Name", "name"]) == "Name"
        assert find_max(["name", "Name"]) == "Name"

    def test_unicode_characters(self):
        assert find_max(["你好", "世界"]) == "世界"

    def test_mixed_case_unicode(self):
        assert find_max(["你好World", "世界name"]) == "你好World"

    def test_all_empty_strings(self):
        assert find_max(["", "", ""]) == ""

    def test_all_same_unique_chars(self):
        assert find_max(["abc", "bac", "cab"]) == "abc"