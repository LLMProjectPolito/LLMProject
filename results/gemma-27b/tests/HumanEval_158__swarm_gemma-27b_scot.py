
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
    pass  # Assume the function is defined elsewhere

def test_empty_list():
    assert find_max([]) == ""

def test_all_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_equal_unique_chars_lexicographical():
    assert find_max(["abc", "bac", "cab"]) == "abc"

def test_edge_case_long_string_with_few_unique():
    assert find_max(["aaaaaaaaaa", "abcdefg"]) == "abcdefg"

def test_edge_case_mix_long_and_short():
    assert find_max(["a", "bb", "ccc", "dddd"]) == "ccc"

def test_edge_case_duplicate_words():
    assert find_max(["abc", "abc", "def"]) == "abc"

def test_edge_case_special_characters():
    assert find_max(["!@#", "$%^", "&*("]) == "!@#"

def test_edge_case_numbers_and_letters():
    assert find_max(["123", "abc", "a1b2"]) == "a1b2"

def test_edge_case_unicode_characters():
    assert find_max(["你好", "世界"]) == "世界"

def test_edge_case_mixed_case():
    assert find_max(["aBc", "AbC", "abc"]) == "AbC"

def test_edge_case_long_string_with_all_unique():
    assert find_max(["abcdefghijklmnopqrstuvwxyz", "abc"]) == "abcdefghijklmnopqrstuvwxyz"

def test_edge_case_long_string_with_some_unique():
    assert find_max(["aaaaaaaaaaaaaaaaaaaaaaab", "abcdefg"]) == "abcdefg"

def test_edge_case_empty_string_and_others():
    assert find_max(["", "abc", "def"]) == "abc"

def test_edge_case_only_one_word():
    assert find_max(["abc"]) == "abc"

def test_edge_case_very_long_word():
    long_word = "a" * 1000 + "b"
    assert find_max([long_word, "abc"]) == long_word

def test_edge_case_long_string_with_many_duplicates():
    assert find_max(["aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd", "abc"]) == "aaaaaaaaaabbbbbbbbbbccccccccccdddddddddd"