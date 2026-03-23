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
        unique_chars = len(set(word))
        if unique_chars > max_unique_count:
            max_unique_count = unique_chars
            result = word
        elif unique_chars == max_unique_count and word < result:
            result = word

    return result

class TestFindMax:
    def test_empty_list(self):
        assert find_max([]) == ""

    def test_single_word(self):
        assert find_max(["hello"]) == "hello"

    def test_multiple_words_different_unique_chars(self):
        assert find_max(["name", "of", "string"]) == "string"

    def test_multiple_words_same_unique_chars_lexicographical_order(self):
        assert find_max(["name", "enam", "game"]) == "enam"

    def test_multiple_words_same_unique_chars_lexicographical_order_2(self):
        assert find_max(["abc", "bca", "cab"]) == "abc"

    def test_words_with_repeated_characters(self):
        assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    def test_words_with_mixed_characters(self):
        assert find_max(["abcde", "abcdef", "abc"]) == "abcdef"

    def test_words_with_special_characters(self):
        assert find_max(["!@#", "abc", "123"]) == "!@#"

    def test_words_with_numbers(self):
        assert find_max(["12345", "123", "12"]) == "12345"

    def test_words_with_spaces(self):
        assert find_max(["hello world", "hello", "world"]) == "hello world"

    def test_words_with_unicode_characters(self):
        assert find_max(["你好世界", "hello", "world"]) == "你好世界"

    def test_words_with_empty_string(self):
        assert find_max(["", "abc", "def"]) == "abc"

    def test_words_with_all_empty_strings(self):
        assert find_max(["", "", ""]) == ""

    def test_words_with_mixed_empty_and_non_empty(self):
        assert find_max(["", "abc", ""]) == "abc"