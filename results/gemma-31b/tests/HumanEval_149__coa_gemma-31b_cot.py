
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


# Focus: Filtering Logic
def test_filtering_odd_lengths():
    assert sorted_list_sum(["a", "bb", "ccc", "dddd"]) == ["bb", "dddd"]

def test_filtering_all_odd():
    assert sorted_list_sum(["a", "abc", "abcde"]) == []

def test_filtering_all_even():
    assert sorted_list_sum(["aa", "bb", "cccc"]) == ["aa", "bb", "cccc"]

# Focus: Sorting Logic
def test_sorting_by_length():
    # Tests that strings are sorted primarily by length (ascending)
    assert sorted_list_sum(["abcd", "ab", "abcdef"]) == ["ab", "abcd", "abcdef"]

def test_sorting_alphabetically():
    # Tests that strings of the same length are sorted alphabetically
    assert sorted_list_sum(["cd", "ab", "ba", "ac"]) == ["ab", "ac", "ba", "cd"]

def test_sorting_combined_logic():
    # Tests both length and alphabetical sorting combined
    assert sorted_list_sum(["zz", "aaaa", "bb", "aa", "cc"]) == ["aa", "bb", "cc", "zz", "aaaa"]

# Focus: Boundary Values
def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd():
    assert sorted_list_sum(["a", "aaa", "abcde"]) == []

def test_sorted_list_sum_same_even_length_alphabetical():
    assert sorted_list_sum(["dc", "ba", "ac", "ab"]) == ["ab", "ac", "ba", "dc"]