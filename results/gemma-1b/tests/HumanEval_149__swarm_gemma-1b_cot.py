
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

def list_sort(lst):
    new_lst = []
    for s in lst:
        if len(s) % 2 == 0:
            new_lst.append(s)
        else:
            if s < new_lst[0]:
                new_lst.append(s)
            else:
                new_lst.append(s)
    new_lst.sort()
    return new_lst

def list_sort(lst):
    new_lst = []
    for s in lst:
        if len(s) % 2 == 0:
            new_lst.append(s)
        else:
            if s < new_lst[0]:
                new_lst.append(s)
            else:
                new_lst.append(s)
    new_lst.sort()
    return new_lst

def list_sort(lst):
    new_lst = []
    for s in lst:
        if len(s) % 2 == 0:
            new_lst.append(s)
        else:
            if s < new_lst[0]:
                new_lst.append(s)
            else:
                new_lst.append(s)
    new_lst.sort()
    return new_lst

def test_list_sort():
    assert list_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert list_sort([1, 3, 2, 4, 5]) == [1, 2, 3, 4, 5]
    assert list_sort([2, 4, 1, 3, 5]) == [1, 2, 3, 4, 5]
    assert list_sort([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert list_sort([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert list_sort([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert list_sort([]) == []
    assert list_sort([5]) == [5]
    assert list_sort([1]) == [1]
    assert list_sort([2]) == [2]
    assert list_sort([3]) == [3]
    assert list_sort([4]) == [4]
    assert list_sort([5, 6]) == [5, 6]
    assert list_sort([6, 5]) == [5, 6]