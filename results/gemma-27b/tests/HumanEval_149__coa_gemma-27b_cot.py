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
    new_lst = [s for s in lst if len(s) % 2 == 0]
    new_lst.sort(key=lambda s: (len(s), s))
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
    new_lst = [s for s in lst if len(s) % 2 == 0]
    new_lst.sort(key=lambda s: (len(s), s))
    return new_lst

def test_equivalence_partitioning_even_lengths():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_equivalence_partitioning_mixed_lengths():
    assert sorted_list_sum(["a", "aa", "aaa", "aaaa"]) == ["aa", "aaaa"]

def test_equivalence_partitioning_empty_list():
    assert sorted_list_sum([]) == []

def test_equivalence_partitioning_all_odd_lengths():
    assert sorted_list_sum(["a", "aaa", "ccccc"]) == []

def test_equivalence_partitioning_duplicate_even_lengths():
    assert sorted_list_sum(["aa", "aa", "bb"]) == ["aa", "aa", "bb"]

def test_equivalence_partitioning_same_length_alphabetical():
    assert sorted_list_sum(["ab", "cd", "aa"]) == ["aa", "ab", "cd"]

# Focus: Logic Branches
import pytest

def test_sorted_list_sum_empty_list():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd_lengths():
    assert sorted_list_sum(["a", "abc", "e"]) == []

def test_sorted_list_sum_mixed_lengths():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_sorted_list_sum_mixed_lengths_duplicates():
    assert sorted_list_sum(["ab", "a", "aaa", "cd", "ab"]) == ["ab", "ab", "cd"]

def test_sorted_list_sum_same_length_alphabetical():
    assert sorted_list_sum(["bc", "ab", "cd"]) == ["bc", "cd"]

def test_sorted_list_sum_even_lengths_only():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]