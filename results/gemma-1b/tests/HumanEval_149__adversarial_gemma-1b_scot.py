
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
    filtered_list = []
    for word in lst:
        if len(word) % 2 == 0:
            filtered_list.append(word)
    filtered_list.sort()
    return filtered_list

def test_list_sort_empty():
    assert list_sort([]) == []

def test_list_sort_single():
    assert list_sort(["a"]) == ["a"]

def test_list_sort_even_length():
    assert list_sort(["aa", "a", "aaa"]) == ["aa"]

def test_list_sort_odd_length():
    assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_list_sort_duplicates():
    assert list_sort(["aa", "a", "aaa", "aa"]) == ["aa", "aa", "aaa"]

def test_list_sort_mixed_lengths():
    assert list_sort(["ab", "a", "aaa", "cd", "aa"]) == ["ab", "aa", "cd", "aaa"]

def test_list_sort_with_duplicates():
    assert list_sort(["aa", "a", "aaa", "aa"]) == ["aa", "aa", "aaa"]