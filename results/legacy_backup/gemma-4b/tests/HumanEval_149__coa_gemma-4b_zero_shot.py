import pytest
import math


# Focus: Boundary Values
import pytest

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_odd_lengths():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_sorted_list_sum_mixed_lengths():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "a", "aa", "aaa"]) == ["aa", "aa"]

def test_sorted_list_sum_same_length():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

# Focus: Type Scenarios
import pytest

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_length():
    assert sorted_list_sum(["a", "b", "c"]) == []

def test_all_even_length():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

# Focus: Logic Branches
import pytest

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_odd_lengths():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_sorted_list_sum_mixed_lengths():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "a", "aa", "aaa"]) == ["aa", "aa"]

def test_sorted_list_sum_same_length():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]