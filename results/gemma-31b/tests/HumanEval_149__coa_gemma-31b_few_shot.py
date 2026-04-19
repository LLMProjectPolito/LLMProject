
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
    # Test that strings with odd lengths are removed and even lengths are kept
    assert sorted_list_sum(["a", "bb", "ccc", "dddd"]) == ["bb", "dddd"]
    assert sorted_list_sum(["apple", "pear", "banana", "kiwi"]) == ["kiwi", "pear"]

def test_filtering_all_odd():
    # Test that a list containing only odd-length strings returns an empty list
    assert sorted_list_sum(["a", "aaa", "aaaaa"]) == []
    assert sorted_list_sum(["hello", "world"]) == []

def test_filtering_all_even():
    # Test that a list containing only even-length strings keeps all elements
    assert sorted_list_sum(["aa", "bbbb", "cc"]) == ["aa", "cc", "bbbb"]

# Focus: Sorting Criteria
def test_sorting_criteria_alphabetical_tie():
    # Tests that words of the same even length are sorted alphabetically
    assert sorted_list_sum(["dc", "ba", "zz", "aa"]) == ["aa", "ba", "dc", "zz"]

def test_sorting_criteria_length_then_alphabetical():
    # Tests ascending length first, then alphabetical tie-breaking
    assert sorted_list_sum(["fedc", "abcd", "ba", "dc"]) == ["ba", "dc", "abcd", "fedc"]

def test_sorting_criteria_mixed_even_lengths():
    # Tests sorting across multiple different even lengths
    assert sorted_list_sum(["abcdef", "ab", "abcd", "aa"]) == ["aa", "ab", "abcd", "abcdef"]

# Focus: Boundary Values
import pytest

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd():
    assert sorted_list_sum(["a", "aaa", "abcde", "123"]) == []

def test_sorted_list_sum_even_boundaries():
    # Tests minimum even length (2), alphabetical sorting for same length, and length sorting
    assert sorted_list_sum(["zz", "aa", "bbbb", "cc"]) == ["aa", "cc", "zz", "bbbb"]