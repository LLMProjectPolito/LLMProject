import pytest
import math


# Focus: Boundary Values
def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_word():
    assert find_max(["abc"]) == "abc"

def test_find_max_boundary_same_unique_chars():
    assert find_max(["abc", "cba"]) == "abc"

# Focus: Type Scenarios
def test_type_scenario_empty_list():
    assert find_max([]) == ""

def test_type_scenario_single_word():
    assert find_max(["hello"]) == "hello"

def test_type_scenario_multiple_words_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

# Focus: Logic Branches
def test_find_max_different_unique_chars():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_same_unique_chars_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_repeated_chars():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"