
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
    Filters out strings with odd lengths and returns a new list 
    sorted primarily by length (ascending) and secondarily alphabetically.
    """
    # Filter out odd-length strings
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    
    # Sort by length (primary) and then alphabetically (secondary)
    return sorted(even_length_strings, key=lambda x: (len(x), x))

@pytest.mark.parametrize("input_list, expected_output", [
    # --- Provided Examples ---
    (["aa", "a", "aaa"], ["aa"]),
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
    
    # --- Edge Cases: Empty and Single Element ---
    ([], []),
    (["aa"], ["aa"]),
    (["a"], []),
    
    # --- Edge Cases: All Odd or All Even ---
    (["a", "abc", "abcde", "a"], []),
    (["dc", "ba", "ca", "bb"], ["ba", "bb", "ca", "dc"]),
    
    # --- Sorting Logic: Length Priority and Alphabetical Tie-breaking ---
    (["aaaa", "bb", "cccc", "dd"], ["bb", "aaaa", "cccc", "dd"]),
    (["zz", "aa", "aaaa", "bb"], ["aa", "bb", "aaaa", "zz"]),
    (["banana", "aaaa", "ab", "ba", "abcd", "zz"], ["ab", "ba", "zz", "aaaa", "abcd", "banana"]),
    (["apple", "pear", "kiwi", "banana", "fig", "ace"], ["kiwi", "pear", "banana"]),
    
    # --- Duplicates ---
    (["aa", "bb", "aa", "a", "cc"], ["aa", "aa", "bb", "cc"]),
    (["a", "a", "aaa", "bb", "bb"], ["bb", "bb"]),
    (["aa", "ab", "aa", "a", "zz", "zz"], ["aa", "aa", "ab", "zz", "zz"]),
    
    # --- Complexity and Variety ---
    (["abcdef", "ab", "abcd", "a", "abc", "abcde", "z", "ba"], ["ab", "ba", "abcd", "abcdef"]),
    
    # --- Case Sensitivity (Standard ASCII/Unicode: 'A' < 'a') ---
    (["bB", "Aa", "aa", "BB"], ["Aa", "BB", "aa", "bB"]),
    
    # --- Non-alphabetic characters (Numbers and Symbols) ---
    (["12", "1", "!!", "!!!"], ["!!", "12"]),
])
def test_sorted_list_sum_variations(input_list, expected_output):
    """Tests various scenarios including provided examples, edge cases, and sorting logic."""
    assert sorted_list_sum(input_list) == expected_output

def test_sorted_list_sum_immutability():
    """Ensure the function does not mutate the original input list."""
    original = ["ab", "a", "aaa", "cd"]
    input_copy = list(original)
    sorted_list_sum(input_copy)
    assert input_copy == original