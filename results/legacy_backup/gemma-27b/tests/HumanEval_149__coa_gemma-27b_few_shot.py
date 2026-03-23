import pytest
import math


# Focus: Boundary Values
def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd():
    assert sorted_list_sum(["a", "bb", "ccc"]) == []

def test_sorted_list_sum_all_even():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ['aa', 'bb', 'cc']

# Focus: Equivalence Partitioning
def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd():
    assert sorted_list_sum(["a", "bb", "ccc"]) == []

def test_sorted_list_sum_all_even():
    assert sorted_list_sum(["aa", "bb", "cc"]) == sorted(["aa", "bb", "cc"])

def test_sorted_list_sum_mixed():
    assert sorted_list_sum(["a", "aa", "aaa", "bb", "cccc"]) == sorted(["aa", "bb"])

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "aa", "bb", "ccc"]) == sorted(["aa", "aa", "bb"])

# Focus: Logic Branches
def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd():
    assert sorted_list_sum(["a", "bb", "ccc"]) == []

def test_sorted_list_sum_mixed():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "a", "aaa", "aa"]) == ["aa", "aa"]

def test_sorted_list_sum_same_length():
    assert sorted_list_sum(["bc", "ab", "cd"]) == ["ab", "bc", "cd"]