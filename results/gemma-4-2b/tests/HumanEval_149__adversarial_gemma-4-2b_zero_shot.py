
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
    result = [s for s in lst if len(s) % 2 == 0]
    result.sort(key=lambda x: (len(x), x))
    return result

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_even_length():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_all_odd_length():
    assert sorted_list_sum(["a", "b", "c"]) == []

def test_mixed_even_odd():
    assert sorted_list_sum(["aa", "a", "aaa", "cd"]) == ["aa", "cd"]

def test_duplicate_strings():
    assert sorted_list_sum(["aa", "a", "aaa", "aa"]) == ["aa", "aa"]

def test_single_string():
    assert sorted_list_sum(["a"]) == []

def test_complex_list():
    assert sorted_list_sum(["ab", "a", "aaa", "cd", "ef", "gh"]) == ["ab", "cd", "ef", "gh"]

def test_even_length_strings():
    assert sorted_list_sum(["aa", "bb", "cc", "dd"]) == ["aa", "bb", "cc", "dd"]

def test_odd_length_strings():
    assert sorted_list_sum(["a", "b", "c", "d"]) == []

def test_mixed_even_odd_complex():
    assert sorted_list_sum(["ab", "a", "aaa", "cd", "ef", "gh", "ij"]) == ["ab", "cd", "ef", "gh", "ij"]