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

    def test_all_same_characters(self):
        assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    def test_mixed_lengths(self):
        assert find_max(["a", "bb", "ccc", "dddd"]) == "ccc"

    def test_duplicate_words(self):
        assert find_max(["abc", "abc", "def"]) == "abc"

    def test_words_with_spaces(self):
        assert find_max(["hello world", "good bye"]) == "hello world"

    def test_words_with_special_characters(self):
        assert find_max(["abc!", "def@", "ghi#"]) == "abc!"

    def test_words_with_numbers(self):
        assert find_max(["abc1", "def2", "ghi3"]) == "abc1"

    def test_single_word(self):
        assert find_max(["single"]) == "single"

    def test_multiple_words_same_unique_count(self):
        assert find_max(["abc", "def", "ghi"]) == "abc"

    def test_words_with_unicode_characters(self):
        assert find_max(["你好", "世界", "Python"]) == "Python"

    def test_words_with_mixed_unicode_and_ascii(self):
        assert find_max(["hello", "你好", "world"]) == "hello"