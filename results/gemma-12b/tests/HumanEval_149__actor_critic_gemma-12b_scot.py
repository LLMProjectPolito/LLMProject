
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

def test_all_even_length_strings():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_length_strings():
    assert sorted_list_sum(["aa", "a", "aaa", "bb"]) == ["aa", "bb"]

def test_duplicates_even_length():
    assert sorted_list_sum(["aa", "aa", "bb", "cc", "bb"]) == ["aa", "aa", "bb", "bb", "cc"]

def test_same_length_different_alphabetical():
    assert sorted_list_sum(["ab", "ac", "ba", "ca"]) == ["ab", "ac", "ba", "ca"]

def test_complex_list():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "cc", "b", "dddd", "eee", "ff"]) == ["aa", "bb", "cc", "dddd"]

def test_case_sensitivity():
    assert sorted_list_sum(["aa", "Aa", "bb"]) == ["aa", "bb"]

def test_unicode_strings():
    assert sorted_list_sum(["你好", "世界", "a", "aa"]) == ["aa", "你好", "世界"]

def test_list_with_numbers():
    assert sorted_list_sum(["aa", 1, "bb", 2, "cc"]) == ["aa", "bb", "cc"]

def test_list_with_special_characters():
    assert sorted_list_sum(["!@#", "aa", "$%^"]) == ["aa"]

def test_list_with_empty_strings():
    assert sorted_list_sum(["aa", "", "bb", ""]) == ["aa", "bb"]

def test_invalid_input_type():
    with pytest.raises(TypeError):
        sorted_list_sum(123)