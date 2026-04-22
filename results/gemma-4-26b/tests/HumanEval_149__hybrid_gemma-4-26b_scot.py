
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
from your_module import sorted_list_sum  # Replace 'your_module' with actual module name

@pytest.mark.parametrize("input_list, expected_output", [
    # --- Basic Scenarios ---
    ([], []),                                      # Empty list
    (["a", "abc", "abcde"], []),                   # All odd lengths
    (["bb", "aa", "cccc", "dd"], ["aa", "bb", "dd", "cccc"]), # All even (sort length, then alpha)
    
    # --- Mixed & Filtering ---
    (["apple", "pear", "kiwi", "a", "bb"], ["bb", "kiwi", "pear"]), # Mixed (filter odd, sort even)
    (["ab", "a", "aaa", "cd", "efgh"], ["ab", "cd", "efgh"]),      # Mixed (Suite 2 variation)
    
    # --- Duplicates & Tie-breaking ---
    (["bb", "aa", "aa", "cc", "a"], ["aa", "aa", "bb", "cc"]),     # Duplicates preserved
    (["dc", "ba", "ab", "cc"], ["ab", "ba", "cc", "dc"]),          # Alphabetical tie-break
    
    # --- Docstring Examples ---
    (["aa", "a", "aaa"], ["aa"]),                  # Docstring Example 1
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),      # Docstring Example 2
])
def test_sorted_list_sum_logic(input_list, expected_output):
    """
    Tests the core logic of the function:
    1. Filtering even-length strings.
    2. Sorting by length (ascending).
    3. Sorting alphabetically (ascending) for ties.
    4. Preserving duplicates.
    """
    assert sorted_list_sum(input_list) == expected_output

def test_single_element_scenarios():
    """Test boundary cases with single-element lists."""
    assert sorted_list_sum(["aa"]) == ["aa"]  # Single even
    assert sorted_list_sum(["a"]) == []       # Single odd

def test_large_gap_lengths():
    """Test sorting stability when even lengths have large gaps."""
    input_data = ["zzzzzz", "aa", "bbbb", "c"]
    # "c" (3) -> skip; "aa" (2), "bbbb" (4), "zzzzzz" (6)
    assert sorted_list_sum(input_data) == ["aa", "bbbb", "zzzzzz"]

def test_case_sensitivity():
    """
    Test alphabetical sorting with mixed case.
    Verifies standard Python/ASCII order (Uppercase < Lowercase).
    """
    input_list = ["bb", "Aa", "aa"]
    # All length 2. Alphabetical: Aa, aa, bb
    expected = ["Aa", "aa", "bb"]
    assert sorted_list_sum(input_list) == expected

def test_large_even_lengths():
    """Test with larger even-length strings to ensure no length-based logic errors."""
    input_list = ["abcdef", "ab", "abcd", "abcde"]
    # Even: "ab" (2), "abcd" (4), "abcdef" (6)
    expected = ["ab", "abcd", "abcdef"]
    assert sorted_list_sum(input_list) == expected