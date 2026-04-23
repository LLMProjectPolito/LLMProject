
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
    result.sort(key=lambda x: (len(x), x))
    return result

@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        (["aa", "a", "aaa"], ["aa"]),
        (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
        (["a", "b", "c"], ["a", "b", "c"]),
        (["aa", "bb", "cc"], ["aa", "bb", "cc"]),
        (["a", "aa", "aaa"], ["a", "aa"]),
        (["aaa", "aa", "a"], ["a", "aa"]),
        ([], []),
        (["a"], ["a"]),
        (["aa", "a", "aaa", "aa", "a"], ["aa", "aa"]),
        (["abc", "def", "ghi", "jkl"], ["abc", "def", "ghi", "jkl"]),
        (["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]),
    ],
)
def test_sorted_list_sum(input_list, expected_output):
    assert sorted_list_sum(input_list) == expected_output

@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        (["aa", "ab", "aaa", "a"], ["aa", "ab", "a"]),
        (["a", "aa", "aaa", "b"], ["a", "aa", "b"]),
        (["aaa", "aa", "a"], ["a", "aa"]),
        (["a", "b", "c"], ["a", "b", "c"]),
    ],
)
def test_sorted_list_sum_with_same_length(input_list, expected_output):
    assert sorted_list_sum(input_list) == expected_output

@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        (["aa", "bb", "cc", "dd"], ["aa", "bb", "cc", "dd"]),
        (["a", "b", "c", "d"], ["a", "b", "c", "d"]),
        (["aa", "bb", "cc"], ["aa", "bb", "cc"])
    ]
)
def test_sorted_list_sum_all_same_length(input_list, expected_output):
    assert sorted_list_sum(input_list) == expected_output