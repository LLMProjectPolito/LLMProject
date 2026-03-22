import pytest

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
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings

# STEP 2: PLAN
# Test functions:
# - test_empty_list: Test with an empty list.
# - test_all_odd_lengths: Test with a list containing only strings of odd lengths.
# - test_all_even_lengths: Test with a list containing only strings of even lengths.
# - test_mixed_lengths: Test with a list containing both odd and even length strings.
# - test_duplicate_strings: Test with a list containing duplicate strings.
# - test_same_length_strings: Test with strings of the same length, ensuring alphabetical sorting.
# - test_mixed_lengths_duplicates: Test with mixed lengths and duplicate strings.
# - test_single_even_length_string: Test with a list containing only one even length string.
# - test_single_odd_length_string: Test with a list containing only one odd length string.

# STEP 3: CODE
def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "abc", "xyz"]) == []

def test_all_even_lengths():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_lengths():
    assert sorted_list_sum(["a", "aa", "aaa", "bb"]) == ["aa", "bb"]

def test_duplicate_strings():
    assert sorted_list_sum(["aa", "aa", "bb", "cc"]) == ["aa", "aa", "bb", "cc"]

def test_same_length_strings():
    assert sorted_list_sum(["bc", "ab", "cd"]) == ["ab", "bc", "cd"]

def test_mixed_lengths_duplicates():
    assert sorted_list_sum(["a", "aa", "bb", "aaa", "aa"]) == ["aa", "aa", "bb"]

def test_single_even_length_string():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_odd_length_string():
    assert sorted_list_sum(["a"]) == []

def test_example_1():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_example_2():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]