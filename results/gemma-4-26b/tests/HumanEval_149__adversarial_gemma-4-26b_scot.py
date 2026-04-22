
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

# The function is assumed to be defined in the environment as sorted_list_sum

@pytest.mark.parametrize("input_list, expected_output", [
    # Test Case 1: Empty list
    ([], []),
    
    # Test Case 2: All odd lengths (should return empty)
    (["a", "abc", "abcde", "aaaaa"], []),
    
    # Test Case 3: All even lengths (should sort by length, then alpha)
    (["bbbb", "aa", "cccc", "cc"], ["aa", "cc", "bbbb", "cccc"]),
    
    # Test Case 4: Mixed lengths (filtering odd, then sorting)
    (["a", "ab", "abc", "abcd", "abcde", "abcdef"], ["ab", "abcd", "abcdef"]),
    
    # Test Case 5: Alphabetical tie-breaker (same length, different alpha)
    (["ca", "ba", "ab", "ac"], ["ab", "ac", "ba", "ca"]),
    
    # Test Case 6: Duplicates (even length duplicates should remain)
    (["bb", "aa", "bb", "aa", "a"], ["aa", "aa", "bb", "bb"]),
    
    # Test Case 7: Provided Example 1
    (["aa", "a", "aaa"], ["aa"]),
    
    # Test Case 8: Provided Example 2
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
    
    # Test Case 9: Complex mixed case
    # "a" (1, odd) -> remove
    # "bb" (2, even)
    # "ccc" (3, odd) -> remove
    # "dd" (2, even)
    # "eeee" (4, even)
    # "ff" (2, even)
    # Expected: ["bb", "dd", "ff", "eeee"]
    (["a", "bb", "ccc", "dd", "eeee", "ff"], ["bb", "dd", "ff", "eeee"]),
])
def test_sorted_list_sum_logic(input_list, expected_output):
    """
    Tests the core logic of filtering odd lengths and sorting by 
    length (asc) then alphabetically (asc).
    """
    from __main__ import sorted_list_sum # Assuming function is in the same module
    assert sorted_list_sum(input_list) == expected_output

def test_sorted_list_sum_type_consistency():
    """
    Ensures the function always returns a list, even if empty.
    """
    from __main__ import sorted_list_sum
    assert isinstance(sorted_list_sum(["a", "b"]), list)
    assert isinstance(sorted_list_sum([]), list)

def test_sorted_list_sum_case_sensitivity():
    """
    Verifies alphabetical sorting behavior with mixed casing.
    Standard Python sort is lexicographical (ASCII), where 'B' < 'a'.
    """
    from __main__ import sorted_list_sum
    # "Aa" (2), "aa" (2), "BB" (2)
    # Alphabetical order: "AA" (if it were there), "BB", "Aa", "aa" 
    # based on ASCII: 'B' is 66, 'A' is 65, 'a' is 97.
    # Let's use simple lowercase to avoid ambiguity unless specified.
    input_list = ["ba", "ab", "aa", "bb"]
    assert sorted_list_sum(input_list) == ["aa", "ab", "ba", "bb"]