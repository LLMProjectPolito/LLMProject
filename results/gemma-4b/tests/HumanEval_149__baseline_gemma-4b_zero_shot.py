
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
    assert sorted_list_sum(["a", "b", "c"]) == []

def test_all_even_length():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_odd_even():
    assert sorted_list_sum(["aa", "a", "aaa", "cd"]) == ["aa", "cd"]

def test_duplicate_even():
    assert sorted_list_sum(["aa", "aa", "bb", "bb"]) == ["aa", "aa", "bb", "bb"]

def test_duplicate_odd():
    assert sorted_list_sum(["a", "a", "b", "b"]) == []

def test_mixed_duplicate():
    assert sorted_list_sum(["aa", "a", "aaa", "cd", "aa"]) == ["aa", "aa", "cd"]

def test_same_length_different_chars():
    assert sorted_list_sum(["ab", "ac", "ad"]) == ["ab", "ac", "ad"]

def test_same_length_same_chars():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_complex_case():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape"]) == ["banana", "orange"]

def test_single_element():
    assert sorted_list_sum(["abc"]) == []

def test_single_even_element():
    assert sorted_list_sum(["abcd"]) == ["abcd"]