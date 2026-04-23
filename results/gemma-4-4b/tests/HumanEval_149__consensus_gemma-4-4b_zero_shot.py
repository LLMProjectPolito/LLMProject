
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
    result = [s for s in lst if len(s) % 2 == 0]
    result.sort(key=lambda s: (len(s), s))
    return result

@pytest.fixture
def test_sorted_list_sum_empty_list():
    return []

@pytest.mark.parametrize("input_list, expected_output", [
    (["aa", "a", "aaa"], ["aa"]),
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
    (["aa", "bb", "cc", "dd"], ["aa", "bb", "cc", "dd"]),
    (["a", "b", "c", "d"], []),
    (["aa", "bb", "cc", "dd", "ee"], ["aa", "bb", "cc", "dd"]),
    (["ee", "dd", "cc", "bb", "aa"], ["aa", "bb", "cc", "dd"]),
    (["ab", "cd", "ef", "gh"], ["ab", "cd", "ef", "gh"]),
    (["a", "aa", "aaa", "aaaa"], ["aa", "aaa", "aaaa"]),
    (["aaaa", "aaa", "aa", "a"], ["aa", "aaa", "aaaa"]),
    (["abc", "def", "ghi"], []),
    ([], [])
])
def test_sorted_list_sum(input_list, expected_output):
    assert sorted_list_sum(input_list) == expected_output

@pytest.mark.parametrize("input_list, expected_output", [
    (["aa", "a", "aaa", "aa", "ab"], ["aa", "aa", "ab"]),
    (["ab", "a", "aaa", "cd", "ab"], ["ab", "cd", "ab"]),
    (["aa", "bb", "cc", "dd", "aa", "bb"], ["aa", "aa", "bb", "bb", "cc", "dd"]),
])
def test_sorted_list_sum_duplicates(input_list, expected_output):
    assert sorted_list_sum(input_list) == expected_output