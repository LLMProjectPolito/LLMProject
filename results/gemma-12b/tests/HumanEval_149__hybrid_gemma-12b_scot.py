
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

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "bbb", "ccccc"]) == []

def test_all_even_lengths():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_lengths():
    assert sorted_list_sum(["aa", "a", "aaa", "bb"]) == ["aa", "bb"]

def test_mixed_lengths_2():
    assert sorted_list_sum(["aa", "a", "bbb", "cc"]) == ["aa", "cc"]

def test_duplicate_strings():
    assert sorted_list_sum(["aa", "a", "aa", "bbb", "cc"]) == ["aa", "aa", "cc"]

def test_duplicate_strings_2():
    assert sorted_list_sum(["aa", "a", "aa", "bbb", "cc", "cc"]) == ["aa", "aa", "cc", "cc"]

def test_same_length_strings():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_same_length_strings_2():
    assert sorted_list_sum(["ab", "cd", "ef", "gh"]) == ["ab", "cd", "ef", "gh"]

def test_same_length_strings_with_duplicates():
    assert sorted_list_sum(["ab", "ab", "cd", "ef"]) == ["ab", "ab", "cd", "ef"]

def test_complex_list():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "cc", "bbb", "dd", "ee", "fff", "gg"]) == ["aa", "bb", "cc", "dd", "ee"]

def test_single_even_length_string():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_odd_length_string():
    assert sorted_list_sum(["a"]) == []

def test_long_list():
    input_list = ["aa", "a", "bbb", "cc", "dddd", "eee", "ff", "gggg", "h", "iiiii"]
    expected_output = ["aa", "cc", "ff"]
    assert sorted_list_sum(input_list) == expected_output

def test_strings_with_spaces():
    assert sorted_list_sum(["aa", " a ", "b"]) == ["aa", " a "]