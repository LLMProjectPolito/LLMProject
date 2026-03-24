
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

def test_all_words_same_unique_count_lexicographical():
    assert find_max(["abc", "bac", "cab"]) == "abc"

def test_empty_string_in_list():
    assert find_max(["", "abc", "def"]) == "abc"

def test_list_with_duplicate_words():
    assert find_max(["abc", "abc", "def"]) == "abc"

def test_edge_case_long_string_with_few_unique():
    assert find_max(["aaaaaaaaaa", "abcdefgh"]) == "abcdefgh"

def test_edge_case_mix_of_long_and_short_strings():
    assert find_max(["a", "bb", "ccc", "dddd"]) == "ccc"

def test_edge_case_strings_with_same_length_and_unique_chars():
    assert find_max(["abcd", "efgh"]) == "abcd"

def test_edge_case_strings_with_special_characters():
    assert find_max(["!@#$", "abc"]) == "!@#$"

def test_edge_case_strings_with_numbers():
    assert find_max(["1234", "abc"]) == "1234"

def test_edge_case_strings_with_mixed_characters():
    assert find_max(["a1b2", "abc"]) == "a1b2"

def test_edge_case_unicode_characters():
    assert find_max(["你好世界", "abc"]) == "你好世界"

def test_edge_case_long_string_with_many_duplicates():
    assert find_max(["aaaaaaaaaabbbbbbbbbb", "abcdefg"]) == "abcdefg"

def test_edge_case_long_string_with_some_duplicates():
    assert find_max(["aabbccddeeff", "abcdefg"]) == "abcdefg"

def test_edge_case_all_same_character():
    assert find_max(["aaaa", "bbbb", "cccc"]) == "aaaa"

def test_edge_case_mix_of_all_same_and_unique():
    assert find_max(["aaaa", "abc"]) == "abc"

def test_all_empty_strings():
    assert find_max(["", "", ""]) == ""