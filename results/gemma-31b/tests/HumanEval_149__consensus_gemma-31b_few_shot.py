
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

def test_sorted_list_sum_basic():
    """Test basic filtering of odd lengths and sorting."""
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_length_sorting():
    """Test that strings are sorted primarily by length (ascending)."""
    # Even lengths: 2, 4, 6
    assert sorted_list_sum(["banana", "abcd", "ab"]) == ["ab", "abcd", "banana"]
    # Mix of odd and even
    assert sorted_list_sum(["apple", "pear", "banana", "kiwi"]) == ["kiwi", "pear", "banana"]

def test_sorted_list_sum_alphabetical_sorting():
    """Test that strings of the same length are sorted alphabetically."""
    assert sorted_list_sum(["cd", "ab", "ef"]) == ["ab", "cd", "ef"]
    assert sorted_list_sum(["zz", "aa", "bb"]) == ["aa", "bb", "zz"]
    assert sorted_list_sum(["dcba", "abcd", "bacd"]) == ["abcd", "bacd", "dcba"]

def test_sorted_list_sum_empty_and_none():
    """Test edge cases like empty lists or lists with no even-length strings."""
    assert sorted_list_sum([]) == []
    assert sorted_list_sum(["a", "abc", "abcde"]) == []

def test_sorted_list_sum_duplicates():
    """Test that duplicates are preserved and sorted correctly."""
    assert sorted_list_sum(["aa", "aa", "bb", "bb"]) == ["aa", "aa", "bb", "bb"]
    assert sorted_list_sum(["aa", "a", "aa"]) == ["aa", "aa"]

def test_sorted_list_sum_mixed_case():
    """Test alphabetical sorting with mixed case (ASCII order)."""
    # In Python, uppercase comes before lowercase
    assert sorted_list_sum(["Bb", "Aa", "aa", "AA"]) == ["AA", "Aa", "Bb", "aa"]

def test_sorted_list_sum_complex():
    """Comprehensive test with various lengths and alphabetical requirements."""
    input_list = ["zebra", "apple", "dog", "cat", "bear", "fish", "bird", "elephant", "ox"]
    # Even items: ox(2), bear(4), bird(4), fish(4), elephant(8)
    assert sorted_list_sum(input_list) == ["ox", "bear", "bird", "fish", "elephant"]

@pytest.mark.parametrize("input_lst, expected_output", [
    (["", "a", "bb"], ["", "bb"]), # Empty string has length 0 (even)
    (["abcd", "ef"], ["ef", "abcd"]), # Length sort
    (["zz", "aa"], ["aa", "zz"]), # Alphabetical sort
    (["12", "1"], ["12"]), # Numeric strings
])
def test_sorted_list_sum_parametrized(input_lst, expected_output):
    assert sorted_list_sum(input_lst) == expected_output