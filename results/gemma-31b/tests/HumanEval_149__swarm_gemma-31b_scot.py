
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
import math

def test_sorted_list_sum_complex_sorting_and_filtering():
    # Test case:
    # "a" (1), "ccc" (3) -> Odd, should be removed
    # "zz", "aa", "bb" (2) -> Even, should be sorted alphabetically: "aa", "bb", "zz"
    # "dddd" (4) -> Even, comes after length 2
    # "banana" (6) -> Even, comes after length 4
    # "aa" (2) -> Duplicate, should be preserved and sorted
    input_list = ["zz", "a", "aa", "ccc", "bb", "dddd", "banana", "aa"]
    expected_output = ["aa", "aa", "bb", "zz", "dddd", "banana"]
    assert sorted_list_sum(input_list) == expected_output

def test_sorted_list_sum_empty_and_duplicates():
    """
    Tests the function with:
    - Empty strings (length 0 is even)
    - Duplicate strings
    - Mixed even lengths (to test primary length sort)
    - Same even lengths (to test secondary alphabetical sort)
    - Odd length strings (to ensure they are removed)
    """
    input_list = ["banana", "apple", "pear", "kiwi", "", "cherry", "date", "", "apple", "a"]
    # Filtering odd lengths:
    # "banana" (6), "pear" (4), "kiwi" (4), "" (0), "cherry" (6), "date" (4), "" (0)
    # Sorted by length:
    # 0: "", ""
    # 4: "date", "kiwi", "pear" (alphabetical)
    # 6: "banana", "cherry" (alphabetical)
    expected = ["", "", "date", "kiwi", "pear", "banana", "cherry"]
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_case_sensitivity():
    """
    Test with a mix of:
    - Empty string (even length 0)
    - Odd length strings (should be removed)
    - Even length strings with different cases (to check alphabetical order)
    - Multiple different even lengths (to check length sort)
    """
    input_list = ["Banana", "apple", "Kiwi", "date", "Pear", "pear", "cherry", "", "a"]
    # Filtering odd lengths:
    # "Banana" (6) - Keep
    # "apple" (5) - Remove
    # "Kiwi" (4) - Keep
    # "date" (4) - Keep
    # "Pear" (4) - Keep
    # "pear" (4) - Keep
    # "cherry" (6) - Keep
    # "" (0) - Keep
    # "a" (1) - Remove
    
    # Remaining: ["Banana", "Kiwi", "date", "Pear", "pear", "cherry", ""]
    # Sort by length (primary) and alphabet (secondary):
    # Length 0: ""
    # Length 4: "Kiwi", "Pear", "date", "pear" (Alphabetical: K < P < d < p)
    # Length 6: "Banana", "cherry" (Alphabetical: B < c)
    
    expected = ["", "Kiwi", "Pear", "date", "pear", "Banana", "cherry"]
    assert sorted_list_sum(input_list) == expected