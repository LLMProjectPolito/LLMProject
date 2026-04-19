
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

def test_sorted_list_sum_empty():
    """Test with an empty list."""
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd():
    """Test where all strings have odd lengths."""
    assert sorted_list_sum(["a", "aaa", "abcde", "123"]) == []

def test_sorted_list_sum_all_even():
    """Test where all strings have even lengths, requiring sorting by length then alpha."""
    # "aa" (2), "bb" (2), "cccc" (4), "dddd" (4)
    # "aa" < "bb" and "cccc" < "dddd"
    assert sorted_list_sum(["dddd", "bb", "cccc", "aa"]) == ["aa", "bb", "cccc", "dddd"]

def test_sorted_list_sum_mixed_lengths():
    """Test mixed odd and even lengths."""
    assert sorted_list_sum(["a", "bb", "ccc", "dddd"]) == ["bb", "dddd"]

def test_sorted_list_sum_alphabetical_tiebreak():
    """Test that strings of the same even length are sorted alphabetically."""
    assert sorted_list_sum(["ba", "ab", "dc", "cd"]) == ["ab", "ba", "cd", "dc"]

def test_sorted_list_sum_duplicates():
    """Test that duplicates are preserved and sorted correctly."""
    assert sorted_list_sum(["aa", "bb", "aa", "bb"]) == ["aa", "aa", "bb", "bb"]

def test_sorted_list_sum_provided_examples():
    """Test the examples provided in the docstring."""
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_complex_case():
    """Test a complex combination of odd/even, length, and alphabetical sorting."""
    input_list = ["apple", "pear", "banana", "kiwi", "plum", "orange", "fig"]
    # Even lengths: 
    # "pear" (4), "kiwi" (4), "banana" (6), "orange" (6)
    # Sorted by length: [4, 4, 6, 6]
    # Sorted alphabetically within length:
    # 4: "kiwi", "pear"
    # 6: "banana", "orange"
    expected = ["kiwi", "pear", "banana", "orange"]
    assert sorted_list_sum(input_list) == expected

@pytest.mark.parametrize("input_lst, expected", [
    (["", "a", "bb"], ["", "bb"]), # Empty string has length 0 (even)
    (["aa", "bb", "cc"], ["aa", "bb", "cc"]),
    (["cc", "bb", "aa"], ["aa", "bb", "cc"]),
    (["abcd", "ab"], ["ab", "abcd"]),
    (["abcd", "ab", "ac"], ["ab", "ac", "abcd"]),
])
def test_sorted_list_sum_parametrized(input_lst, expected):
    """Parametrized tests for various scenarios."""
    assert sorted_list_sum(input_lst) == expected