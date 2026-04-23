
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
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    if not words:
        return ""

    max_unique_chars = -1
    max_unique_word = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            max_unique_word = word
        elif unique_chars == max_unique_chars and word < max_unique_word:
            max_unique_word = word

    return max_unique_word

def test_empty_list():
    assert find_max([]) == ""

def test_single_word_all_unique():
    assert find_max(["abc"]) == "abc"

def test_single_word_repeated():
    assert find_max(["aaaa"]) == ""

def test_multiple_words_different_unique_counts():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_unique_count_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_multiple_words_same_unique_count_different_lexicographical():
    assert find_max(["abc", "def"]) == "abc"

def test_multiple_words_all_same_unique_count():
    assert find_max(["abc", "def", "ghi"]) == "abc"

def test_words_with_leading_trailing_spaces():
    assert find_max(["  abc", "def"]) == "def"

def test_words_with_special_characters():
    assert find_max(["abc!", "def"]) == "def"

def test_words_with_numbers():
    assert find_max(["abc1", "def"]) == "def"

def test_empty_strings_in_list():
    assert find_max(["", "abc"]) == "abc"

def test_words_with_mixed_unique_and_repeated():
    assert find_max(["aab", "aaa"]) == "aab"

def test_large_list_varied_unique_chars():
    assert find_max(["a", "aa", "aaa", "aaaa", "abc", "abcd", "abcde"]) == "abcde"

def test_mixed_case():
    assert find_max(["a", "A"]) == "a"

def test_words_with_unicode():
    assert find_max(["你好", "世界"]) == "世界"

def test_words_with_numbers_and_letters():
    assert find_max(["1a", "b1"]) == "b1"