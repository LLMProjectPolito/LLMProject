# STEP 1: REASONING
# The function `sorted_list_sum` filters a list of strings, keeping only those with even lengths,
# and then sorts the resulting list based on length (ascending) and alphabetically (for ties).
# We need to test various scenarios:
# - Empty list
# - List with only odd-length strings
# - List with only even-length strings
# - List with a mix of odd and even-length strings
# - List with strings of the same length (to test alphabetical sorting)
# - List with duplicate strings
# - List with a single string
# - Edge cases like very long strings

# STEP 2: PLAN
# 1. test_empty_list: Test with an empty list.
# 2. test_odd_length_strings: Test with a list containing only odd-length strings.
# 3. test_even_length_strings: Test with a list containing only even-length strings.
# 4. test_mixed_length_strings: Test with a list containing both odd and even-length strings.
# 5. test_same_length_strings: Test with strings of the same length to verify alphabetical sorting.
# 6. test_duplicate_strings: Test with duplicate strings.
# 7. test_single_string_even: Test with a single even-length string.
# 8. test_single_string_odd: Test with a single odd-length string.
# 9. test_long_strings: Test with very long strings.
# 10. test_mixed_case: Test with mixed case strings.

# STEP 3: CODE
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

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_odd_length_strings():
    assert sorted_list_sum(["a", "abc", "def"]) == []

def test_even_length_strings():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_length_strings():
    assert sorted_list_sum(["aa", "a", "aaa", "cd"]) == ["aa", "cd"]

def test_same_length_strings():
    assert sorted_list_sum(["ab", "aa", "ac"]) == ["aa", "ab", "ac"]

def test_duplicate_strings():
    assert sorted_list_sum(["aa", "aa", "bb"]) == ["aa", "aa", "bb"]

def test_single_string_even():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_string_odd():
    assert sorted_list_sum(["a"]) == []

def test_long_strings():
    assert sorted_list_sum(["aaaaaaaa", "bbbbbbbb", "ccccccccc"]) == ["aaaaaaaa", "bbbbbbbb"]

def test_mixed_case():
    assert sorted_list_sum(["aA", "BB", "cc"]) == ["aA", "BB", "cc"]

def test_mixed_case_and_length():
    assert sorted_list_sum(["aA", "BB", "c", "dd"]) == ["aA", "BB", "dd"]