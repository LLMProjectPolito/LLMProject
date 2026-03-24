
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

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """

    if not arr:
        return None

    max_val = arr[0]
    for word in arr:
        if word > max_val:
            max_val = word
    return max_val

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_max_string():
    assert get_max(["name", "of", "string"]) == "string"

def test_max_mixed():
    assert get_max(["name", "enam", "game"]) == "enam"

def test_max_aaaaaaa():
    assert get_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_max_single_element():
    assert get_max([5]) == 5

def test_max_duplicate_elements():
    assert get_max(["a", "a", "b"]) == "a"

def test_max_same_elements():
    assert get_max(["a", "a", "a"]) == "a"