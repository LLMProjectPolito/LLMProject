
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
    result = [s for s in lst if len(s) % 2 == 0]
    result.sort(key=lambda x: (len(x), x))
    return result

def test_sorted_list_sum_basic():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert sorted_list_sum(["abc", "def", "ghi"]) == ["def", "ghi"]
    assert sorted_list_sum(["a", "aa", "aaa", "aaaa"]) == ["aa", "aaaa"]

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd():
    assert sorted_list_sum(["a", "b", "c"]) == []

def test_sorted_list_sum_all_even():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "a", "aa", "aaa"]) == ["aa", "aa"]

def test_sorted_list_sum_mixed():
    assert sorted_list_sum(["aa", "a", "aaa", "ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_sorted_list_sum_long_strings():
    assert sorted_list_sum(["abcdef", "ghijkl", "mnopqr"]) == ["ghijkl", "mnopqr"]

def test_sorted_list_sum_single_element():
    assert sorted_list_sum(["a"]) == []
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_sorted_list_sum_large_list():
    large_list = [str(i) * 2 for i in range(100)]
    assert sorted_list_sum(large_list) == [str(i) * 2 for i in range(50)]