
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

# The function signature provided in the problem
# def sorted_list_sum(lst: list[str]) -> list[str]:

@pytest.mark.parametrize("input_list, expected_output", [
    # --- Basic Functionality (from examples) ---
    (["aa", "a", "aaa"], ["aa"]),
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
    
    # --- Edge Case: Empty Input ---
    ([], []),
    
    # --- Edge Case: All Odd Lengths (Should return empty) ---
    (["a", "abc", "abcde", "a"], []),
    
    # --- Edge Case: All Even Lengths (Should only sort alphabetically) ---
    (["zz", "aa", "bb", "cc"], ["aa", "bb", "cc", "zz"]),
    
    # --- Edge Case: Mixed Lengths (Filtering + Sorting) ---
    # "a" (1), "bb" (2), "ccc" (3), "dd" (2), "eeee" (4)
    # Expected: ["bb", "dd", "eeee"]
    (["a", "bb", "ccc", "dd", "eeee"], ["bb", "dd", "eeee"]),
    
    # --- Requirement: Tie-breaker (Same length, sort alphabetically) ---
    (["ca", "ba", "ab", "aa"], ["aa", "ab", "ba", "ca"]),
    
    # --- Requirement: Sorting by length first ---
    # "abcd" (4), "aa" (2), "bb" (2), "c" (1)
    # Expected: ["aa", "bb", "abcd"]
    (["abcd", "aa", "bb", "c"], ["aa", "bb", "abcd"]),
    
    # --- Edge Case: Duplicates ---
    (["aa", "bb", "aa", "a", "cc"], ["aa", "aa", "bb", "cc"]),
    
    # --- Edge Case: Case Sensitivity ---
    # Standard Python sort: 'B' (66) comes before 'a' (97)
    (["ba", "Ab", "a", "ab"], ["Ab", "ab", "ba"]),
    
    # --- Edge Case: Special Characters and Spaces ---
    # "a " is length 2, "!!" is length 2
    (["a", "!!", "a ", "abc"], ["!!", "a ", "a "]), # Wait, "a " is length 2. 
    # Let's refine: ["a", "!!", "a ", "abc"] -> ["!!", "a "]
    (["a", "!!", "a ", "abc"], ["!!", "a "]),
])
def test_sorted_list_sum_logic(input_list, expected_output):
    """Tests the core logic: filter odd, sort by length, then alphabetically."""
    from your_module import sorted_list_sum # Replace with actual module name
    assert sorted_list_sum(input_list) == expected_output

def test_sorted_list_sum_non_string_elements():
    """
    Blue Team: Check if the function handles unexpected types gracefully.
    The docstring says 'The list is always a list of strings', 
    but a robust function should handle or fail predictably.
    """
    from your_module import sorted_list_sum
    with pytest.raises(TypeError):
        sorted_list_sum([1, 2, 3])

def test_sorted_list_sum_immutability():
    """
    Blue Team: Ensure the function does not mutate the original input list.
    """
    from your_module import sorted_list_sum
    original = ["aa", "a", "bb"]
    input_copy = list(original)
    sorted_list_sum(input_copy)
    assert input_copy == original, "The function mutated the original input list!"

def test_sorted_list_sum_large_input():
    """
    Blue Team: Performance/Stress test.
    """
    from your_module import sorted_list_sum
    large_list = ["a"] * 1000 + ["bb"] * 1000 + ["ccc"] * 1000
    result = sorted_list_sum(large_list)
    assert len(result) == 2000
    assert all(len(word) == 2 for word in result)