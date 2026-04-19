
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


# Focus: Logic Branches
import pytest

def test_sorted_list_sum_mixed_branches():
    # Tests filtering odd lengths, sorting by length, and alphabetical tie-breaking
    assert sorted_list_sum(["banana", "apple", "pear", "kiwi", "cherry"]) == ["kiwi", "pear", "banana", "cherry"]
    assert sorted_list_sum(["ab", "abc", "de", "fgh", "aa"]) == ["aa", "ab", "de"]

def test_sorted_list_sum_all_odd_or_empty():
    # Tests the branch where all elements are filtered out or input is empty
    assert sorted_list_sum(["a", "aaa", "abcde"]) == []
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_even_length_sorting():
    # Tests primary sort (length) and secondary sort (alphabetical) for even lengths
    assert sorted_list_sum(["zz", "aa", "bbbb", "cccc"]) == ["aa", "zz", "bbbb", "cccc"]
    assert sorted_list_sum(["abcd", "ef", "ghij", "kl"]) == ["ef", "kl", "abcd", "ghij"]

# Focus: Sorting Criteria
def test_sorting_by_length():
    # Tests that strings are sorted primarily by length (ascending)
    assert sorted_list_sum(["banana", "hi", "apple"]) == ["hi", "banana"]

def test_sorting_alphabetically():
    # Tests that strings of the same length are sorted alphabetically
    assert sorted_list_sum(["dc", "ba", "ca", "ab"]) == ["ab", "ba", "ca", "dc"]

def test_sorting_combined_criteria():
    # Tests both length and alphabetical sorting combined
    assert sorted_list_sum(["zz", "aa", "bbbb", "cccc", "dddd"]) == ["aa", "zz", "bbbb", "cccc", "dddd"]

# Focus: Boundary Values
def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd():
    assert sorted_list_sum(["a", "aaa", "abcde"]) == []

def test_sorted_list_sum_same_even_length():
    assert sorted_list_sum(["zz", "aa", "bb", "cc"]) == ["aa", "bb", "cc", "zz"]