import pytest
import math


# Focus: Boundary Values
def test_boundary_empty_list():
    """Test with an empty list."""
    assert sorted_list_sum([]) == []

def test_boundary_single_odd_length():
    """Test with a list containing only one string of odd length."""
    assert sorted_list_sum(["a"]) == []

def test_boundary_single_even_length():
    """Test with a list containing only one string of even length."""
    assert sorted_list_sum(["aa"]) == ["aa"]

# Focus: Type Scenarios
def test_type_scenario_list_of_strings():
    """Test that the function accepts a list of strings."""
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_type_scenario_empty_list():
    """Test that the function handles an empty list correctly."""
    assert sorted_list_sum([]) == []

def test_type_scenario_mixed_lengths():
    """Test that the function handles a list with strings of varying lengths."""
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

# Focus: Logic Branches
def test_sorted_list_sum_empty_list():
    """Test case for an empty input list."""
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd_lengths():
    """Test case where all strings have odd lengths."""
    assert sorted_list_sum(["a", "abc", "de"]) == []

def test_sorted_list_sum_mixed_lengths_and_duplicates():
    """Test case with mixed string lengths, duplicates, and sorting."""
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "cc", "b"]) == ["aa", "bb", "cc"]