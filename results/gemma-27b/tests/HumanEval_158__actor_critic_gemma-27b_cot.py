
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
        elif unique_chars == max_unique_chars:
            if word < max_word:
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

def test_words_with_same_length():
    assert find_max(["abc", "bac", "cab"]) == "abc"

def test_words_with_different_lengths():
    assert find_max(["a", "aa", "aaa"]) == "aaa"

def test_words_with_symbols():
    assert find_max(["!@#", "abc", "123"]) == "!@#"

def test_words_with_mixed_case():
    assert find_max(["Hello", "hello", "World"]) == "World"

def test_words_with_digits():
    assert find_max(["1234", "123", "12"]) == "1234"

def test_words_with_empty_string():
    assert find_max(["", "abc", "def"]) == "abc"

def test_single_unique_char():
    assert find_max(["aaaa", "bbbb", "cccc"]) == "aaaa"

def test_lexicographical_order():
    assert find_max(["zebra", "apple", "banana"]) == "zebra"

def test_long_strings():
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "abcdef"]) == "abcdefghijklmnopqrstuvwxyz"

def test_unicode():
    assert find_max(["你好", "世界"]) == "世界"

def test_mixed_unicode_ascii():
    assert find_max(["你好world", "hello世界"]) == "你好world"

def test_complex_tiebreaker():
    assert find_max(["abc", "abd", "abe"]) == "abc"

def test_all_same_unique_count():
    assert find_max(["cab", "abc", "bac"]) == "abc"

def test_all_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_complex_unicode():
    assert find_max(["你好世界！", "hello🌍"]) == "你好世界！"