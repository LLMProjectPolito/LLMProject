
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

def test_empty_list():
    """Test with an empty list."""
    assert sorted_list_sum([]) == []

def test_list_with_only_odd_length_strings():
    """Test with a list containing only strings with odd lengths."""
    assert sorted_list_sum(["a", "abc", "de"]) == []

def test_list_with_duplicate_strings_of_same_length():
    """Test with duplicate strings of the same length."""
    assert sorted_list_sum(["aa", "aa", "bb", "cc"]) == ["aa", "aa", "bb", "cc"]

def test_list_with_duplicate_strings_of_different_lengths():
    """Test with duplicate strings of different lengths."""
    assert sorted_list_sum(["a", "aa", "a", "aaa", "aa"]) == ["a", "a", "aa", "aa"]

def test_list_with_mixed_lengths_and_duplicates():
    """Test with a list containing strings of mixed lengths and duplicates."""
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "aa", "c", "bbb"]) == ["aa", "aa", "bb", "bbb"]