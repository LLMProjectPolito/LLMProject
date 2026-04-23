
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
    The sorting is case-sensitive.
    Leading/trailing spaces are considered when calculating string length.
    For example:
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    """
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings

def test_empty_list_returns_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths_returns_empty_list():
    assert sorted_list_sum(["a", "aaa", "abc"]) == []

def test_mixed_lengths():
    assert sorted_list_sum(["aa", "a", "aaa", "bb"]) == ["aa", "bb"]

def test_duplicate_even_lengths():
    assert sorted_list_sum(["aa", "bb", "aa", "cc"]) == ["aa", "aa", "bb", "cc"]

def test_same_length_alphabetical():
    assert sorted_list_sum(["ab", "cd", "aa"]) == ["aa", "ab", "cd"]

def test_longer_strings():
    assert sorted_list_sum(["abcdef", "abc", "abcd", "abcde"]) == ["abcd"]

def test_empty_string_among_others():
    assert sorted_list_sum(["", "a", "aa"]) == ["aa"]

def test_only_empty_string():
    assert sorted_list_sum([""]) == [""]

def test_mixed_case():
    assert sorted_list_sum(["aA", "bb", "Aa"]) == ["aA", "Aa", "bb"]

def test_numbers_as_strings():
    assert sorted_list_sum(["12", "1", "123", "124"]) == ["12", "124"]

def test_mixed_odd_and_even_same_length():
    assert sorted_list_sum(["ba", "aa", "ab"]) == ["aa", "ab", "ba"]

def test_leading_trailing_spaces():
    assert sorted_list_sum(["  aa", "aa  ", "bb"]) == ["  aa", "aa  ", "bb"]

def test_only_spaces():
    assert sorted_list_sum(["   "]) == ["   "]

def test_very_long_strings():
    long_string = "a" * 1000
    assert sorted_list_sum([long_string, "aa"]) == ["aa", long_string]

def test_unicode_characters():
    assert sorted_list_sum(["你好", "世界", "a"]) == ["a"]