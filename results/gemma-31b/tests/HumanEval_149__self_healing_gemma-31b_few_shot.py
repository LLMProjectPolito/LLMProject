
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
    # Filter out strings with odd lengths
    filtered = [s for s in lst if len(s) % 2 == 0]
    # Sort primarily by length (ascending) and secondarily alphabetically (ascending)
    return sorted(filtered, key=lambda x: (len(x), x))

import pytest

def test_basic_filtering():
    """Test that odd length strings are removed."""
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_length_sorting():
    """Test that strings are sorted primarily by length ascending."""
    # "abcd" (4), "ab" (2), "abcdef" (6)
    assert sorted_list_sum(["abcdef", "abcd", "ab"]) == ["ab", "abcd", "abcdef"]

def test_alphabetical_sorting():
    """Test that strings of the same length are sorted alphabetically."""
    # All length 2: "cd", "ab", "zz", "aa" -> "aa", "ab", "cd", "zz"
    assert sorted_list_sum(["cd", "ab", "zz", "aa"]) == ["aa", "ab", "cd", "zz"]

def test_combined_sorting():
    """Test both length and alphabetical sorting together."""
    # Length 2: "zz", "aa" -> "aa", "zz"
    # Length 4: "bcde", "abcd" -> "abcd", "bcde"
    # Odd lengths: "a", "abc" (removed)
    input_list = ["zz", "a", "bcde", "aa", "abc", "abcd"]
    expected = ["aa", "zz", "abcd", "bcde"]
    assert sorted_list_sum(input_list) == expected

def test_empty_list():
    """Test behavior with an empty list."""
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    """Test behavior when all strings have odd lengths."""
    assert sorted_list_sum(["a", "abc", "abcde", "q"]) == []

def test_all_even_lengths():
    """Test behavior when all strings have even lengths."""
    assert sorted_list_sum(["bb", "aa", "dddd", "cccc"]) == ["aa", "bb", "cccc", "dddd"]

def test_duplicates():
    """Test behavior with duplicate strings."""
    assert sorted_list_sum(["aa", "aa", "bb", "bb", "a"]) == ["aa", "aa", "bb", "bb"]

def test_case_sensitivity():
    """Test that alphabetical sorting respects Python's default string comparison (ASCII)."""
    # In ASCII, uppercase comes before lowercase
    assert sorted_list_sum(["bb", "AA"]) == ["AA", "bb"]