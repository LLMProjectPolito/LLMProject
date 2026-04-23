
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
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_list_with_only_odd_length_strings():
        assert sorted_list_sum(["a", "bbb", "ccccc"]) == []

def test_same_length_alphabetical():
    assert sorted_list_sum(["cd", "ab", "ef"]) == ["ab", "cd", "ef"]

def test_same_length_alphabetical_different_order():
    assert sorted_list_sum(["zz", "aa", "bb"]) == ["aa", "bb", "zz"]

def test_empty_string():
    assert sorted_list_sum([""]) == [""]

def test_single_even_length_string():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_odd_length_string():
    assert sorted_list_sum(["a"]) == []

def test_mixed_list():
    assert sorted_list_sum(["aa", "a", "aaa", "cd"]) == ["aa", "cd"]

def test_list_with_duplicates():
    assert sorted_list_sum(["aa", "aa", "a", "aaa", "bb", "bb"]) == ["aa", "aa", "bb", "bb"]

def test_list_with_mixed_lengths_and_duplicates():
    assert sorted_list_sum(["aa", "a", "aaa", "cd", "aa", "bb"]) == ["aa", "aa", "bb", "cd"]

def test_list_with_long_strings():
    assert sorted_list_sum(["abcdef", "abcde", "abcdefg"]) == ["abcdef"]

def test_list_with_special_characters():
    assert sorted_list_sum(["a!", "aa", "a?"]) == ["aa"]

def test_unicode_characters():
    assert sorted_list_sum(["你好", "世界"]) == ["你好", "世界"]

def test_edge_case_one_even_one_odd():
    assert sorted_list_sum(["a", "aa"]) == ["aa"]

def test_edge_case_empty_and_odd():
    assert sorted_list_sum(["", "a"]) == [""]

def test_numbers_as_strings():
    assert sorted_list_sum(["1", "12", "123"]) == ["12"]

def test_mixed_case_strings():
    assert sorted_list_sum(["AA", "aa"]) == ["aa", "AA"]