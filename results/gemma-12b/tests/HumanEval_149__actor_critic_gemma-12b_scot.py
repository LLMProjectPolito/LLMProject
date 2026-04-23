
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
from your_module import sorted_list_sum  # Replace your_module

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_only_odd_length_strings():
    assert sorted_list_sum(["a", "bbb", "ccccc"]) == []

def test_only_even_length_strings():
    assert sorted_list_sum(["aa", "bbbb", "cccccc"]) == ["aa", "bbbb", "cccccc"]

def test_mixed_even_odd_lengths():
    assert sorted_list_sum(["a", "aa", "aaa", "aaaa"]) == ["aa", "aaaa"]

def test_duplicates_preserved():
    assert sorted_list_sum(["aa", "aa", "bb", "cc", "cc"]) == ["aa", "aa", "bb", "cc", "cc"]

def test_complex_scenario():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "c", "cc", "ddd", "ee"]) == ["aa", "bb", "cc", "ee"]

def test_single_even_length():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_odd_length():
    assert sorted_list_sum(["a"]) == []

def test_numbers_excluded():
    assert sorted_list_sum([1, 2, 3, 4, 5]) == []  # Should remove all numbers

def test_mixed_data_types_excluded():
    assert sorted_list_sum(["a", 1, "bb", 2]) == ["a", "bb"] # Should remove numbers

def test_empty_strings_included():
    assert sorted_list_sum(["a", "", "bb"]) == ["a", "bb"]

def test_empty_strings_only():
    assert sorted_list_sum(["", "", ""]) == ["", "", ""]

def test_long_list():
    long_list = ["a"] * 100 + ["aa"] * 50 + ["aaa"] * 25
    expected_result = ["aa"] * 50
    assert sorted_list_sum(long_list) == expected_result