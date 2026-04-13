
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
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "abc", "def"]) == []

def test_all_even_lengths():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_lengths():
    assert sorted_list_sum(["aa", "a", "aaa", "bb"]) == ["aa", "bb"]

def test_duplicate_even_lengths():
    assert sorted_list_sum(["aa", "bb", "aa", "cc"]) == ["aa", "aa", "bb", "cc"]

def test_same_length_alphabetical():
    assert sorted_list_sum(["cb", "ab", "db"]) == ["ab", "cb", "db"]

def test_mixed_lengths_and_duplicates():
    assert sorted_list_sum(["ab", "a", "abc", "cd", "ab"]) == ["ab", "ab", "cd"]

def test_long_strings():
    assert sorted_list_sum(["abcdef", "abc", "defgh"]) == ["abcdef", "defgh"]

def test_number_as_string():
    assert sorted_list_sum(["12", "a", "34"]) == ["12", "34"]

def test_unicode_strings():
    assert sorted_list_sum(["你好", "世界", "你好世界"]) == ["你好", "世界"]

def test_numeric_strings_odd_length():
    assert sorted_list_sum(["1", "12", "123"]) == ["12"]

def test_large_list():
    large_list = ["".join([chr(ord('a') + i % 26) for i in range(j)]) for j in range(2, 11, 2)] * 5
    expected_result = sorted([s for s in large_list if len(s) % 2 == 0], key=lambda s: (len(s), s))
    assert sorted_list_sum(large_list) == expected_result