
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
    Implementation of the described logic:
    1. Remove strings with odd lengths.
    2. Sort by length (ascending).
    3. Sort alphabetically if lengths are equal.
    """
    # Filter out odd lengths
    filtered = [s for s in lst if len(s) % 2 == 0]
    # Sort by length first, then alphabetically
    filtered.sort(key=lambda x: (len(x), x))
    return filtered

class TestSortedListSum:
    """
    Superior test suite for sorted_list_sum function, merging comprehensive 
    edge cases, functional requirements, and stability checks.
    """

    @pytest.mark.parametrize("input_list, expected", [
        # Basic examples
        (["aa", "a", "aaa"], ["aa"]),
        (["ab", "a", "aaa", "cd"], ["ab", "cd"]),
        
        # Edge Case: Empty list
        ([], []),
        
        # Edge Case: All odd lengths (should return empty list)
        (["a", "abc", "abcde", "123"], []),
        
        # Edge Case: All even lengths, already sorted
        (["aa", "bbbb", "cccccc"], ["aa", "bbbb", "cccccc"]),
        
        # Edge Case: All even lengths, unsorted by length
        (["abcdef", "ab", "abcd"], ["ab", "abcd", "abcdef"]),
        
        # Test: Alphabetical sort for same lengths
        (["zebra", "apple", "bear", "cat", "dog", "fish"], ["bear", "fish"]), 
        (["dc", "ba", "ca", "ad"], ["ad", "ba", "ca", "dc"]),
        
        # Test: Mixed lengths and alphabetical order
        (["zz", "bbbb", "aa", "cccc", "dd"], ["aa", "dd", "zz", "bbbb", "cccc"]),
        (["dddd", "aa", "cccc", "bb"], ["aa", "bb", "cccc", "dddd"]),
        
        # Test: Duplicates
        (["aa", "aa", "bb", "bb", "a"], ["aa", "aa", "bb", "bb"]),
        
        # Test: Case Sensitivity (ASCII: uppercase comes before lowercase)
        (["Bb", "AA", "aa", "BB"], ["AA", "BB", "Bb", "aa"]),
        
        # Test: Strings containing numbers, special characters, or spaces
        (["12", "123", "!!", "!!!", "1234"], ["!!", "12", "1234"]),
        (["a b", "ab", "abc d", "abcd"], ["ab", "a b", "abcd", "abc d"]),
        
        # Test: Large strings
        (["a" * 10, "a" * 2, "a" * 4], ["aa", "aaaa", "aaaaaaaaaa"]),
    ])
    def test_sorted_list_sum_variations(self, input_list, expected):
        """Test a wide variety of input scenarios to ensure filtering and sorting logic."""
        assert sorted_list_sum(input_list) == expected

    def test_original_list_unmodified(self):
        """Ensure the function does not mutate the input list in-place."""
        original = ["bb", "aa", "c"]
        original_copy = original[:]
        sorted_list_sum(original)
        assert original == original_copy, "The original input list should not be mutated"

    def test_idempotency(self):
        """Test that running the function on its own output does not change the result."""
        input_lst = ["apple", "banana", "pear", "kiwi", "plum"]
        first_pass = sorted_list_sum(input_lst)
        second_pass = sorted_list_sum(first_pass)
        assert first_pass == second_pass

    def test_large_input_stability(self):
        """Test with a larger set of strings to verify stability and correctness."""
        input_list = ["a" * i for i in range(1, 11)] # lengths 1 to 10
        # Evens are 2, 4, 6, 8, 10
        expected = ["a" * i for i in range(2, 11, 2)]
        assert sorted_list_sum(input_list) == expected