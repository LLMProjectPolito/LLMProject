
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
            # If unique character counts are equal, choose the lexicographically smaller word
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

def test_find_max_with_empty_list():
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

# New tests based on review
def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"

def test_find_max_with_special_chars():
    assert find_max(["abc!", "def$", "ghi#"]) == "abc!"

def test_find_max_with_numbers():
    assert find_max(["abc1", "def2", "ghi3"]) == "abc1"

def test_find_max_case_sensitivity():
    assert find_max(["Name", "name"]) == "Name"  # Assuming case-sensitive

def test_find_max_long_strings():
    long_string1 = "a" * 1000
    long_string2 = "abcdefghijklmnopqrstuvwxyz"
    assert find_max([long_string1, long_string2]) == long_string2