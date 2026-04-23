
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

def test_all_odd_length_strings():
    assert sorted_list_sum(["a", "bc", "def"]) == []

def test_all_even_length_strings():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_even_and_odd_length_strings():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "b", "ccc"]) == ["aa", "bb", "ccc"]

def test_duplicate_strings():
    assert sorted_list_sum(["aa", "aa", "a", "aaa"]) == ["aa", "aa"]

def test_strings_with_same_length():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_list_with_only_one_odd_length_string():
    assert sorted_list_sum(["a"]) == []

def test_list_with_only_one_even_length_string():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_case_sensitivity():
    assert sorted_list_sum(["AA", "a"]) == ["AA"]

def test_whitespace():
    assert sorted_list_sum(["  aa", "aa"]) == ["aa", "  aa"]

def test_non_string_input():
    with pytest.raises(TypeError):
        sorted_list_sum([1, "aa"])

def test_null_values():
    with pytest.raises(TypeError):
        sorted_list_sum(["aa", None])