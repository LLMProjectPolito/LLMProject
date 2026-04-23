
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
from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
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
def test_empty_list():
    return []

@pytest.fixture
def test_single_element_even_length():
    return ["aa"]

@pytest.fixture
def test_single_element_odd_length():
    return ["a"]

@pytest.fixture
def test_multiple_elements_mixed_lengths():
    return ["aa", "a", "aaa", "ab", "cd"]

@pytest.fixture
def test_duplicates():
    return ["aa", "aa", "a", "ab", "ab"]

@pytest.fixture
def test_all_even_lengths():
    return ["aa", "bb", "cc", "dd"]

@pytest.fixture
def test_all_odd_lengths():
    return ["a", "b", "c", "d"]

@pytest.mark.parametrize("input_list, expected_output", [
    (["aa", "a", "aaa"], ["aa"]),
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
    ([], []),
    (["aa"], ["aa"]),
    (["a"], []),
    (["aa", "bb", "cc", "dd"], ["aa", "bb", "cc", "dd"]),
    (["a", "b", "c", "d"], []),
    (["aa", "aa", "a", "ab", "ab"], ["aa", "aa", "ab", "ab"]),
    (["abc", "def", "ghi", "jkl"], ["def", "ghi", "jkl"]),
    (["abc", "def", "ghi", "jkl", "def"], ["def", "def", "ghi", "jkl"]),
])
def test_sorted_list_sum(input_list: List[str], expected_output: List[str]):
    assert sorted_list_sum(input_list) == expected_output

@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        (["aa", "a", "aaa"], ["aa"]),
        (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
        (["aa", "bb", "cc", "dd"], ["aa", "bb", "cc", "dd"]),
        (["a", "b", "c", "d"], []),
        ([], []),
        (["aa", "aa", "bb", "bb"], ["aa", "aa", "bb", "bb"]),
        (["abc", "def", "ghi"], []),
        (["a", "aa", "aaa", "aaaa"], ["aa", "aaa", "aaaa"]),
        (["zz", "xx", "vv", "uu"], ["xx", "uu", "vv", "zz"]),
        (["abc", "def", "ghi", "jkl"], ["def", "ghi", "jkl"]),
        (["a", "aa", "b", "bb"], ["aa", "bb"]),
    ],
)
def test_sorted_list_sum_duplicates(input_list: List[str], expected_output: List[str]):
    assert sorted_list_sum(input_list) == expected_output

@pytest.mark.parametrize(
    "input_list, expected_output",
    [
        (["aa", "a", "aaa", "bb", "b"], ["aa", "bb"]),
        (["ab", "a", "aaa", "cd", "bc"], ["ab", "cd", "bc"]),
        (["abc", "def", "ghi", "jkl"], []),
        (["a", "aa", "aaa", "aaaa"], ["aa", "aaa", "aaaa"]),
        (["zz", "xx", "vv", "uu"], ["xx", "uu", "vv", "zz"]),
    ],
)

def test_empty_list(input_list: List[str], expected_output: List[str]):
    assert sorted_list_sum(input_list) == expected_output