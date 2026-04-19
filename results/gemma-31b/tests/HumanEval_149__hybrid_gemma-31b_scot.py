
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

# The function sorted_list_sum is already defined in the environment.

@pytest.mark.parametrize("input_list, expected_output", [
    # --- Edge Cases ---
    ([], []),                                           # Empty list
    (["a", "aaa", "abcde", "123"], []),                # All odd lengths
    (["a", "b", "c"], []),                             # Single char strings (odd)
    
    # --- Sorting Logic: Same Length (Alphabetical) ---
    (["cc", "aa", "bb"], ["aa", "bb", "cc"]),          # Simple alpha sort
    (["ba", "ab", "ca"], ["ab", "ba", "ca"]),          # Simple alpha sort
    
    # --- Sorting Logic: Different Lengths (Length Sort) ---
    (["abcdef", "ab", "abcd"], ["ab", "abcd", "abcdef"]), 
    (["abcdefghij", "abcd", "ab", "abcdefgh"], ["ab", "abcd", "abcdefgh", "abcdefghij"]),
    
    # --- Combined Logic: Filter -> Length -> Alphabetical ---
    (["apple", "banana", "cherry", "date"], ["date", "banana", "cherry"]), 
    # date(4), banana(6), cherry(6)
    
    (["ijkl", "m", "ab", "nop", "efgh", "cd"], ["ab", "cd", "efgh", "ijkl"]),
    # Filtered: ab(2), cd(2), efgh(4), ijkl(4)
    
    (["banana", "apple", "pear", "kiwi", "plum", "fig", "orange"], 
     ["kiwi", "pear", "plum", "banana", "orange"]),
    # Even: banana(6), pear(4), kiwi(4), plum(4), orange(6)
    # Length 4 alpha: kiwi, pear, plum
    # Length 6 alpha: banana, orange
    
    # --- Special Character & Case Handling ---
    (["bb", "AA", "aa", "BB"], ["AA", "BB", "aa", "bb"]), # ASCII: Upper < Lower
    (["Ba", "aa", "Ab"], ["Ab", "Ba", "aa"]),             # Mixed case
    (["1234", "12", "!!", "!!!"], ["!!", "12", "1234"]),  # Symbols and numbers
    
    # --- Duplicates ---
    (["bb", "aa", "b", "aa"], ["aa", "aa", "bb"]),
    
    # --- Docstring Examples ---
    (["aa", "a", "aaa"], ["aa"]),
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
])
def test_sorted_list_sum_scenarios(input_list, expected_output):
    """
    Tests the core requirements: filtering odd lengths, sorting by length, 
    and then sorting alphabetically.
    """
    assert sorted_list_sum(input_list) == expected_output

def test_sorted_list_sum_immutability():
    """
    Verify that the original input list is not mutated by the function.
    """
    original = ["banana", "apple", "pear"]
    original_copy = list(original)
    _ = sorted_list_sum(original)
    assert original == original_copy, "The original list should not be mutated."

def test_sorted_list_sum_stability_with_large_input():
    """
    Test with a larger set of even-length strings to ensure sorting stability.
    """
    input_list = ["zz" * 50, "aa" * 50, "bb" * 25, "cc" * 25]
    # Lengths: 100, 100, 50, 50
    # Expected: 50s (bb, cc), then 100s (aa, zz)
    expected = ["bb" * 25, "cc" * 25, "aa" * 50, "zz" * 50]
    assert sorted_list_sum(input_list) == expected