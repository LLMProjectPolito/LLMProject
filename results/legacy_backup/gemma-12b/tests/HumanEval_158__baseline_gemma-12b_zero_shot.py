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
        assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

    def test_mixed_lengths(self):
        assert find_max(["a", "aa", "aaa", "aaaa"]) == "a"

    def test_all_same_unique_count(self):
        assert find_max(["abc", "bca", "cab"]) == "abc"

    def test_numbers_and_symbols(self):
        assert find_max(["123", "abc", "1234"]) == "1234"

    def test_special_characters(self):
        assert find_max(["!@#", "$%^", "&*()"]) == "!@#"

    def test_mixed_characters(self):
        assert find_max(["a1b2", "c3d4", "e5f6"]) == "a1b2"

    def test_duplicate_words(self):
        assert find_max(["abc", "abc", "def"]) == "abc"

    def test_long_words(self):
        assert find_max(["abcdefghijklmnopqrstuvwxyz", "1234567890"]) == "abcdefghijklmnopqrstuvwxyz"

    def test_words_with_spaces(self):
        assert find_max(["hello world", "goodbye"]) == "hello world"

    def test_words_with_unicode(self):
        assert find_max(["你好世界", "hello"]) == "你好世界"

    def test_words_with_empty_string(self):
        assert find_max(["", "abc"]) == "abc"

    def test_words_with_only_empty_string(self):
        assert find_max(["", ""]) == ""