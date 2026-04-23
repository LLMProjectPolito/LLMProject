
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
    """Test that an empty list returns an empty list."""
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    """Test that a list containing only odd-length strings returns an empty list."""
    assert sorted_list_sum(["a", "abc", "abcde", "123"]) == []

def test_all_even_lengths():
    """Test that a list of even-length strings is sorted alphabetically."""
    # All length 2, should sort alphabetically
    assert sorted_list_sum(["cc", "aa", "bb", "dd"]) == ["aa", "bb", "cc", "dd"]

def test_provided_examples():
    """Test the specific examples provided in the problem description."""
    # Example 1: ["aa", "a", "aaa"] -> ["aa"]
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    # Example 2: ["ab", "a", "aaa", "cd"] -> ["ab", "cd"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_complex_sorting():
    """
    Test the primary sort (length) and secondary sort (alphabetical).
    Input: ["aaaa", "bb", "cc", "a", "ddd", "aa"]
    1. Filter odds: ["aaaa", "bb", "cc", "aa"]
    2. Sort by length: ["bb", "cc", "aa", "aaaa"] (Wait, length 2 comes first)
    3. Sort by length then alpha: 
       Length 2: "aa", "bb", "cc"
       Length 4: "aaaa"
    Result: ["aa", "bb", "cc", "aaaa"]
    """
    input_list = ["aaaa", "bb", "cc", "a", "ddd", "aa"]
    expected = ["aa", "bb", "cc", "aaaa"]
    assert sorted_list_sum(input_list) == expected

def test_duplicates():
    """Test that duplicate even-length strings are preserved and sorted."""
    assert sorted_list_sum(["bb", "aa", "bb", "aa"]) == ["aa", "aa", "bb", "bb"]

def test_case_sensitivity():
    """
    Test alphabetical sorting with mixed casing.
    In Python, 'A' < 'Z' < 'a' < 'z'.
    """
    # All length 2
    assert sorted_list_sum(["ba", "Aa", "aa", "BB"]) == ["Aa", "BB", "aa", "ba"]

@pytest.mark.parametrize("input_data, expected_output", [
    (["z", "y", "x"], []),
    (["zz", "aa", "bb"], ["aa", "bb", "zz"]),
    (["abcd", "ab", "abc", "a"], ["ab", "abcd"]),
    (["apple", "pear", "kiwi", "banana"], ["kiwi", "pear"]), # pear(4), kiwi(4) -> kiwi, pear
])
def test_parameterized_scenarios(input_data, expected_output):
    """Run multiple scenarios through a single test function."""
    assert sorted_list_sum(input_data) == expected_output