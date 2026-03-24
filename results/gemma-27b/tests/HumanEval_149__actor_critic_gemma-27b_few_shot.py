
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
    For example:
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    """
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings

import pytest

def test_sorted_list_sum_basic():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_odd_lengths():
    assert sorted_list_sum(["a", "c", "e"]) == []

def test_sorted_list_sum_mixed():
    assert sorted_list_sum(["ab", "cd", "aa", "bb"]) == ["aa", "bb", "ab", "cd"]

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "aa", "ab", "cd"]) == ["aa", "aa", "ab", "cd"]

def test_sorted_list_sum_different_lengths():
    assert sorted_list_sum(["a", "aa", "aaa", "aaaa"]) == ["aa", "aaaa"]

def test_sorted_list_sum_numbers_as_strings():
    assert sorted_list_sum(["12", "1", "123"]) == ["12"]

def test_sorted_list_sum_alphabetical_tie_breaking():
    assert sorted_list_sum(["ba", "aa", "bb"]) == ["aa", "bb", "ba"]

def test_sorted_list_sum_complex():
    assert sorted_list_sum(["abc", "ab", "a", "abcd", "ef", "e", "efgh", "cd"]) == ["ab", "cd", "ef", "abcd", "efgh"]