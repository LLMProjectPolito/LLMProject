
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

def test_sorted_list_sum_basic():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_sorted_list_sum_multiple():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd():
    assert sorted_list_sum(["a", "b", "c"]) == []

def test_sorted_list_sum_all_even():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_sorted_list_sum_mixed_same_length():
    assert sorted_list_sum(["aa", "bb", "a", "b"]) == ["aa", "bb"]

def test_sorted_list_sum_mixed_different_lengths():
    assert sorted_list_sum(["aa", "b", "ccc", "dd"]) == ["aa", "dd"]

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "aa", "a"]) == ["aa", "aa"]

def test_sorted_list_sum_same_length_alphabetical():
    assert sorted_list_sum(["bb", "aa", "cc"]) == ["aa", "bb", "cc"]

def test_sorted_list_sum_complex():
    assert sorted_list_sum(["abc", "a", "ab", "abcd", "abcde"]) == ["ab", "abc", "abcd"]