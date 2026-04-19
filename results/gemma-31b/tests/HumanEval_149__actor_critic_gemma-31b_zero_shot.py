
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

def sorted_list_sum(lst):
    """
    Filters out strings with odd lengths and sorts the remaining strings 
    first by length (ascending) and then alphabetically.
    """
    # Filter out strings with odd lengths
    filtered = [s for s in lst if len(s) % 2 == 0]
    
    # Sort by length (primary) and alphabetically (secondary)
    return sorted(filtered, key=lambda x: (len(x), x))

# --- Pytest Suite ---

def test_provided_example_1():
    """Test the first example provided in the docstring."""
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_provided_example_2():
    """Test the second example provided in the docstring."""
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_empty_list():
    """Test that an empty list returns an empty list."""
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    """Test that a list containing only odd-length strings returns an empty list."""
    assert sorted_list_sum(["a", "abc", "abcde", "123"]) == []

def test_all_even_lengths_same_size():
    """Test alphabetical sorting when all strings have the same even length."""
    assert sorted_list_sum(["dc", "ba", "ca", "ab"]) == ["ab", "ba", "ca", "dc"]

def test_even_lengths_different_sizes():
    """Test sorting by length first, then alphabetically."""
    input_list = ["dddd", "aa", "cccc", "bb"]
    expected = ["aa", "bb", "cccc", "dddd"]
    assert sorted_list_sum(input_list) == expected

def test_mixed_lengths():
    """Test a mix of odd and even lengths with various sorting requirements."""
    input_list = ["apple", "pear", "banana", "kiwi", "plum", "orange"]
    # Evens: pear(4), kiwi(4), plum(4), banana(6), orange(6)
    expected = ["kiwi", "pear", "plum", "banana", "orange"]
    assert sorted_list_sum(input_list) == expected

def test_duplicates():
    """Test that duplicates are preserved and sorted correctly."""
    assert sorted_list_sum(["aa", "bb", "aa", "bb"]) == ["aa", "aa", "bb", "bb"]

def test_case_sensitivity():
    """Test that alphabetical sorting respects ASCII/Unicode order (Uppercase before Lowercase)."""
    assert sorted_list_sum(["aa", "Aa"]) == ["Aa", "aa"]

def test_numeric_strings():
    """Test that strings containing numbers are handled as strings."""
    assert sorted_list_sum(["12", "1", "123", "10"]) == ["10", "12"]

def test_empty_strings():
    """Test that empty strings (length 0) are treated as even and sorted to the front."""
    # "" (0), "aa" (2), "" (0), "a" (1)
    assert sorted_list_sum(["", "aa", "", "a"]) == ["", "", "aa"]

def test_non_string_inputs():
    """Test that non-string inputs raise a TypeError during len() or sorting."""
    with pytest.raises(TypeError):
        sorted_list_sum([None])
    with pytest.raises(TypeError):
        sorted_list_sum([123, 456])