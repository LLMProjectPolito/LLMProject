
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

@pytest.mark.parametrize("input_list, expected", [
    # Examples from docstring
    (["aa", "a", "aaa"], ["aa"]),
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
    
    # Empty list
    ([], []),
    
    # All odd lengths
    (["a", "aaa", "abcde"], []),
    
    # All even lengths, already sorted by length and alpha
    (["aa", "bb", "cccc"], ["aa", "bb", "cccc"]),
    
    # All even lengths, needs sorting by length
    (["cccc", "bb", "aa"], ["aa", "bb", "cccc"]),
    
    # Same length, needs alphabetical sorting
    (["zz", "aa", "bb"], ["aa", "bb", "zz"]),
    
    # Mixed lengths, mixed parity
    (["apple", "banana", "cherry", "date", "egg"], ["date", "banana", "cherry"]),
    # Explanation: 
    # apple(5)-odd, banana(6)-even, cherry(6)-even, date(4)-even, egg(3)-odd
    # Evens: banana, cherry, date
    # Sorted by length: date(4), banana(6), cherry(6)
    # Sorted alphabetically for length 6: banana, cherry
    
    # Duplicates
    (["aa", "aa", "bb", "a"], ["aa", "aa", "bb"]),
    
    # Case sensitivity (Standard Python sort: Uppercase before Lowercase)
    (["BB", "aa", "AA"], ["AA", "BB", "aa"]),
    
    # Long strings
    (["abcdef", "abcd", "ab"], ["ab", "abcd", "abcdef"]),
])
def test_sorted_list_sum(input_list, expected):
    assert sorted_list_sum(input_list) == expected