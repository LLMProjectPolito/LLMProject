
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
    """
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "bbb", "ccccc"]) == []

def test_mixed_lengths():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "c"]) == ["aa", "bb"]

def test_duplicates():
    assert sorted_list_sum(["aa", "aa", "bb", "cc", "cc"]) == ["aa", "aa", "bb", "cc", "cc"]

def test_same_length_alphabetical():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_same_length_different_alphabetical():
    assert sorted_list_sum(["bc", "ac", "ab"]) == ["ab", "ac", "bc"]

def test_complex_list():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "c", "cc", "ddd", "ee", "ff", "g", "hhhh"]) == ["aa", "bb", "cc", "ee", "ff", "hhhh"]

def test_same_length_alphabetical_explicit():
    assert sorted_list_sum(["ab", "ba", "cd"]) == ["ab", "ba", "cd"]

def test_case_insensitive():
    assert sorted_list_sum(["AA", "aa", "Bb"]) == ["AA", "aa", "Bb"]

def test_single_element():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_long_strings():
    assert sorted_list_sum(["abcdef", "abcde", "abcd"]) == ["abcd", "abcde"]

def test_empty_string():
    assert sorted_list_sum([""]) == [""]

def test_single_odd_length_string():
    assert sorted_list_sum(["a", "bb"]) == ["bb"]