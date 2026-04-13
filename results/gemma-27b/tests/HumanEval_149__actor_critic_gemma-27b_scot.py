
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
    """
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings

def test_empty_list_returns_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths_returns_empty_list():
    assert sorted_list_sum(["a", "abc", "xyz"]) == []

def test_mixed_lengths():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_duplicate_strings():
    assert sorted_list_sum(["aa", "bb", "aa", "cc"]) == ["aa", "aa", "bb", "cc"]

def test_same_length_strings():
    assert sorted_list_sum(["bc", "ab", "cd"]) == ["ab", "bc", "cd"]

def test_mixed_lengths_and_duplicates():
    assert sorted_list_sum(["a", "bb", "ccc", "bb", "dd"]) == ["bb", "bb", "dd"]

def test_single_even_length_string():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_odd_length_string():
    assert sorted_list_sum(["a"]) == []

def test_large_list():
    large_list = ["a" * i for i in range(1, 101) if i % 2 == 0]
    assert sorted_list_sum(large_list) == sorted(large_list, key=lambda s: (len(s), s))

def test_same_length_different_order():
    assert sorted_list_sum(["zz", "aa", "bb", "cc"]) == ["aa", "bb", "cc", "zz"]