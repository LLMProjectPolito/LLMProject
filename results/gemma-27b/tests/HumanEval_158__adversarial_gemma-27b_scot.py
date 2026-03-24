
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

def test_list_with_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_basic_case():
    assert find_max(["name", "of", "string"]) == "string"

def test_tie_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_all_same_characters():
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_multiple_words_same_max_unique_chars():
    assert find_max(["abc", "bca", "cab"]) == "abc"

def test_words_with_different_lengths():
    assert find_max(["a", "aa", "aaa", "aaaa"]) == "aaaa"

def test_words_with_special_characters():
    assert find_max(["!@#", "$%^", "&*("]) == "!@#"

def test_mixed_case():
    assert find_max(["Name", "name", "NaMe"]) == "Name"