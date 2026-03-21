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

def test_basic_cases():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_empty_list():
    assert find_max([]) == ""

def test_single_word_list():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_same_max_unique():
    assert find_max(["abc", "bac", "cab"]) == "abc"
    assert find_max(["xyz", "zyx"]) == "xyz"

def test_words_with_all_same_characters():
    assert find_max(["aaaa", "bbb", "c"]) == "aaaa"
    assert find_max(["aaaaaaaa", "bbbbbbbb", "cccc"]) == "aaaaaaaa"

def test_words_with_special_characters():
    assert find_max(["!@#", "abc", "123"]) == "!@#"
    assert find_max(["abc!", "def@", "ghi#"]) == "abc!"

def test_mixed_case():
    assert find_max(["Hello", "world", "Python"]) == "Python"
    assert find_max(["aBc", "AbC"]) == "AbC"

def test_long_words():
    long_word1 = "abcdefghijklmnopqrstuvwxyz"
    long_word2 = "zyxwvutsrqponmlkjihgfedcba"
    assert find_max([long_word1, long_word2]) == "abcdefghijklmnopqrstuvwxyz"

def test_empty_strings():
    assert find_max(["", "abc", ""]) == "abc"
    assert find_max(["", "", ""]) == ""

def test_mixed_empty_and_normal():
    assert find_max(["abc", "", "def"]) == "abc"

def test_duplicate_words():
    assert find_max(["abc", "abc", "def"]) == "abc"

def test_numbers_as_strings():
    assert find_max(["123", "12", "1"]) == "123"

def test_complex_case():
    assert find_max(["abcdef", "abcde", "abcdf"]) == "abcdef"