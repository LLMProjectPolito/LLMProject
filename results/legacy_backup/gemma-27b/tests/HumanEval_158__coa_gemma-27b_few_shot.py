import pytest
import math


# Focus: Boundary Values
def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_word():
    assert find_max(["hello"]) == "hello"

def test_find_max_all_same_unique_count():
    assert find_max(["abc", "def", "ghi"]) == "abc"

# Focus: Equivalence Partitioning
def test_find_max_equivalence_partitioning():
    assert find_max(["name", "of", "string"]) == "string"
    assert find_max(["name", "enam", "game"]) == "enam"
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
    assert find_max(["abc", "aba", "abb"]) == "abc"
    assert find_max(["", "a", "aa"]) == "a"
    assert find_max(["abc", "cba", "bac"]) == "abc"
    assert find_max(["apple", "banana", "orange"]) == "banana"

# Focus: Logic Branches
def test_find_max_basic():
    assert find_max(["name", "of", "string"]) == "string"

def test_find_max_lexicographical():
    assert find_max(["name", "enam", "game"]) == "enam"

def test_find_max_all_same_unique_count():
    assert find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"