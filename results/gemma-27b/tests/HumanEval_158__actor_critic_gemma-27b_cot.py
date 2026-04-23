
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
    result = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_unique_chars = unique_chars
            result = word
        elif unique_chars == max_unique_chars and word < result:
            result = word

    return result

def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_unique_count():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_words_with_repeated_characters():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_words_with_different_lengths():
    assert find_max(["a", "aa", "aaa"]) == "aaa"

def test_special_characters():
    assert find_max(["!@#", "abc", "def"]) == "!@#"

def test_words_with_numbers():
    assert find_max(["123", "abc", "def"]) == "123"

def test_mixed_characters():
    assert find_max(["a1b2", "abc", "123"]) == "a1b2"

def test_mixed_empty_and_nonempty():
    assert find_max(["", "abc", ""]) == "abc"

def test_long_strings():
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "abcdef"]) == "abcdefghijklmnopqrstuvwxyz"

def test_very_long_strings():
    long_string = "a" * 1000
    short_string = "b" * 100
    assert find_max([long_string, short_string]) == long_string

def test_all_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_unicode_characters():
    assert find_max(["你好", "世界", "abc"]) == "世界"

def test_same_max_unique_lexicographical():
    assert find_max(["abc", "abc", "def"]) == "abc"

def test_mixed_case():
    assert find_max(["aBc", "abc"]) == "aBc"

def test_large_list():
    words = [f"word{i}" for i in range(20)]
    assert find_max(words) == "word0"