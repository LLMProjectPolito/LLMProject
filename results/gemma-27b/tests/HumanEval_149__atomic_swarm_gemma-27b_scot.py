import pytest
import math

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
    new_lst = [s for s in lst if len(s) % 2 == 0]
    new_lst.sort(key=lambda s: (len(s), s))
    return new_lst

def test_basic():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

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
    new_list = [word for word in lst if len(word) % 2 == 0]
    new_list.sort(key=lambda x: (len(x), x))
    return new_list

def test_empty_list():
    assert sorted_list_sum([]) == []

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
    new_lst = [s for s in lst if len(s) % 2 == 0]
    new_lst.sort(key=lambda s: (len(s), s))
    return new_lst

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "abc", "e"]) == []

def test_mixed_lengths():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_duplicates():
    assert sorted_list_sum(["ab", "ab", "cd", "cd"]) == ["ab", "ab", "cd", "cd"]

def test_same_length_alphabetical():
    assert sorted_list_sum(["bc", "ab", "cd"]) == ["ab", "bc", "cd"]

def test_long_strings():
    assert sorted_list_sum(["abcdef", "abc", "def"]) == ["abcdef"]

def test_mixed_case():
    assert sorted_list_sum(["aA", "aa", "AB"]) == ["aA", "aa", "AB"]

def test_special_characters():
    assert sorted_list_sum(["!@#", "abc", "$%^"]) == ["!@#", "$%^"]

def test_numbers_as_strings():
    assert sorted_list_sum(["12", "1", "123"]) == ["12"]

def test_list_with_one_even_length_string():
    assert sorted_list_sum(["a", "aa", "b"]) == ["aa"]