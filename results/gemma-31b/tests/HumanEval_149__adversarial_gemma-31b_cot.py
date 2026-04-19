
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
    # Basic examples from docstring
    (["aa", "a", "aaa"], ["aa"]),
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
    
    # Edge Case: Empty list
    ([], []),
    
    # Edge Case: All odd lengths (should return empty)
    (["a", "abc", "abcde", "123"], []),
    
    # Edge Case: All even lengths, different lengths (sort by length)
    (["abcd", "ab", "abcdef"], ["ab", "abcd", "abcdef"]),
    
    # Edge Case: Same even length, alphabetical sort
    (["cc", "aa", "bb"], ["aa", "bb", "cc"]),
    
    # Edge Case: Mixed lengths, same length alphabetical
    (["zz", "aa", "bbbb", "cccc", "a"], ["aa", "zz", "bbbb", "cccc"]),
    
    # Edge Case: Duplicates
    (["aa", "aa", "bb", "bb"], ["aa", "aa", "bb", "bb"]),
    
    # Edge Case: Case sensitivity (Standard Python sort: Uppercase < Lowercase)
    (["Bb", "Aa", "aa"], ["Aa", "Bb", "aa"]),
    
    # Edge Case: Strings with spaces or special characters (even length)
    (["a b ", "cd", "e f "], ["cd", "a b ", "e f "]), # "a b " is len 4, "cd" is len 2, "e f " is len 4
    
    # Edge Case: Only one even string among many odd
    (["a", "b", "cc", "d", "e"], ["cc"]),
    
    # Edge Case: Large even lengths
    (["" * 10, "" * 2, "" * 4], ["", "", ""]), # Empty strings are length 0 (even)
    (["a" * 4, "a" * 2, "a" * 6], ["aa", "aaaa", "aaaaaa"]), # Corrected to actual strings
])
def test_sorted_list_sum(input_list, expected):
    """
    Tests the sorted_list_sum function against various scenarios:
    - Filtering of odd-length strings.
    - Sorting by length (ascending).
    - Sorting alphabetically for ties in length.
    - Handling of empty lists and duplicates.
    """
    # Adjusting the "a"*n cases for the parametrize logic
    # Since I wrote "a"*4 in the thought process but the list above had empty strings
    # I will refine the specific test case for large even lengths inside the logic if needed,
    # but the parametrize list is the source of truth.
    
    # Re-evaluating the "a" * n case for the actual test run:
    # If input_list is ["aaaa", "aa", "aaaaaa"], expected is ["aa", "aaaa", "aaaaaa"]
    
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_large_even_strings():
    """Specific test for longer even strings to ensure length sorting works."""
    input_list = ["abcdefgh", "ab", "abcd"]
    expected = ["ab", "abcd", "abcdefgh"]
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_alphabetical_tie():
    """Specific test for alphabetical sorting when lengths are identical."""
    input_list = ["zebra", "apple", "banana", "cherry", "date", "egg"]
    # Even lengths: banana(6), cherry(6), date(4), egg(3-X)
    # Filtered: ["banana", "cherry", "date"]
    # Sorted by length: ["date", "banana", "cherry"]
    # Sorted by alpha for length 6: banana < cherry
    expected = ["date", "banana", "cherry"]
    assert sorted_list_sum(input_list) == expected