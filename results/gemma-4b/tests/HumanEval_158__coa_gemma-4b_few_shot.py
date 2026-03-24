
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
import math


# Focus: Boundary Values
import pytest

def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_word():
    assert find_max(["word"]) == "word"

def test_find_max_multiple_words_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_multiple_words_same_unique_chars_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_multiple_words_same_unique_chars_and_length():
    assert find_max(["aaaaaaa", "bb", "cc"]) == ""aaaaaaa"

# Focus: Type Scenarios
import pytest

def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["word"]) == "word"

def test_multiple_words_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

def test_multiple_words_same_unique_chars_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_multiple_words_same_unique_chars_and_lexicographical():
    assert find_max(["aaaaaaa", "bb", "cc"]) == ""aaaaaaa"

# Focus: Logic Branches
import pytest

def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_word():
    assert find_max(["word"]) == "word"

def test_find_max_multiple_words_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_multiple_words_same_unique_chars_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_multiple_words_same_unique_chars_and_lexicographical():
    assert find_max(["aaaaaaa", "bb", "cc"]) == ""aaaaaaa"