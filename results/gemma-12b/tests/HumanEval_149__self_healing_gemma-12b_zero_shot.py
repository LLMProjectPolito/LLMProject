
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
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "ccc", "d"]) == ["aa", "bb"]

def test_mixed_lengths_with_duplicates():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "ccc", "d", "aa"]) == ["aa", "aa", "bb"]

def test_same_length_alphabetical():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_same_length_alphabetical_with_duplicates():
    assert sorted_list_sum(["ab", "cd", "ef", "ab"]) == ["ab", "ab", "cd", "ef"]

def test_complex_case():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape"]) == ["kiwi", "grape"]

def test_case_with_empty_string():
    assert sorted_list_sum(["", "a", "aa"]) == ["", "aa"]

def test_case_with_special_characters():
    assert sorted_list_sum(["a!", "b?", "c#"]) == ["a!", "b?", "c#"]

def test_case_with_numbers_as_strings():
    assert sorted_list_sum(["12", "1", "123"]) == ["12"]

def test_case_with_mixed_characters():
    assert sorted_list_sum(["a1", "b2", "c3"]) == ["a1", "b2", "c3"]

def test_long_strings():
    assert sorted_list_sum(["abcdefgh", "abcdefg", "abcdef"]) == ["abcdef", "abcdefg"]

def test_duplicate_even_length_strings():
    assert sorted_list_sum(["aa", "aa", "aa"]) == ["aa", "aa", "aa"]

def test_duplicate_odd_length_strings():
    assert sorted_list_sum(["a", "a", "a"]) == []