import pytest

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
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings

# STEP 1: REASONING
# The function `sorted_list_sum` takes a list of strings, filters out strings with odd lengths,
# and returns a sorted list of the remaining strings. The sorting is based on length (ascending)
# and then alphabetically for strings of the same length.
# We need to test various scenarios including:
# 1. Empty list input
# 2. List with only odd length strings
# 3. List with only even length strings
# 4. List with a mix of odd and even length strings
# 5. List with duplicate strings
# 6. List with strings of varying lengths
# 7. List with strings of the same length (to test alphabetical sorting)

# STEP 2: PLAN
# Test functions:
# - test_empty_list: Test with an empty list.
# - test_only_odd_length: Test with a list containing only strings with odd lengths.
# - test_only_even_length: Test with a list containing only strings with even lengths.
# - test_mixed_lengths: Test with a list containing both odd and even length strings.
# - test_duplicate_strings: Test with a list containing duplicate strings.
# - test_varying_lengths: Test with a list containing strings of different lengths.
# - test_same_length_strings: Test with a list containing strings of the same length.
# - test_example_1: Test with the first example provided in the prompt.
# - test_example_2: Test with the second example provided in the prompt.

# STEP 3: CODE
class TestSortedListSum:
    def test_empty_list(self):
        assert sorted_list_sum([]) == []

    def test_only_odd_length(self):
        assert sorted_list_sum(["a", "bbb", "cc"]) == []

    def test_only_even_length(self):
        assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

    def test_mixed_lengths(self):
        assert sorted_list_sum(["a", "aa", "bbb", "cc", "dddd"]) == ["aa", "cc"]

    def test_duplicate_strings(self):
        assert sorted_list_sum(["aa", "aa", "bb", "cc"]) == ["aa", "aa", "bb", "cc"]

    def test_varying_lengths(self):
        assert sorted_list_sum(["a", "aa", "aaa", "aaaa", "aaaaa"]) == ["aa", "aaaa"]

    def test_same_length_strings(self):
        assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

    def test_example_1(self):
        assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

    def test_example_2(self):
        assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]