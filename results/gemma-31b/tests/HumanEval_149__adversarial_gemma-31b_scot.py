
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

# The function is provided in the environment; we are testing 'sorted_list_sum'

def test_empty_list():
    """Should return an empty list when input is empty."""
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    """Should return an empty list when all strings have odd lengths."""
    assert sorted_list_sum(["a", "aaa", "abcde", "123"]) == []

def test_all_even_lengths_same_size():
    """Should sort alphabetically when all strings have the same even length."""
    # All length 2: 'ba', 'ab', 'ac' -> sorted: 'ab', 'ac', 'ba'
    assert sorted_list_sum(["ba", "ab", "ac"]) == ["ab", "ac", "ba"]

def test_mixed_lengths_filtering():
    """Should remove odd lengths and keep even lengths."""
    # "a"(1), "bb"(2), "ccc"(3), "dddd"(4) -> ["bb", "dddd"]
    assert sorted_list_sum(["a", "bb", "ccc", "dddd"]) == ["bb", "dddd"]

def test_sorting_priority():
    """Should sort by length first, then alphabetically."""
    # "zebra"(5-odd), "apple"(5-odd), "cat"(3-odd), "dog"(3-odd) -> []
    # "be"(2), "at"(2), "boat"(4), "bear"(4)
    # Length 2: "at", "be"
    # Length 4: "bear", "boat"
    input_list = ["boat", "be", "bear", "at"]
    expected = ["at", "be", "bear", "boat"]
    assert sorted_list_sum(input_list) == expected

def test_duplicates():
    """Should handle duplicate strings correctly."""
    # "aa"(2), "aa"(2), "bb"(2) -> ["aa", "aa", "bb"]
    assert sorted_list_sum(["bb", "aa", "aa"]) == ["aa", "aa", "bb"]

def test_case_sensitivity():
    """Should follow standard Python lexicographical sorting (Uppercase before Lowercase)."""
    # "B"(1-odd), "A"(1-odd), "bb"(2), "AA"(2)
    # Length 2: "AA", "bb"
    assert sorted_list_sum(["bb", "AA"]) == ["AA", "bb"]

def test_provided_examples():
    """Verify the examples provided in the docstring."""
    # Example 1: ["aa", "a", "aaa"] -> "a"(1), "aaa"(3) removed -> ["aa"]
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    # Example 2: ["ab", "a", "aaa", "cd"] -> "a"(1), "aaa"(3) removed -> ["ab", "cd"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

@pytest.mark.parametrize("input_lst, expected", [
    (["banana", "apple", "cherry", "date"], ["date", "banana", "cherry"]), 
    # banana(6), apple(5-X), cherry(6), date(4)
    # Sorted by length: date(4), [banana(6), cherry(6)]
    # Sorted alphabetically: date, banana, cherry
    (["", "a", "bb", "ccc", "dddd"], ["", "bb", "dddd"]),
    # "" is length 0 (even), "a" is 1 (odd), "bb" is 2 (even), etc.
])
def test_parametrized_cases(input_lst, expected):
    """Additional complex scenarios."""
    assert sorted_list_sum(input_lst) == expected