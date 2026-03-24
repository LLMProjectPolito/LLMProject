
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
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "b", "ccc"]) == ["aa", "bb", "ccc"]

def test_mixed_lengths_with_duplicates():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "a", "ccc", "aa"]) == ["aa", "aa", "bb", "ccc"]

def test_same_length_alphabetical():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_same_length_alphabetical_with_odd():
    assert sorted_list_sum(["ab", "a", "cd", "ef", "b"]) == ["ab", "cd", "ef"]

def test_complex_case():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape"]) == ["kiwi", "grape"]

def test_duplicate_same_length():
    assert sorted_list_sum(["aa", "bb", "aa", "cc", "bb"]) == ["aa", "aa", "bb", "bb", "cc"]

def test_single_element_even():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_element_odd():
    assert sorted_list_sum(["a"]) == []

def test_long_strings():
    assert sorted_list_sum(["abcdefgh", "abcde", "abcdef"]) == ["abcde", "abcdef", "abcdefgh"]

def test_strings_with_spaces():
    assert sorted_list_sum(["a b", "c d e", "f"]) == ["a b", "c d e"]

def test_strings_with_special_characters():
    assert sorted_list_sum(["a!", "b?", "c#"]) == ["a!", "b?", "c#"]

def test_strings_with_numbers():
    assert sorted_list_sum(["12", "1", "123"]) == ["12", "123"]

def test_all_same_length_different_alphabetical():
    assert sorted_list_sum(["zebra", "apple", "banana"]) == ["apple", "banana", "zebra"]