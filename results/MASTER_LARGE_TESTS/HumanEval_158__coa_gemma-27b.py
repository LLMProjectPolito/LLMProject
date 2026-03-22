import pytest
import math


# Focus: Boundary Values
def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_single_element():
    assert find_max(["hello"]) == "hello"

def test_find_max_all_same_length():
    assert find_max(["abc", "def", "ghi"]) == "abc"

# Focus: Equivalence Partitioning
def test_equivalence_partition_empty_list():
    assert find_max([]) == ""

def test_equivalence_partition_single_word():
    assert find_max(["word"]) == "word"

def test_equivalence_partition_multiple_words_same_unique_count():
    assert find_max(["abc", "bac", "cab"]) == "abc"

# Focus: Logic Branches
def test_find_max_multiple_max_unique_chars():
    assert find_max(["abc", "bca", "cab"]) == "abc"

def test_find_max_empty_list():
    assert find_max([]) == ""

def test_find_max_all_same_unique_chars():
    assert find_max(["aaa", "bbb", "ccc"]) == "aaa"