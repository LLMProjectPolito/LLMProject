import pytest
import math

def test_sorted_list_sum_positive():
    """Test with a list containing strings of varying lengths,
    ensuring the function correctly filters odd-length strings,
    sorts the remaining strings by length (ascending), and
    then alphabetically for strings of the same length.
    """
    from solution import sorted_list_sum
    input_list = ["aa", "a", "aaa", "ab", "cd", "b"]
    expected_output = ["aa", "ab", "cd"]
    assert sorted_list_sum(input_list) == expected_output

import pytest

def test_empty_list(lst):
    """Test with an empty list as input."""
    assert sorted_list_sum(lst) == []

def test_sorted_list_sum_empty_list():
    """Test with an empty list."""
    assert sorted_list_sum([]) == []