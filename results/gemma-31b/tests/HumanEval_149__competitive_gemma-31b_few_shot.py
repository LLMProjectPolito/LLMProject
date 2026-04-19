
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
    # Basic cases from docstring
    (["aa", "a", "aaa"], ["aa"]),
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
    # Empty list
    ([], []),
    # All odd lengths
    (["a", "aaa", "aaaaa"], []),
    # All even lengths, already sorted by length and alpha
    (["ab", "abcd", "abcdef"], ["ab", "abcd", "abcdef"]),
    # All even lengths, unsorted
    (["abcdef", "abcd", "ab"], ["ab", "abcd", "abcdef"]),
    # Same length, alphabetical sort
    (["cc", "aa", "bb"], ["aa", "bb", "cc"]),
    # Mixed lengths, mixed parity
    (["apple", "banana", "cherry", "date", "egg"], ["date", "banana", "cherry"]),
    # Duplicates
    (["aa", "aa", "bb", "bb", "a"], ["aa", "aa", "bb", "bb"]),
    # Mixed case (Python default sort is case-sensitive: Uppercase before Lowercase)
    (["Bb", "Aa", "aa", "BB"], ["Aa", "BB", "aa", "Bb"]),
    # Strings with spaces or special characters (even length)
    (["a b", "ab", "c d", "cd"], ["ab", "cd", "a b", "c d"]),
])
def test_sorted_list_sum(input_list, expected):
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_mutation():
    """Ensure the original list is not mutated if that's a requirement, 
    though the prompt doesn't explicitly forbid it, it's good practice."""
    original = ["ab", "a", "cd"]
    original_copy = list(original)
    sorted_list_sum(original)
    # If the function uses .remove() or .pop() on the input list, this might fail.
    # The prompt says "deletes the strings", which could imply mutation.
    # However, usually, these functions should return a new list.
    # We check if the result is correct regardless of mutation.
    assert sorted_list_sum(original_copy) == ["ab", "cd"]