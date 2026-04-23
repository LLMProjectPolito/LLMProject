
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

# Note: The function being tested is assumed to be 'sorted_list_sum'
# Logic: Filter even-length strings, sort by length (asc), then alphabetically (asc).

@pytest.mark.parametrize("input_list, expected", [
    # --- 1. Provided Docstring Examples ---
    (["aa", "a", "aaa"], ["aa"]),
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),

    # --- 2. Filtering Logic (Even vs Odd) ---
    ([], []),                                # Empty input
    (["a", "abc", "abcde", "123"], []),      # All odd lengths
    (["apple", "pear", "kiwi", "banana"], ["kiwi", "pear"]), # Mixed (apple/banana are odd)
    (["a", "bb", "ccc", "dddd", "ee"], ["bb", "ee"]),       # Mixed (only bb and ee are even)

    # --- 3. Sorting Logic (Length then Alphabetical) ---
    (["cc", "aa", "bb"], ["aa", "bb", "cc"]), # Same length, alphabetical
    (["zzzz", "ab", "ba", "aaaa", "cd"], ["ab", "ba", "cd", "aaaa", "zzzz"]), # Mixed lengths
    (["xy", "ab", "cd", "ef"], ["ab", "cd", "ef", "xy"]), # All even, same length
    
    # --- 4. Data Integrity (Duplicates) ---
    (["bb", "aa", "bb", "a", "aa"], ["aa", "aa", "bb", "bb"]),
    (["bb", "aa", "aa", "a", "ccc"], ["aa", "aa", "bb"]),

    # --- 5. Edge Cases (Empty strings, spaces, special chars) ---
    (["a", "", "abc", "  ", "b", "a "], ["", "  ", "a "]), # "" (0), "  " (2), "a " (2)
])
def test_sorted_list_sum_scenarios(input_list, expected):
    """
    Comprehensive test covering docstring examples, filtering, 
    sorting rules, duplicates, and edge cases via parametrization.
    """
    assert sorted_list_sum(input_list) == expected


def test_sorted_list_sum_case_sensitivity():
    """
    Tests specific behavior regarding Unicode/ASCII sorting.
    Standard Python sort: Uppercase (A=65) < Lowercase (a=97).
    """
    # "Aa" (len 2), "aa" (len 2) -> "Aa" should come first
    assert sorted_list_sum(["aa", "Aa"]) == ["Aa", "aa"]
    # "B" (len 1 - odd), "a" (len 1 - odd), "AA" (len 2), "bb" (len 2)
    assert sorted_list_sum(["bb", "AA", "a", "B"]) == ["AA", "bb"]


def test_sorted_list_sum_complex_types():
    """
    Tests behavior with strings containing numbers and symbols 
    to ensure standard string comparison is maintained.
    """
    # "12" (2), "!!" (2), "a" (1)
    # "!!" comes before "12" in ASCII
    assert sorted_list_sum(["12", "!!", "a"]) == ["!!", "12"]