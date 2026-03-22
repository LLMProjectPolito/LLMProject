import pytest
import math


# Focus: Boundary Values
def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["abc"]) == "abc"

def test_same_unique_chars():
    assert find_max(["abc", "cba"]) == "abc"

# Focus: Type Scenarios
def test_empty_list():
    assert find_max([]) == ""

def test_single_word():
    assert find_max(["hello"]) == "hello"

def test_multiple_words_different_unique_chars():
    assert find_max(["abc", "ab", "a"]) == "abc"

# Focus: Logic Branches
def test_find_max_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_same_unique_chars_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_all_same_chars():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"