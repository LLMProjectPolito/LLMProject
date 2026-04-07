
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

def test_empty_list():
    assert find_max([]) == ""

def test_all_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_equal_unique_chars_lexicographical():
    assert find_max(["abc", "bac", "cab"]) == "abc"

def test_edge_case_long_string_with_few_unique():
    assert find_max(["aaaaaaaaaa", "abcdefg"]) == "abcdefg"

def test_edge_case_mix_long_and_short_with_same_unique():
    assert find_max(["abcde", "bcdefa"]) == "abcde"

def test_edge_case_duplicate_words():
    assert find_max(["abc", "abc", "def"]) == "abc"

def test_edge_case_special_characters():
    assert find_max(["!@#$", "abc"]) == "!@#$"

def test_edge_case_numbers_and_letters():
    assert find_max(["12345", "abcde"]) == "12345"

def test_edge_case_unicode_characters():
    assert find_max(["你好世界", "abc"]) == "你好世界"

def test_edge_case_mixed_case():
    assert find_max(["aBcDe", "abcde"]) == "aBcDe"

def test_edge_case_long_string_with_many_duplicates():
    assert find_max(["aaaaaaaaaabbbbbbbbbbcccccccccc", "abcdefgh"]) == "abcdefgh"

def test_edge_case_long_string_with_all_same_char():
    assert find_max(["aaaaaaaaaa", "bbbbbbbbbb", "ccccccccc"]) == "aaaaaaaaaa"

def test_edge_case_empty_string_and_others():
    assert find_max(["", "abc", "def"]) == "abc"

def test_edge_case_only_one_word():
    assert find_max(["abcdefg"]) == "abcdefg"