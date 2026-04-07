
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
import math


# Focus: Boundary Values
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
    new_lst = [x for x in lst if len(x) % 2 == 0]
    new_lst.sort(key=lambda x: (len(x), x))
    return new_lst

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_list_with_only_odd_length_strings():
    assert sorted_list_sum(["a", "abc", ""]) == []

def test_list_with_only_even_length_strings():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_list_with_mixed_length_strings():
    assert sorted_list_sum(["a", "aa", "aaa", "aaaa"]) == ["aa", "aaaa"]

def test_list_with_duplicate_even_length_strings():
    assert sorted_list_sum(["aa", "aa", "bb"]) == ["aa", "aa", "bb"]

def test_list_with_same_length_strings_different_alphabetical_order():
    assert sorted_list_sum(["cb", "ab"]) == ["ab", "cb"]

# Focus: Equivalence Partitioning
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

@pytest.mark.parametrize("lst, expected", [
    (["aa", "a", "aaa"], ["aa"]),
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
    (["abc", "def", "ghi"], []),
    (["abcd", "efgh", "ijkl"], ["abcd", "efgh", "ijkl"]),
    (["bb", "aa", "dd", "cc"], ["aa", "bb", "cc", "dd"]),
    (["", "a", "aa"], ["aa"]),
    ([], []),
    (["aaaa", "bbbb", "cccc"], ["aaaa", "bbbb", "cccc"]),
    (["aaaa", "bbbb", "cccc", "aa"], ["aa", "aaaa", "bbbb", "cccc"])
])
def test_equivalence_partitioning(lst, expected):
    assert sorted_list_sum(lst) == expected

# Focus: Logic Branches
import pytest

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "bb", "ccc"]) == []

def test_mixed_lengths():
    assert sorted_list_sum(["aa", "a", "aaa", "cd"]) == ["aa", "cd"]

def test_same_length_alphabetical():
    assert sorted_list_sum(["ab", "aa", "ac"]) == ["aa", "ab", "ac"]

def test_duplicates():
    assert sorted_list_sum(["aa", "aa", "a", "aaa"]) == ["aa", "aa"]

def test_even_lengths_only():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]