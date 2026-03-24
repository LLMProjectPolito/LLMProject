
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
    new_lst = [s for s in lst if len(s) % 2 == 0]
    new_lst.sort(key=lambda s: (len(s), s))
    return new_lst

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "abc", ""]) == []

def test_mixed_lengths():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_duplicate_even_lengths():
    assert sorted_list_sum(["aa", "aa", "bb"]) == ["aa", "aa", "bb"]

def test_duplicate_even_lengths_different_order():
    assert sorted_list_sum(["bb", "aa", "aa"]) == ["aa", "aa", "bb"]

def test_same_length_alphabetical():
    assert sorted_list_sum(["cb", "ab"]) == ["ab", "cb"]

def test_edge_case_empty_string():
    assert sorted_list_sum(["", "aa", "bb"]) == ["", "aa", "bb"]

def test_edge_case_long_strings():
    assert sorted_list_sum(["abcdef", "ghijkl", "mnopqr"]) == ["abcdef", "ghijkl", "mnopqr"]

def test_edge_case_long_strings_mixed():
    assert sorted_list_sum(["abcdef", "ghi", "mnopqr"]) == ["abcdef", "ghijkl"]

def test_edge_case_with_numbers_as_strings():
    assert sorted_list_sum(["12", "3", "456"]) == ["12"]

def test_edge_case_special_characters():
    assert sorted_list_sum(["!@#", "abc", "def"]) == ["!@#", "abc", "def"]

def test_edge_case_mixed_case():
    assert sorted_list_sum(["aA", "bb", "Cc"]) == ["aA", "bb", "Cc"]

def test_edge_case_unicode_characters():
    assert sorted_list_sum(["你好", "世界"]) == []

def test_edge_case_long_even_string():
    assert sorted_list_sum(["abcdefgh"]) == ["abcdefgh"]

def test_edge_case_long_odd_string():
    assert sorted_list_sum(["abcdefghi"]) == []

def test_edge_case_empty_string_and_odd_string():
    assert sorted_list_sum(["", "a"]) == []

def test_edge_case_empty_string_and_even_string():
    assert sorted_list_sum(["", "aa"]) == [""]