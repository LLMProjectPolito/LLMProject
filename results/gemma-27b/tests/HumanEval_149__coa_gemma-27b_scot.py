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
# lists with only even length strings, and lists with strings of the same length.

# STEP 2: PLAN - List test functions names and scenarios.
# test_empty_list: Test with an empty input list.
# test_all_odd_lengths: Test with a list containing only strings of odd lengths.
# test_all_even_lengths: Test with a list containing only strings of even lengths.
# test_same_length_strings: Test with strings of the same even length, checking alphabetical order.
# test_mixed_lengths: Test with a mix of odd and even length strings.

# STEP 3: CODE - Write the high-quality pytest suite.
def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "abc", ""]) == []

def test_all_even_lengths():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_same_length_strings():
    assert sorted_list_sum(["ab", "aa", "ac"]) == ["aa", "ab", "ac"]

def test_mixed_lengths():
    assert sorted_list_sum(["a", "aa", "aaa", "bb"]) == ["aa", "bb"]

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
#   - Empty list
#   - List with only odd length strings
#   - List with only even length strings
#   - List with a mix of odd and even length strings
#   - List with duplicate even length strings
#   - List with strings of the same length (to test alphabetical sorting)

# STEP 2: PLAN - List test functions names and scenarios.
# test_empty_list: Tests the function with an empty list.
# test_odd_length_strings: Tests the function with a list containing only odd length strings.
# test_even_length_strings: Tests the function with a list containing only even length strings.
# test_mixed_length_strings: Tests the function with a list containing both odd and even length strings.
# test_duplicate_even_length_strings: Tests the function with duplicate even length strings.
# test_same_length_strings: Tests the function with strings of the same length to verify alphabetical sorting.

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_odd_length_strings():
    assert sorted_list_sum(["a", "abc", "def"]) == []

def test_even_length_strings():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_length_strings():
    assert sorted_list_sum(["aa", "a", "aaa", "cd"]) == ["aa", "cd"]

def test_duplicate_even_length_strings():
    assert sorted_list_sum(["aa", "bb", "aa", "cc"]) == ["aa", "aa", "bb", "cc"]

def test_same_length_strings():
    assert sorted_list_sum(["ab", "ac", "aa"]) == ["aa", "ab", "ac"]

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
    assert sorted_list_sum(["ab", "a", "aa", "cd", "aa"]) == ["aa", "aa", "ab", "cd"]