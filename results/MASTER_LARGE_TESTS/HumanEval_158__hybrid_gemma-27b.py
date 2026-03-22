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

    max_unique_chars = -1
    max_word = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_word = word
        elif unique_chars == max_unique_chars and word < max_word:
            max_word = word

    return max_word

# Pytest suite - Comprehensive
class TestFindMax:

    def test_empty_list(self):
        assert find_max([]) == ""

    def test_single_word(self):
        assert find_max(["hello"]) == "hello"

    def test_basic_example1(self):
        assert find_max(["name", "of", "string"]) == "string"

    def test_basic_example2(self):
        assert find_max(["name", "enam", "game"]) == "enam"

    def test_basic_example3(self):
        assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    def test_multiple_max_unique_chars_lexicographical(self):
        assert find_max(["abc", "bca", "cab"]) == "abc"

    def test_words_with_same_unique_chars(self):
        assert find_max(["abc", "def", "ghi"]) == "abc"

    def test_words_with_different_lengths(self):
        assert find_max(["a", "aa", "aaa", "aaaa"]) == "aaaa"

    def test_words_with_repeated_chars(self):
        assert find_max(["aabbcc", "abcdef", "aab"]) == "abcdef"

    def test_mixed_case_words(self):
        assert find_max(["Hello", "World", "python"]) == "python"

    def test_words_with_numbers(self):
        assert find_max(["word1", "word22", "word333"]) == "word1"

    def test_words_with_special_characters(self):
        assert find_max(["word!", "word@", "word#"]) == "word!"

    def test_long_words(self):
        assert find_max(["abcdefghijklmnopqrstuvwxyz", "abcdefghijklm"]) == "abcdefghijklmnopqrstuvwxyz"

    def test_words_with_unicode_characters(self):
        assert find_max(["你好世界", "hello"]) == "你好世界"

    def test_all_words_same_unique_count_lexicographical_order(self):
        assert find_max(["zebra", "apple", "banana"]) == "apple"

    def test_empty_strings_in_list(self):
        assert find_max(["", "abc", "def"]) == "abc"

    def test_list_with_only_empty_strings(self):
        assert find_max(["", "", ""]) == ""

    def test_words_with_leading_and_trailing_spaces(self):
        assert find_max(["  abc", "def  ", "ghi"]) == "abc"

    def test_words_with_internal_spaces(self):
        assert find_max(["hello world", "hello", "world"]) == "hello world"

    def test_large_list_of_words(self):
        words = ["word" + str(i) for i in range(100)]
        assert find_max(words) == "word0"

    def test_words_with_mixed_case(self):
        assert find_max(["Hello", "hello", "World"]) == "World"

    def test_words_with_unicode_and_ascii(self):
        assert find_max(["hello", "你好世界"]) == "你好世界"

    def test_words_with_same_length_and_unique_chars(self):
        assert find_max(["abc", "bca", "cab"]) == "abc"