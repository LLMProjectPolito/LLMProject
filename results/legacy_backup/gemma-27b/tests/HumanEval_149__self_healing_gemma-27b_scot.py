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
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings

import pytest

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_only_odd_length_strings():
    assert sorted_list_sum(["a", "abc", "e"]) == []

def test_only_even_length_strings():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_odd_and_even_length_strings():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_duplicate_strings():
    assert sorted_list_sum(["aa", "bb", "aa", "cc", "bb"]) == ["aa", "aa", "bb", "bb", "cc"]

def test_strings_of_same_length():
    assert sorted_list_sum(["ab", "cd", "ac"]) == ["ac", "ab", "cd"]

def test_single_even_length_string():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_odd_length_string():
    assert sorted_list_sum(["a"]) == []

def test_larger_list():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape", "pear"]) == ["pear"]

def test_list_with_empty_string():
    assert sorted_list_sum(["", "a", "aa"]) == ["aa"]

def test_list_with_multiple_empty_strings():
    assert sorted_list_sum(["", "", "aa", "bb"]) == ["aa", "bb"]

def test_list_with_same_length_and_duplicates():
    assert sorted_list_sum(["ab", "ab", "cd", "cd"]) == ["ab", "ab", "cd", "cd"]