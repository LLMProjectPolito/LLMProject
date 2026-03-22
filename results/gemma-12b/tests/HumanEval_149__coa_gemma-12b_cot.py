import pytest
import math


# Focus: Boundary Values
def test_sorted_list_sum_empty_list():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd_length():
    assert sorted_list_sum(["a", "bc", "def"]) == []

def test_sorted_list_sum_mixed_lengths_same_length():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_sorted_list_sum_same_length_different_alphabetical():
    assert sorted_list_sum(["cc", "aa", "bb"]) == ["aa", "bb", "cc"]

def test_sorted_list_sum_boundary_one_element_even():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_sorted_list_sum_boundary_one_element_odd():
    assert sorted_list_sum(["a"]) == []

# Focus: Type Scenarios
def test_sorted_list_sum_empty_list():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd_lengths():
    assert sorted_list_sum(["a", "bc", "def"]) == []

def test_sorted_list_sum_mixed_lengths_and_duplicates():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "cc", "dd", "ee", "ff", "ggg"]) == ["aa", "bb", "cc", "dd", "ee", "ff"]

# Focus: Logic Branches
def test_sorted_list_sum_empty_list():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd_lengths():
    assert sorted_list_sum(["a", "bc", "def"]) == []

def test_sorted_list_sum_mixed_lengths_and_duplicates():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "cc", "dd", "ee", "ff", "ggg"]) == ["aa", "bb", "cc", "dd", "ee", "ff"]

def test_sorted_list_sum_same_length_alphabetical_sort():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_sorted_list_sum_same_length_different_alphabetical_sort():
    assert sorted_list_sum(["ba", "cd", "ef"]) == ["ba", "cd", "ef"]