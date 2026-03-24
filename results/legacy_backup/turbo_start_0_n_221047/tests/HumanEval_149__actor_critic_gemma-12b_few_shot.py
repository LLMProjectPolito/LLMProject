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
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    """
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings


import pytest

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_only_odd():
    assert sorted_list_sum(["a", "aaa", "abcde"]) == []

def test_sorted_list_sum_single_element():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_sorted_list_sum_same_length_alphabetical():
    assert sorted_list_sum(["bc", "ac", "ab"]) == ["ab", "ac", "bc"]

def test_sorted_list_sum_longer_strings():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grapefruit"]) == ["kiwi"]

def test_sorted_list_sum_mixed():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "ccc", "dd"]) == ["aa", "bb", "dd"]

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "a", "aa", "aaa", "bb", "bb", "ccc"]) == ["aa", "aa", "bb", "bb"]

def test_sorted_list_sum_same_length():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_sorted_list_sum_same_length_mixed():
    assert sorted_list_sum(["ab", "a", "cd", "ef", "aaa"]) == ["ab", "cd", "ef"]

def test_sorted_list_sum_varying_lengths():
    assert sorted_list_sum(["a", "aa", "aaa", "aaaa", "aaaaa"]) == ["aa", "aaaa"]

def test_sorted_list_sum_duplicates_same_length():
    assert sorted_list_sum(["aa", "bb", "cc", "aa", "bb"]) == ["aa", "aa", "bb", "bb", "cc"]