import pytest
import math


# Focus: Boundary Values
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
    new_lst = [s for s in lst if len(s) % 2 == 0]
    new_lst.sort(key=lambda s: (len(s), s))
    return new_lst

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function filters strings based on even length and sorts the result.
# Boundary values focus on empty lists, lists with only odd length strings,
# lists with only even length strings, and lists with strings of minimal/maximal lengths.

# STEP 2: PLAN - List test functions names and scenarios.
# test_empty_list: Test with an empty input list.
# test_odd_length_only: Test with a list containing only strings of odd lengths.
# test_even_length_only: Test with a list containing only strings of even lengths.
# test_minimal_length: Test with strings of length 0 or 2.
# test_maximal_length: Test with strings of a larger even length.

# STEP 3: CODE - Write the high-quality pytest suite.
def test_empty_list():
    assert sorted_list_sum([]) == []

def test_odd_length_only():
    assert sorted_list_sum(["a", "abc", ""]) == []

def test_even_length_only():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_minimal_length():
    assert sorted_list_sum(["", "aa", "bb"]) == ["", "aa", "bb"]

def test_maximal_length():
    assert sorted_list_sum(["abcdef", "ghijkl", "mnopqr"]) == ["abcdef", "ghijkl", "mnopqr"]

# Focus: Equivalence Partitioning
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

# STEP 1: REASONING - Analyze functional goals and constraints.
# The function filters strings based on even length and sorts them by length then alphabetically.
# Equivalence partitioning focuses on identifying groups of inputs that should be treated the same.
# Key equivalence classes:
# 1. List with only even length strings.
# 2. List with only odd length strings.
# 3. List with a mix of even and odd length strings.
# 4. Empty list.
# 5. List with duplicate even length strings.
# 6. List with strings of the same length (to test alphabetical sorting).

# STEP 2: PLAN - List test functions names and scenarios.
# test_even_length_strings: Tests a list containing only even length strings.
# test_odd_length_strings: Tests a list containing only odd length strings (should return empty list).
# test_mixed_length_strings: Tests a list with both even and odd length strings.
# test_empty_list: Tests an empty list.
# test_duplicate_even_length_strings: Tests a list with duplicate even length strings.
# test_same_length_strings: Tests strings of the same even length to verify alphabetical sorting.

# STEP 3: CODE - Write the high-quality pytest suite.

def test_even_length_strings():
    assert sorted_list_sum(["aa", "bb", "cc", "dd"]) == ["aa", "bb", "cc", "dd"]
    assert sorted_list_sum(["abcd", "efgh", "ijkl"]) == ["abcd", "efgh", "ijkl"]
    assert sorted_list_sum(["zz", "aa", "bb"]) == ["aa", "bb", "zz"]

def test_odd_length_strings():
    assert sorted_list_sum(["a", "abc", "def"]) == []
    assert sorted_list_sum(["x"]) == []

def test_mixed_length_strings():
    assert sorted_list_sum(["aa", "a", "aaa", "cd"]) == ["aa", "cd"]
    assert sorted_list_sum(["ab", "a", "abc", "cd", "c"]) == ["ab", "cd"]
    assert sorted_list_sum(["abc", "abcd", "a", "ab"]) == ["ab", "abcd"]

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_duplicate_even_length_strings():
    assert sorted_list_sum(["aa", "aa", "bb", "cc"]) == ["aa", "aa", "bb", "cc"]

def test_same_length_strings():
    assert sorted_list_sum(["ab", "ac", "aa"]) == ["aa", "ab", "ac"]
    assert sorted_list_sum(["zz", "xy", "ab"]) == ["ab", "xy", "zz"]

# Focus: Logic Branches
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
    new_lst = [s for s in lst if len(s) % 2 == 0]
    new_lst.sort(key=lambda s: (len(s), s))
    return new_lst

def test_even_length_strings():
    """Test case with only even length strings."""
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_length_strings():
    """Test case with a mix of even and odd length strings."""
    assert sorted_list_sum(["aa", "a", "aaa", "bb"]) == ["aa", "bb"]

def test_duplicate_even_length_strings():
    """Test case with duplicate even length strings."""
    assert sorted_list_sum(["aa", "aa", "bb"]) == ["aa", "aa", "bb"]

def test_empty_list():
    """Test case with an empty list."""
    assert sorted_list_sum([]) == []

def test_all_odd_length_strings():
    """Test case with all odd length strings."""
    assert sorted_list_sum(["a", "aaa", "ccccc"]) == []

def test_same_length_strings_alphabetical():
    """Test case with strings of the same length, checking alphabetical order."""
    assert sorted_list_sum(["cb", "ab"]) == ["ab", "cb"]

def test_mixed_lengths_and_duplicates():
    """Test case with mixed lengths, duplicates, and alphabetical sorting."""
    assert sorted_list_sum(["ab", "a", "aa", "bb", "aaa", "cc", "aa"]) == ["aa", "aa", "ab", "bb", "cc"]