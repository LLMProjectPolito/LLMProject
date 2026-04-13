
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
    assert sorted_list_sum(["aa", "a", "aaa"]) => ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    new_list = []
    for s in lst:
        if len(s) % 2 == 0:
            new_list.append(s)
    new_list.sort(key=lambda x: (len(x), x))
    return new_list

### SCoT Steps:

# STEP 1: REASONING
# The function `sorted_list_sum` takes a list of strings as input.
# It filters out strings with odd lengths, keeping only even-length strings.
# Then, it sorts the remaining strings first by length (ascending) and then alphabetically (ascending) if lengths are equal.
# The function should return a new list containing the sorted even-length strings.
# Edge cases to consider:
# 1. Empty list: Should return an empty list.
# 2. List with only odd-length strings: Should return an empty list.
# 3. List with only even-length strings: Should return the original list.
# 4. List with mixed odd and even length strings.
# 5. List with duplicate strings.

# STEP 2: PLAN
# Test functions:
# - test_empty_list: Tests the case where the input list is empty.
# - test_odd_length_only: Tests the case where the input list contains only odd-length strings.
# - test_even_length_only: Tests the case where the input list contains only even-length strings.
# - test_mixed_lengths: Tests the case where the input list contains a mix of odd and even-length strings.
# - test_duplicates: Tests the case where the input list contains duplicate strings.
# - test_basic_sorting: Tests a basic sorting scenario with different lengths and alphabetical order.

# STEP 3: CODE
#