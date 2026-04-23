
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

@pytest.mark.parametrize("input_list, expected_output", [
    # Provided examples
    (["aa", "a", "aaa"], ["aa"]),
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
    
    # Edge Case: Empty list
    ([], []),
    
    # Edge Case: All odd lengths (should return empty)
    (["a", "abc", "abcde", "a"], []),
    
    # Edge Case: All even lengths, same length (should sort alphabetically)
    (["dc", "ba", "ca", "bb"], ["ba", "bb", "ca", "dc"]),
    
    # Edge Case: All even lengths, different lengths (should sort by length then alpha)
    (["abcd", "ab", "zz", "aa"], ["aa", "zz", "ab", "abcd"]),
    
    # Case: Mixed lengths and duplicates
    (["apple", "pear", "kiwi", "banana", "pear", "a"], ["kiwi", "pear", "pear", "banana"]),
    
    # Case: Single element even
    (["aa"], ["aa"]),
    
    # Case: Single element odd
    (["a"], []),
    
    # Case: Duplicate even strings
    (["bb", "aa", "bb", "aa"], ["aa", "aa", "bb", "bb"]),
])
def test_sorted_list_sum(input_list, expected_output):
    """
    Tests the sorted_list_sum function against various scenarios including
    provided examples, edge cases, and complex sorting requirements.
    """
    assert sorted_list_sum(input_list) == expected_output

def test_sorting_logic_integrity():
    """
    Specific test to ensure the primary sort key is length 
    and the secondary sort key is alphabetical.
    """
    # Lengths: 2, 2, 4, 6
    # Strings: "zz", "aa", "abcd", "abcdef"
    # Expected: "aa" (len 2), "zz" (len 2), "abcd" (len 4), "abcdef" (len 6)
    input_data = ["abcdef", "abcd", "zz", "aa"]
    expected = ["aa", "zz", "abcd", "abcdef"]
    assert sorted_list_sum(input_data) == expected

def test_no_odd_strings_remain():
    """
    Ensures that no strings with odd lengths exist in the output.
    """
    input_data = ["a", "bb", "ccc", "dddd", "eeeee", "ffffff"]
    result = sorted_list_sum(input_data)
    for word in result:
        assert len(word) % 2 == 0, f"Found odd length word in result: {word}"