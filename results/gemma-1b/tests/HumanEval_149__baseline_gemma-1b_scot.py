
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

def list_sort(lst):
    """Sorts a list of strings based on length, ascending by length, and alphabetically for duplicates."""
    return sorted(lst, key=lambda x: (len(x), x))

def test_empty_list():
    assert list_sort([]) == []

def test_single_element():
    assert list_sort(["a"]) == ["a"]

def test_example_1():
    assert list_sort(["aa", "a", "aaa"]) == ["aa"]

def test_example_2():
    assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_example_3():
    assert list_sort(["abc", "ab", "a"]) == ["a", "ab", "abc"]

def test_duplicate_elements():
    assert list_sort(["aa", "a", "aaa", "aa"]) == ["aa", "a", "aa", "aaa"]