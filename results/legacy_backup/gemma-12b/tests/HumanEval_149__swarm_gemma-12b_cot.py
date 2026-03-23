import pytest
import math

def test_empty_list():
    """Test with an empty list."""
    assert sorted_list_sum([]) == []

def test_list_with_only_odd_length_strings():
    """Test with a list containing only strings with odd lengths."""
    assert sorted_list_sum(["a", "abc", "de"]) == []

def test_list_with_duplicate_strings_of_same_length():
    """Test with duplicate strings of the same length."""
    assert sorted_list_sum(["aa", "aa", "bb", "cc"]) == ["aa", "aa", "bb", "cc"]

def test_list_with_duplicate_strings_of_different_lengths():
    """Test with duplicate strings of different lengths."""
    assert sorted_list_sum(["a", "aa", "a", "aaa", "aa"]) == ["a", "a", "aa", "aa"]

def test_list_with_mixed_lengths_and_duplicates():
    """Test with a list containing strings of mixed lengths and duplicates."""
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "aa", "c", "bbb"]) == ["aa", "aa", "bb", "bbb"]

def test_list_with_same_length_strings_requiring_alphabetical_sort():
    """Test with strings of the same length, requiring alphabetical sorting."""
    assert sorted_list_sum(["cc", "aa", "bb"]) == ["aa", "bb", "cc"]