
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

def test_sorted_list_sum_provided_examples():
    """Tests the examples explicitly provided in the docstring."""
    # Example 1: ["aa", "a", "aaa"] -> "a" (1) and "aaa" (3) are odd, removed.
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    # Example 2: ["ab", "a", "aaa", "cd"] -> "a" (1) and "aaa" (3) are odd, removed. 
    # "ab" and "cd" are length 2, sorted alphabetically.
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_filtering():
    """Tests that all odd-length strings are strictly removed."""
    assert sorted_list_sum(["a", "abc", "abcde"]) == []
    assert sorted_list_sum(["aa", "bbbb", "cccccc"]) == ["aa", "bbbb", "cccccc"]
    assert sorted_list_sum(["apple", "pear", "banana", "kiwi"]) == ["pear", "kiwi", "banana"] # pear(4), kiwi(4), banana(6)

def test_sorted_list_sum_length_sorting():
    """Tests that the primary sort key is the length of the string (ascending)."""
    # All even, but different lengths
    input_list = ["abcdef", "ab", "abcd"]
    expected = ["ab", "abcd", "abcdef"]
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_alphabetical_sorting():
    """Tests that the secondary sort key is alphabetical when lengths are equal."""
    # All length 2, should be sorted alphabetically
    input_list = ["zz", "aa", "mm", "bb"]
    expected = ["aa", "bb", "mm", "zz"]
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_combined_sorting():
    """Tests the combination of length sorting and alphabetical tie-breaking."""
    input_list = ["zebra", "apple", "dog", "cat", "bear", "ant", "banana"]
    # Even lengths: "bear"(4), "banana"(6)
    # Wait, let's use a better set:
    # "aa" (2), "bb" (2), "cccc" (4), "dddd" (4)
    input_list = ["dddd", "bb", "cccc", "aa"]
    expected = ["aa", "bb", "cccc", "dddd"]
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_empty_and_null_cases():
    """Tests edge cases like empty lists."""
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_duplicates():
    """Tests that duplicates are preserved and sorted correctly."""
    input_list = ["aa", "aa", "bb", "bb"]
    assert sorted_list_sum(input_list) == ["aa", "aa", "bb", "bb"]

def test_sorted_list_sum_case_sensitivity():
    """
    Tests how the function handles casing. 
    Standard Python sort is case-sensitive (ASCII), where 'A' < 'a'.
    """
    input_list = ["Bb", "Aa"]
    # If the function uses standard sorted(), "Aa" comes before "Bb"
    assert sorted_list_sum(input_list) == ["Aa", "Bb"]

def test_sorted_list_sum_special_characters():
    """Tests strings with spaces or symbols (which still have lengths)."""
    # "  " is length 2 (even), "   " is length 3 (odd)
    input_list = ["  ", "   ", "!!", "!"]
    # Even: "  " (length 2), "!!" (length 2). 
    # ASCII: " " (32) comes before "!" (33)
    assert sorted_list_sum(input_list) == ["  ", "!!"]