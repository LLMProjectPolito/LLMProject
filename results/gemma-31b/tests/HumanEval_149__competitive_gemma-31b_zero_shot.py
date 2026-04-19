
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

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "aaa", "abcde", "g"]) == []

def test_all_even_lengths_same_size():
    # Testing alphabetical sort for same length
    assert sorted_list_sum(["ba", "ab", "cd", "ac"]) == ["ab", "ac", "ba", "cd"]

def test_all_even_lengths_different_size():
    # Testing length sort
    assert sorted_list_sum(["abcdef", "ab", "abcd", "aa"]) == ["aa", "ab", "abcd", "abcdef"]

def test_mixed_lengths():
    # Should remove "a", "aaa", "b" and keep "aa", "bbbb"
    assert sorted_list_sum(["a", "aa", "aaa", "bbbb", "b"]) == ["aa", "bbbb"]

def test_length_and_alphabetical_combined():
    # Length 2: "aa", "zz" | Length 4: "aaaa", "bbbb"
    input_list = ["zz", "bbbb", "aa", "aaaa"]
    expected = ["aa", "zz", "aaaa", "bbbb"]
    assert sorted_list_sum(input_list) == expected

def test_duplicates():
    # Should preserve duplicates and sort them
    assert sorted_list_sum(["bb", "aa", "bb", "aa"]) == ["aa", "aa", "bb", "bb"]

def test_case_sensitivity():
    # Standard Python string sorting is case-sensitive (ASCII: A-Z before a-z)
    assert sorted_list_sum(["bb", "AA", "aa"]) == ["AA", "aa", "bb"]

def test_docstring_example_1():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_docstring_example_2():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]