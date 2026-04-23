
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

def filter_and_sort_even_strings(lst):
    """
    Filters out strings with odd lengths and returns the remaining strings
    sorted by length (primary) and alphabetically (secondary).
    """
    # Filter out strings with odd lengths
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    
    # Sort by length (primary) and then alphabetically (secondary)
    return sorted(even_length_strings, key=lambda x: (len(x), x))

@pytest.mark.parametrize("input_list, expected", [
    # Provided examples
    (["aa", "a", "aaa"], ["aa"]),
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
    
    # Edge Case: Empty list
    ([], []),
    
    # Edge Case: All odd lengths (should return empty list)
    (["a", "abc", "abcde", "z"], []),
    
    # Edge Case: All even lengths (should sort by length then alpha)
    (["zz", "aa", "bb"], ["aa", "bb", "zz"]),
    (["cccc", "aa", "bb", "aaaa"], ["aa", "bb", "aaaa", "cccc"]),
    
    # Edge Case: Duplicates
    (["aa", "bb", "aa", "a", "cc"], ["aa", "aa", "bb", "cc"]),
    
    # Edge Case: Empty strings (length 0 is even)
    (["", "a", "bb", "ccc", ""], ["", "", "bb"]),
    
    # Edge Case: Mixed lengths with alphabetical tie-breaking
    (["ba", "ab", "cd", "ac", "a", "abc"], ["ab", "ac", "ba", "cd"]),
    
    # Edge Case: Single element (even)
    (["aa"], ["aa"]),
    
    # Edge Case: Single element (odd)
    (["a"], []),
    
    # Edge Case: Strings with special characters/numbers
    (["12", "1", "123", "!!", "!"], ["!!", "12"]),

    # Edge Case: Case Sensitivity (ASCII/Unicode: Uppercase comes before lowercase)
    (["ab", "Ab"], ["Ab", "ab"]),
    (["ba", "Ab", "aa"], ["aa", "Ab", "ba"]),
])
def test_filter_and_sort_even_strings(input_list, expected):
    """
    Tests the filter_and_sort_even_strings function with various scenarios including
    provided examples, edge cases, and complex sorting requirements.
    """
    assert filter_and_sort_even_strings(input_list) == expected

def test_type_safety():
    """
    Verify that the function raises a TypeError when elements are incompatible.
    This can occur if elements do not support len() or if they are incomparable
    during the sorting phase (e.g., comparing a list to a string).
    """
    # Case 1: Elements that fail len()
    with pytest.raises(TypeError):
        filter_and_sort_even_strings([12, "aa"])
    with pytest.raises(TypeError):
        filter_and_sort_even_strings([None, "aa"])
        
    # Case 2: Elements that have len() but are incomparable during sorting
    with pytest.raises(TypeError):
        filter_and_sort_even_strings([[1, 2], "aa"])

def test_invalid_input_type():
    """
    Verify that the function raises a TypeError when the input 'lst' 
    itself is not an iterable.
    """
    with pytest.raises(TypeError):
        filter_and_sort_even_strings(None)
    with pytest.raises(TypeError):
        filter_and_sort_even_strings(123)

def test_input_immutability():
    """
    Ensure the original list passed to the function is not mutated.
    """
    original = ["ab", "a", "cd"]
    original_copy = original[:]
    filter_and_sort_even_strings(original)
    assert original == original_copy