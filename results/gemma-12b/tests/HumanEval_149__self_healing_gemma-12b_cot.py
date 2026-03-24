
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

def test_same_length_alphabetical():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_same_length_alphabetical_with_duplicates():
    assert sorted_list_sum(["ab", "cd", "ef", "ab"]) == ["ab", "ab", "cd", "ef"]

def test_mixed_lengths_and_alphabetical():
    assert sorted_list_sum(["aa", "a", "aaa", "cd", "bb", "cc"]) == ["aa", "bb", "cc", "cd"]

def test_longer_strings():
    assert sorted_list_sum(["abcdef", "abc", "ab", "a"]) == ["ab", "abc", "abcdef"]

def test_strings_with_spaces():
    assert sorted_list_sum(["a b", "aa", "aaa"]) == ["aa"]

def test_strings_with_special_characters():
    assert sorted_list_sum(["!@#", "!!", "!!!"]) == ["!!", "!!!"]

def test_duplicate_even_length_strings():
    assert sorted_list_sum(["aa", "aa", "aa"]) == ["aa", "aa", "aa"]

def test_duplicate_odd_length_strings():
    assert sorted_list_sum(["a", "a", "a"]) == []

def test_complex_scenario():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape"]) == ['kiwi', 'grape', 'apple', 'banana', 'orange']