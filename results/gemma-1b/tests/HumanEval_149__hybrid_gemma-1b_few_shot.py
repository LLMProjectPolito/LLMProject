
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
    """ Sorts a list of strings by length of each word, and returns the sorted list. """
    return sorted(lst, key=lambda x: (len(x), x))

def test_list_sort_positive():
    assert list_sort(["aa", "a", "aaa"]) == ["aa"]

def test_list_sort_empty():
    assert list_sort([]) == []

def test_list_sort_single_element():
    assert list_sort(["hello"]) == ["hello"]

def test_list_sort_duplicate_elements():
    assert list_sort(["aa", "a", "aaa"]) == ["aa", "a", "aaa"]

def test_list_sort_mixed_lengths():
    assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_list_sort_same_length_words():
    assert list_sort(["aa", "a", "aaa"]) == ["aa", "a", "aaa"]

def test_list_sort_empty_string_list():
    assert list_sort([]) == []

def test_list_sort_mixed_string_list():
    assert list_sort(["a", "b", "c", "d"]) == ["a", "b", "c", "d"]

def test_list_sort_with_numbers():
    assert list_sort(["1", "2", "3", "1"]) == ["1", "2", "3", "1"]

def test_list_sort_with_mixed_types():
    assert list_sort(["1", "2", "3", "1.5"]) == ["1", "1.5", "2", "3"]

def test_list_sort_with_duplicates():
    assert list_sort(["aa", "a", "aaa", "aa"]) == ["aa", "a", "aaa", "aa"]

def test_list_sort_empty_string_list():
    assert list_sort([]) == []

def test_list_sort_empty_string_list_with_numbers():
    assert list_sort([]) == []

def test_list_sort_empty_string_list_with_mixed_types():
    assert list_sort([]) == []

def test_list_sort_with_special_characters():
    assert list_sort(["!@#", "a", "b"]) == ["!@#", "a", "b"]