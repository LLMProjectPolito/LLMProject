
def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """

import pytest
import math


# Focus: Boundary Values
def test_boundary_empty_list():
    assert sorted_list_sum([]) == []

def test_boundary_single_odd_length():
    assert sorted_list_sum(["a"]) == []

def test_boundary_single_even_length():
    assert sorted_list_sum(["aa"]) == ["aa"]

# Focus: Type Scenarios
def test_type_scenario_empty_list():
    assert sorted_list_sum([]) == []

def test_type_scenario_list_with_one_odd_length_string():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_type_scenario_list_with_multiple_odd_and_even_length_strings():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

# Focus: Logic Branches
def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_length_strings():
    assert sorted_list_sum(["a", "bc", "def"]) == []

def test_mixed_lengths_and_duplicates():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "cc", "dd", "ee", "ff", "ggg"]) == ["aa", "bb", "cc", "dd", "ee", "ff"]