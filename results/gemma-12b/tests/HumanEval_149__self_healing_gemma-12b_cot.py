
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
from your_module import sorted_list_sum  # Replace your_module

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_length():
    assert sorted_list_sum(["a", "bc", "def"]) == []

def test_all_even_length():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_lengths():
    assert sorted_list_sum(["aa", "a", "aaa", "cd"]) == ["aa", "cd"]

def test_mixed_lengths_with_duplicates():
    assert sorted_list_sum(["aa", "a", "aaa", "cd", "aa"]) == ["aa", "aa", "cd"]

def test_same_length_different_alphabetical():
    assert sorted_list_sum(["ab", "ac", "ad"]) == ["ab", "ac", "ad"]

def test_same_length_same_alphabetical():
    assert sorted_list_sum(["aa", "aa", "aa"]) == ["aa", "aa", "aa"]

def test_complex_case():
    assert sorted_list_sum(["abc", "a", "ab", "abcd", "bc", "c", "d", "aa"]) == ["aa", "ab", "bc", "cd"]

def test_long_strings():
    assert sorted_list_sum(["abcdefgh", "abcdefg", "abcdef"]) == ["abcdef", "abcdefg", "abcdefgh"]

def test_strings_with_spaces():
    assert sorted_list_sum(["a b", "a", "aa"]) == ["a", "aa"]

def test_strings_with_special_characters():
    assert sorted_list_sum(["!@#", "a!", "abc"]) == ["a!", "abc"]

def test_duplicate_even_length_strings():
    assert sorted_list_sum(["aa", "aa", "bb", "cc"]) == ["aa", "aa", "bb", "cc"]

def test_duplicate_odd_length_strings():
    assert sorted_list_sum(["a", "a", "b", "b"]) == []

def test_mixed_duplicates():
    assert sorted_list_sum(["aa", "a", "aaa", "aa", "cd", "cd"]) == ["aa", "aa", "cd", "cd"]