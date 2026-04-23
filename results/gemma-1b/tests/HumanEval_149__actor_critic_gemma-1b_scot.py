
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

def list_sort(lst):
    """Sorts a list of strings by length, then alphabetically, and removes strings with odd lengths."""
    filtered_list = [s for s in lst if len(s) % 2 == 0]
    filtered_list.sort(key=lambda x: (len(x), x))
    return filtered_list

def test_empty_list():
    """Test with an empty list."""
    assert list_sort([]) == []

def test_single_element_list():
    """Test with a list containing a single element."""
    assert list_sort(["a"]) == ["a"]

def test_even_length_list():
    """Test with an even-length list."""
    assert list_sort(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_odd_length_list():
    """Test with an odd-length list."""
    assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_list_with_duplicates():
    """Test with a list containing duplicate strings."""
    assert list_sort(["aa", "a", "aaa", "bb"]) == ["aa", "a", "bb"]

def test_list_with_mixed_lengths():
    """Test with a list containing strings of varying lengths."""
    assert list_sort(["aa", "a", "aaa", "cd", "bb"]) == ["aa", "a", "bb", "cd"]

def test_list_with_numbers():
    """Test with a list containing numbers (should not be included)."""
    assert list_sort(["aa", "a", "aaa"]) == ["aa"]

def test_list_with_special_characters():
    """Test with a list containing special characters."""
    assert list_sort(["!@#", "a", "aa"]) == ["!@#", "a"]