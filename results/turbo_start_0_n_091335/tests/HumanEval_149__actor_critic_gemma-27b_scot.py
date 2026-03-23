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
    assert list_sort(["aa", "a", "aaa"]) == ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    """
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "abc", "xyz"]) == []

def test_mixed_lengths_with_duplicates():
    assert sorted_list_sum(["a", "bb", "ccc", "bb", "dd"]) == ["bb", "bb", "dd"]

def test_same_length_strings():
    assert sorted_list_sum(["bc", "ab", "cd"]) == ["ab", "bc", "cd"]

def test_complex_list():
    assert sorted_list_sum(["abc", "aa", "b", "cc", "ddd", "aa", "eee"]) == ["aa", "aa", "cc"]

def test_single_even_length_string():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_even_length_strings_only():
    assert sorted_list_sum(["aa", "bb", "cc", "dd"]) == ["aa", "bb", "cc", "dd"]