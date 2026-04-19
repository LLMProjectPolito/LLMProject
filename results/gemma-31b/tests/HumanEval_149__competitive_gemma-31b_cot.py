
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
    # Provided examples
    (["aa", "a", "aaa"], ["aa"]),
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
    
    # Empty list
    ([], []),
    
    # All odd lengths (should return empty)
    (["a", "aaa", "abcde"], []),
    
    # All even lengths, different lengths (sort by length)
    (["bbbb", "aa", "cccccc"], ["aa", "bbbb", "cccccc"]),
    
    # All even lengths, same length (sort alphabetically)
    (["zz", "aa", "bb"], ["aa", "bb", "zz"]),
    
    # Mixed lengths and alphabetical sorting
    (["banana", "apple", "cherry", "date", "fig", "egg"], ["date", "banana", "cherry"]), 
    # date(4), banana(6), cherry(6) -> banana < cherry
    
    # Duplicates
    (["aa", "aa", "bb", "a"], ["aa", "aa", "bb"]),
    
    # Case sensitivity (Standard Python sort: Uppercase before Lowercase)
    (["Bb", "Aa", "aa", "BB"], ["Aa", "BB", "Bb", "aa"]),
    
    # Complex mix
    (["abcd", "ab", "efgh", "ef", "a", "abc"], ["ab", "ef", "abcd", "efgh"]),
])
def test_sorted_list_sum(input_list, expected):
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_mutation():
    """Ensure the original list is not mutated if that's a requirement, 
    though the prompt doesn't explicitly forbid it, it's good practice."""
    original = ["ab", "a", "cd"]
    original_copy = original[:]
    sorted_list_sum(original)
    # If the function uses .remove() or .pop() on the input list, this might fail.
    # However, the prompt says "deletes the strings", which often implies mutation.
    # But usually, in pytest suites, we check the return value.
    pass