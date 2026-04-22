
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

# The function is assumed to be defined in the same module or imported.
# For the purpose of this suite, we assume the function name is sorted_list_sum.

def test_empty_list():
    """Tests that an empty list returns an empty list."""
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    """Tests that a list containing only odd-length strings returns an empty list."""
    assert sorted_list_sum(["a", "abc", "abcde", "aaaaa"]) == []

def test_all_even_lengths():
    """Tests that a list containing only even-length strings returns all strings sorted."""
    # Lengths are all 2. Alphabetical sort should apply.
    assert sorted_list_sum(["cc", "aa", "bb"]) == ["aa", "bb", "cc"]

def test_mixed_lengths_filtering():
    """Tests that odd-length strings are removed and even-length strings remain."""
    # "a" (1), "aaa" (3) removed. "ab" (2), "abcd" (4) remain.
    assert sorted_list_sum(["a", "ab", "aaa", "abcd"]) == ["ab", "abcd"]

def test_sorting_priority_length():
    """Tests that the primary sort key is the length of the string."""
    # Even lengths: 2, 4, 6.
    input_list = ["aaaaaa", "bb", "cccc"]
    expected = ["bb", "cccc", "aaaaaa"]
    assert sorted_list_sum(input_list) == expected

def test_sorting_priority_alphabetical():
    """Tests that the secondary sort key is alphabetical order when lengths are equal."""
    # All even lengths (2). Should sort alphabetically.
    input_list = ["dc", "ba", "ca", "ab"]
    expected = ["ab", "ba", "ca", "dc"]
    assert sorted_list_sum(input_list) == expected

def test_combined_sorting_logic():
    """Tests the full requirement: filter odd, sort by length, then alphabetically."""
    # "a" (1) -> remove
    # "zz" (2) -> keep
    # "aa" (2) -> keep
    # "bbbb" (4) -> keep
    # "cccc" (4) -> keep
    # "abc" (3) -> remove
    input_list = ["a", "zz", "aa", "bbbb", "cccc", "abc"]
    # Expected: Length 2 (aa, zz), then Length 4 (bbbb, cccc)
    expected = ["aa", "zz", "bbbb", "cccc"]
    assert sorted_list_sum(input_list) == expected

def test_duplicates():
    """Tests that duplicate strings are handled correctly."""
    # "aa" (2) is duplicate. "a" (1) is odd.
    input_list = ["aa", "a", "bb", "aa"]
    expected = ["aa", "aa", "bb"]
    assert sorted_list_sum(input_list) == expected

def test_case_sensitivity():
    """Tests that alphabetical sorting respects standard ASCII/Unicode order (Case sensitivity)."""
    # "Bb" (2), "aa" (2), "Aa" (2)
    # In ASCII: 'A' < 'B' < 'a'
    input_list = ["bb", "AA", "aa", "BB"]
    expected = ["AA", "BB", "aa", "bb"]
    assert sorted_list_sum(input_list) == expected

@pytest.mark.parametrize("input_val, expected_val", [
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
    (["aa", "a", "aaa"], ["aa"]),
    (["", "a", "ab"], ["ab"]), # Empty string "" has length 0 (even)
    (["12", "1", "123", "22"], ["12", "22"]), # Numeric strings
])
def test_provided_examples_and_edge_cases(input_val, expected_val):
    """Parametrized test to cover specific examples and edge cases like empty strings."""
    assert sorted_list_sum(input_val) == expected_val