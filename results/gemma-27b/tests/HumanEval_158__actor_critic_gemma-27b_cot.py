
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

def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"

def test_find_max_multiple_words():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_all_same_character():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_words_with_empty_string():
    assert find_max(["", "abc", "def"]) == "abc"

def test_find_max_words_with_special_characters():
    assert find_max(["!@#", "abc", "def"]) == "!@#"

def test_find_max_words_with_numbers():
    assert find_max(["123", "abc", "def"]) == "123"

def test_find_max_alphanumeric_characters():
    assert find_max(["a1b2", "abc", "def"]) == "a1b2"

def test_find_max_lexicographical_order():
    assert find_max(["abc", "abd", "aba"]) == "abc"

def test_find_max_long_words():
    assert find_max(["abcdefgh", "abcdefg", "abcdef"]) == "abcdefgh"

def test_find_max_words_with_unicode():
    assert find_max(["你好", "世界", "abc"]) == "世界"

def test_find_max_unicode_same_unique_count():
    assert find_max(["你好", "世界", "您好"]) == "世界"

def test_find_max_all_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_find_max_mixed_ascii_unicode():
    assert find_max(["abc你好", "世界123", "def"]) == "abc你好"

def test_find_max_very_long_string():
    long_string = "a" * 1000
    assert find_max([long_string, "b" * 500]) == long_string