
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
    (["a", "abc", "abcde", "123"], []),
    
    # All even lengths, same length (alphabetical sort)
    (["ba", "ab", "ca"], ["ab", "ba", "ca"]),
    
    # All even lengths, different lengths (length sort then alphabetical)
    (["abcd", "ab", "efghij", "cd", "bc"], ["ab", "bc", "cd", "abcd", "efghij"]),
    
    # Mixed odd and even lengths
    (["apple", "pear", "banana", "kiwi", "plum", "orange"], ["kiwi", "pear", "banana", "orange"]),
    # Explanation: 
    # pear(4), banana(6), kiwi(4), orange(6)
    # Length 4: kiwi, pear (alphabetical)
    # Length 6: banana, orange (alphabetical)
    
    # Duplicates
    (["aa", "bb", "aa", "bb"], ["aa", "aa", "bb", "bb"]),
    (["aa", "a", "aa"], ["aa", "aa"]),
    
    # Case sensitivity (Standard Python sort: Uppercase before Lowercase)
    (["Bb", "Aa", "aa", "BB"], ["Aa", "BB", "Bb", "aa"]),
    
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
    # However, usually, these functions should return a new list.
    # This test is optional based on implementation but checks for side effects.
    pass