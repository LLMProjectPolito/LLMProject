
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

# STEP 1: REASONING
# The function `sorted_list_sum` takes a list of strings as input.
# It needs to remove strings with odd lengths.
# The remaining strings should be sorted first by their length (ascending).
# If strings have the same length, they should be sorted alphabetically (ascending).
# The function should return a new list containing the sorted strings.
# The input list is assumed to contain only strings.
# The function should handle duplicate strings correctly.

# STEP 2: PLAN
# We will create pytest test functions to cover the following scenarios:
# 1. Empty list: Test with an empty input list.
# 2. List with only odd-length strings: Test with a list containing only strings of odd lengths.
# 3. List with only even-length strings: Test with a list containing only strings of even lengths.
# 4. Mixed list: Test with a list containing a mix of even and odd length strings.
# 5. List with duplicate strings: Test with a list containing duplicate strings.
# 6. List with strings of varying lengths: Test with a list containing strings of varying lengths.
# 7. List with a single string: Test with a list containing a single string.

# STEP 3: CODE
import pytest
from typing import List

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
    result.sort(key=lambda s: (len(s), s))
    return result

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_only_odd_length_strings():
    assert sorted_list_sum(["a", "aaa"]) == []

def test_only_even_length_strings():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_list():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_duplicate_strings():
    assert sorted_list_sum(["aa", "a", "aa", "aaa"]) == ["aa", "aa"]

def test_varying_lengths():
    assert sorted_list_sum(["ab", "a", "aaa", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_single_string():
    assert sorted_list_sum(["aa"]) == ["aa"]