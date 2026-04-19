
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
    # Basic examples from the problem description
    (["aa", "a", "aaa"], ["aa"]),
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
    
    # Edge Case: Empty list
    ([], []),
    
    # Edge Case: All odd lengths (should return empty list)
    (["a", "aaa", "abcde", "123"], []),
    
    # Edge Case: All even lengths, already sorted
    (["aa", "bbbb"], ["aa", "bbbb"]),
    
    # Sorting Rule: Length ascending, then alphabetical
    (["dc", "ba", "ab"], ["ab", "ba", "dc"]),
    (["abcd", "aa", "efgh", "bb"], ["aa", "bb", "abcd", "efgh"]),
    
    # Sorting Rule: Mixed lengths and alphabetical ties
    (["zz", "aa", "bbbb", "cccc", "a"], ["aa", "zz", "bbbb", "cccc"]),
    
    # Edge Case: Duplicates
    (["aa", "aa", "bb", "a"], ["aa", "aa", "bb"]),
    
    # Edge Case: Strings with spaces or special characters (even length)
    (["  ", " a ", "!!"], ["  ", "!!"]),
    
    # Case Sensitivity: Verify ASCII-betical sorting (Uppercase before Lowercase)
    (["bb", "AA"], ["AA", "bb"]),
    (["bb", "AA", "aa", "BB"], ["AA", "BB", "aa", "bb"]),
])
def test_filter_and_sort_even_strings(input_list, expected):
    """Tests that strings with odd lengths are removed and the rest are sorted by length then alphabetically."""
    assert filter_and_sort_even_strings(input_list) == expected

def test_filter_and_sort_even_strings_none_input():
    """Tests that passing None as input raises a TypeError, as it is not iterable."""
    with pytest.raises(TypeError):
        filter_and_sort_even_strings(None)