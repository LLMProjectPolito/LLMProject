import pytest
import math


# Focus: Boundary Values
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
    new_list = []
    for s in lst:
        if len(s) % 2 == 0:
            new_list.append(s)
    new_list.sort(key=lambda x: (len(x), x))
    return new_list

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_length():
    assert sorted_list_sum(["aa", "a", "aaa"]) == []

def test_all_even_length():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_mixed_odd_even():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

# Focus: Type Scenarios
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
    new_list = []
    for s in lst:
        if len(s) % 2 == 0:
            new_list.append(s)
    new_list.sort(key=lambda x: (len(x), x))
    return new_list

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_length():
    assert sorted_list_sum(["aa", "a", "aaa"]) == []

def test_all_even_length():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_mixed_odd_even():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

# Focus: Logic Branches
import pytest

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_odd_lengths():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_sorted_list_sum_mixed_lengths():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]