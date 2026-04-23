
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

def test_sorted_list_sum_examples():
    """Tests the examples provided in the docstring."""
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_filtering():
    """Tests that strings with odd lengths are correctly removed."""
    # 'a' (1), 'abc' (3), 'abcde' (5) are odd. 'bb' (2), 'dddd' (4) are even.
    assert sorted_list_sum(["a", "bb", "abc", "dddd", "abcde"]) == ["bb", "dddd"]

def test_sorted_list_sum_sorting_logic():
    """Tests the primary sort (length) and secondary sort (alphabetical)."""
    # Even lengths: 'zz' (2), 'aa' (2), 'bbbb' (4), 'cccc' (4), 'ab' (2)
    # Sorted by length: (aa, ab, zz), (bbbb, cccc)
    input_list = ["zz", "aa", "bbbb", "cccc", "ab"]
    expected = ["aa", "ab", "zz", "bbbb", "cccc"]
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_alphabetical_only():
    """Tests alphabetical sorting when all even-length strings have the same length."""
    input_list = ["ca", "ba", "ab", "ac"]
    expected = ["ab", "ac", "ba", "ca"]
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_empty():
    """Tests behavior with an empty list."""
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd():
    """Tests behavior when all strings in the list have odd lengths."""
    assert sorted_list_sum(["a", "ccc", "aaaaa"]) == []

def test_sorted_list_sum_duplicates():
    """Tests that duplicates are preserved and sorted correctly."""
    # 'aa' (2), 'bb' (2), 'aa' (2)
    assert sorted_list_sum(["aa", "bb", "aa"]) == ["aa", "aa", "bb"]

def test_sorted_list_sum_complex_mix():
    """A complex mix of various lengths and alphabetical orders."""
    # Even lengths: 'bb' (2), 'aaaa' (4), 'cc' (2), 'dddddd' (6), 'aa' (2)
    # 1. Filter: bb, aaaa, cc, dddddd, aa
    # 2. Sort by length: (aa, bb, cc), (aaaa), (dddddd)
    # 3. Sort alphabetically: aa, bb, cc, aaaa, dddddd
    input_list = ["aaaa", "bb", "cc", "dddddd", "aa", "a", "abc"]
    expected = ["aa", "bb", "cc", "aaaa", "dddddd"]
    assert sorted_list_sum(input_list) == expected