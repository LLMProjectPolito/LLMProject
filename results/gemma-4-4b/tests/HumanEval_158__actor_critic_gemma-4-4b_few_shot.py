
def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """

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
import pytest

def test_find_max_basic():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

def test_find_max_empty():
    assert find_max([]) == ""

def test_find_max_same_unique_chars():
    assert find_max(["abc", "bca", "cab"]) == "abc"

def test_find_max_all_same():
    assert find_max(["abc", "abc", "abc"]) == "abc"

def test_find_max_single_word():
    assert find_max(["abc"]) == "abc"

def test_find_max_with_empty_string():
    assert find_max(["", "abc"]) == "abc"

def test_find_max_with_duplicate_unique_chars():
    assert find_max(["aabbcc", "abc"]) == "abc"

def test_find_max_long_words():
    assert find_max(["abcdefgh", "ijklmnop", "qrstuvwx"]) == "abcdefgh"