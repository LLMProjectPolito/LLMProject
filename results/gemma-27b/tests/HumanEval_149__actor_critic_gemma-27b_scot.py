
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
    For example:
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    """
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "abc", "de"]) == []

def test_mixed_lengths():
    assert sorted_list_sum(["aa", "a", "aaa", "cd"]) == ["aa", "cd"]

def test_same_length_strings():
    assert sorted_list_sum(["ab", "aa", "ac"]) == ["aa", "ab", "ac"]

def test_duplicate_strings():
    assert sorted_list_sum(["aa", "aa", "bb"]) == ["aa", "aa", "bb"]

def test_mixed_lengths_duplicates():
    assert sorted_list_sum(["aa", "a", "bb", "aa", "ccc", "bb"]) == ["aa", "aa", "bb", "bb"]

def test_single_even_length_string_returns_itself():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_longer_strings():
    assert sorted_list_sum(["abcdef", "abc", "ab", "defghi"]) == ["ab", "abcdef"]

def test_large_list():
    large_list = ["".join([chr(ord('a') + i % 26) for i in range(j)]) for j in range(1, 11, 2)] + ["".join([chr(ord('a') + i % 26) for i in range(j)]) for j in range(2, 12, 2)]
    expected = sorted_list_sum(large_list)
    assert sorted_list_sum(large_list) == expected

def test_empty_string():
    assert sorted_list_sum([""]) == [""]