import pytest
import math


# Focus: Boundary Values
def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_odd_lengths():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_sorted_list_sum_mixed():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

# Focus: Type Scenarios
def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_odd_lengths():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_sorted_list_sum_mixed():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

# Focus: Logic Branches
def test_sorted_list_sum_basic():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["ab", "a", "aaa", "cd", "ab"]) == ["ab", "ab", "cd"]