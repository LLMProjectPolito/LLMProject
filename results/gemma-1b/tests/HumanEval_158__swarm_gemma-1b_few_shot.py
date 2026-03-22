import pytest
import math

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    unique_counts = {}
    for word in words:
        unique_chars = set(word)
        unique_counts[word] = len(unique_chars)

    max_word = ""
    max_count = 0
    for word, count in unique_counts.items():
        if count > max_count:
            max_count = count
            max_word = word
        elif count == max_count and word < max_word:
            max_word = word

    return max_word

def find_max(words):
    """Write a function that accepts a list of strings.
    The list contains different words. Return the word with maximum number
    of unique characters. If multiple strings have maximum number of unique
    characters, return the one which comes first in lexicographical order.

    find_max(["name", "of", "string"]) == "string"
    find_max(["name", "enam", "game"]) == "enam"
    find_max(["aaaaaaa", "bb" ,"cc"]) == ""aaaaaaa"
    """
    unique_counts = {}
    for word in words:
        unique_chars = set(word)
        unique_counts[word] = len(unique_chars)

    max_word = ""
    max_count = 0
    for word, count in unique_counts.items():
        if count > max_count:
            max_count = count
            max_word = word
        elif count == max_count and word < max_word:
            max_word = word

    return max_word

def test_find_max():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == ""
    assert find_max(["a", "b", "c"]) == "a"
    assert find_max(["a", "b", "a"]) == "a"
    assert find_max(["a", "b", "c", "d"]) == "a"
    assert find_max(["a", "b", "c", "d", "e"]) == "a"
    assert find_max(["a", "b", "c", "d", "e", "f"]) == "a"
    assert find_max(["a", "b", "c", "d", "e", "f", "g"]) == "a"
    assert find_max(["a", "b", "c", "d", "e", "f", "g", "h"]) == "a"
    assert find_max(["a", "b", "c", "d", "e", "f", "g", "h", "i"]) == "a"
    assert find_max(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]) == "a"
    print("All tests passed")