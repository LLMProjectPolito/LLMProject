import pytest
import math


# Focus: Boundary Values
def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_word():
    assert find_max(["word"]) == "word"

def test_find_max_same_unique_chars():
    assert find_max(["abc", "cba", "bac"]) == "abc"

# Focus: Type Scenarios
def test_find_max_basic():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_repeated_chars():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"

# Focus: Logic Branches
def test_find_max_different_lengths():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_same_unique_chars():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_repeated_chars():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"