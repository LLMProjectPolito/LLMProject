
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
    The function is case-sensitive.
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

def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_unique_count():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_words_with_all_same_characters():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_words_with_special_characters():
    assert find_max(["!@#", "abc", "123"]) == "!@#"

def test_words_with_numbers():
    assert find_max(["1234", "12", "1"]) == "1234"

def test_words_with_empty_string():
    assert find_max(["", "abc", "def"]) == "abc"

def test_lexicographical_order():
    assert find_max(["zebra", "apple", "banana"]) == "apple"

def test_lexicographical_tiebreaker():
    assert find_max(["abc", "abd", "aba"]) == "aba"

def test_long_strings():
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "abcdef"]) == "abcdefghijklmnopqrstuvwxyz"

def test_duplicate_words():
    assert find_max(["hello", "hello", "world"]) == "hello"

def test_mixed_case():
    assert find_max(["Hello", "hello", "World"]) == "Hello"

def test_identical_words():
    assert find_max(["abc", "abc"]) == "abc"

def test_large_number_of_words():
    words = ["a" * i for i in range(1, 101)]
    assert find_max(words) == "a" * 100

def test_all_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_unicode_characters():
    assert find_max(["你好", "世界", "abc"]) == "世界"