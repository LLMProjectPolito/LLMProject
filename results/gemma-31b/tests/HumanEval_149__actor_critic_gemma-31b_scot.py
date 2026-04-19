
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

# The function sorted_list_sum is defined in the environment.
# Functional requirements: 
# 1. Remove strings with odd lengths.
# 2. Sort by length (ascending).
# 3. Sort alphabetically (ascending) if lengths are equal.
# 4. Return a list of strings.

@pytest.mark.parametrize("input_list, expected", [
    # Basic examples from docstring
    (["aa", "a", "aaa"], ["aa"]),
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
    
    # Edge Case: Empty list
    ([], []),
    
    # Edge Case: All odd lengths (should return empty)
    (["a", "aaa", "abcde", "123"], []),
    
    # Edge Case: All even lengths, already sorted
    (["aa", "bb", "cccc"], ["aa", "bb", "cccc"]),
    
    # Edge Case: All even lengths, unsorted
    (["cccc", "bb", "aa"], ["aa", "bb", "cccc"]),
    
    # Secondary Sort: Same length, alphabetical order
    (["ba", "ab", "dc", "ca"], ["ab", "ba", "ca", "dc"]),
    
    # Primary Sort: Different even lengths
    (["abcdef", "abcd", "ab"], ["ab", "abcd", "abcdef"]),
    
    # Duplicates: Should be preserved and sorted
    (["aa", "bb", "aa", "bb"], ["aa", "aa", "bb", "bb"]),
    
    # Mixed: Odd lengths removed, then sorted by length, then alpha
    (["apple", "banana", "pear", "kiwi", "plum", "orange"], 
     ["kiwi", "pear", "plum", "banana", "orange"]),
    
    # Special characters and spaces (even lengths)
    (["a b ", "ab", "abc "], ["ab", "a b ", "abc "]), 
    
    # Edge Case: Empty Strings (Length 0 is even)
    (["", "a", "bb", ""], ["", "", "bb"]),
    
    # Edge Case: Case Sensitivity (ASCII: 'B' < 'a')
    (["Ba", "aa", "BB"], ["BB", "Ba", "aa"]),
    
    # Mixed Case and Lengths
    # Corrected: "banana" (6) is even and must be preserved
    (["Apple", "banana", "Cat", "dog", "Egg"], ["banana"]), 
    (["Apple", "banana", "Pear", "Kiwi"], ["Kiwi", "Pear", "banana"]), # 4, 4, 6
])
def test_sorted_list_sum_parametrized(input_list, expected):
    """
    Tests the sorted_list_sum function against various scenarios including
    filtering odd lengths, sorting by length, and alphabetical order.
    """
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_mutation():
    """
    Ensure the original list is not mutated.
    """
    original = ["ba", "ab", "a"]
    original_copy = list(original)
    sorted_list_sum(original)
    assert original == original_copy, "The original input list should not be mutated."

def test_sorted_list_sum_invalid_types():
    """
    Verify that the function handles non-string elements gracefully.
    Since the problem states input is always strings, we expect a TypeError 
    if the implementation tries to call len() or sort on incompatible types.
    """
    with pytest.raises(TypeError):
        sorted_list_sum([123, 456])
    
    with pytest.raises(TypeError):
        sorted_list_sum(["aa", None])