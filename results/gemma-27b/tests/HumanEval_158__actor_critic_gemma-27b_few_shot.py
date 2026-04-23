
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
    if words is None:
        raise TypeError("Input cannot be None")
    if not words:
        return ""

    max_unique = -1
    max_word = ""

    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique:
            max_unique = unique_chars
            max_word = word
        elif unique_chars == max_unique:
            # If words have the same number of unique characters,
            # choose the one that comes first lexicographically.
            if word < max_word:
                max_word = word

    return max_word

### Tests (Pytest):

def test_find_max_basic():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_same_unique_chars():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_all_same_char():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_all_empty_strings():
    assert find_max(["", "", ""]) == ""

def test_find_max_same_length_different_unique():
    assert find_max(["abc", "abd", "abe"]) == "abc"

def test_find_max_reverse_lexicographical():
    assert find_max(["zebra", "yacht", "xerox"]) == "xerox"

def test_find_max_none_input():
    with pytest.raises(TypeError):
        find_max(None)

# New tests based on review:

def test_find_max_special_chars():
    assert find_max(["abc!", "ab2", "a!2"]) == "abc!"

def test_find_max_long_short_same_unique():
    assert find_max(["a", "bb", "ccc", "abcd"]) == "a"

def test_find_max_same_max_unique_lexicographical():
    assert find_max(["aaa", "aaa", "aaa"]) == "aaa"

def test_find_max_case_sensitivity():
    assert find_max(["Name", "name"]) == "Name"  # Or "name" if case-insensitive is desired