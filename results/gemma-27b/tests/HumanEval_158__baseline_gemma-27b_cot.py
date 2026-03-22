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

def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_unique_chars_lexicographical_order():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_all_words_same_unique_chars():
    assert find_max(["abc", "bac", "cab"]) == "abc"

def test_words_with_repeated_characters():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_words_with_empty_string():
    assert find_max(["", "abc", "def"]) == "abc"

def test_words_with_empty_string_and_same_unique_chars():
    assert find_max(["", "ab", "cd"]) == "ab"

def test_words_with_special_characters():
    assert find_max(["!@#", "abc", "def"]) == "!@"

def test_words_with_numbers():
    assert find_max(["123", "abc", "def"]) == "123"

def test_mixed_characters():
    assert find_max(["a1b2", "abc", "def"]) == "a1b2"

def test_long_words():
    assert find_max(["abcdefgh", "abc"]) == "abcdefgh"

def test_same_word_multiple_times():
    assert find_max(["hello", "hello", "hello"]) == "hello"

def test_case_sensitivity():
    assert find_max(["Hello", "hello"]) == "Hello"