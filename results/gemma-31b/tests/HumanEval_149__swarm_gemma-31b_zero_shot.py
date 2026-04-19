
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

@pytest.mark.parametrize("input_list, expected", [
    (["", "zz", "aa", "b", "cccc", "cc"], ["", "aa", "cc", "zz", "cccc"]),
    (["", "a", "BB", "aa", "AA", "bb", "ccc", ""], ["", "", "AA", "BB", "aa", "bb"]),
])
def test_sorted_list_sum_edge_cases(input_list, expected):
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_mixed_even_lengths():
    # Tests filtering of odd lengths, sorting by length (ascending), 
    # and tie-breaking with alphabetical order.
    assert sorted_list_sum(["ox", "apple", "bear", "deer", "cat", "hi", "elephant", "bo"]) == ["bo", "hi", "ox", "bear", "deer", "elephant"]