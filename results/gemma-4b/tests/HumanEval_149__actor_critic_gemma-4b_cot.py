
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
    assert sorted_list_sum(["aa", "a", "aaa"]) => ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    filtered_list = [s for s in lst if len(s) % 2 == 0]
    filtered_list.sort(key=lambda x: (len(x), x))
    return filtered_list

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_length_strings():
    assert sorted_list_sum(["aa", "a", "aaa"]) == []

def test_all_even_length_strings():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_mixed_odd_and_even_length_strings():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_duplicate_strings():
    assert sorted_list_sum(["aa", "ab", "aa", "cd"]) == ["aa", "aa", "ab", "cd"]

def test_strings_with_same_length_different_alphabetical_order():
    assert sorted_list_sum(["abc", "abd", "abe"]) == ["abc", "abd", "abe"]

def test_single_even_length_string():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_odd_length_string():
    assert sorted_list_sum(["a"]) == []

def test_longer_list_with_mixed_lengths():
    assert sorted_list_sum(["aa", "ab", "abc", "a", "cd", "efg", "aaa"]) == ["aa", "ab", "cd", "efg"]

def test_list_with_empty_string():
    assert sorted_list_sum(["", "aa", ""]) == ["","aa"]