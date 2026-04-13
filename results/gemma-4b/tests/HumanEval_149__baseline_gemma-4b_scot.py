
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
    filtered_list = [s for s in lst if len(s) % 2 == 0]
    filtered_list.sort(key=lambda x: (len(x), x))
    return filtered_list

### STEP 1: REASONING
# The function `sorted_list_sum` takes a list of strings as input.
# It filters out strings with odd lengths, keeping only even-length strings.
# Then, it sorts the remaining strings first by length (ascending) and then alphabetically (ascending) for strings of the same length.
# The function returns the sorted list of strings.
# We need to test various scenarios including empty list, list with odd and even length strings, list with duplicates, and lists with different lengths.

### STEP 2: PLAN
# Test cases:
# 1. Empty list: []
# 2. List with only odd length strings: ["a", "b", "c"]
# 3. List with only even length strings: ["aa", "bb", "cc"]
# 4. List with mixed odd and even length strings: ["aa", "a", "aaa", "cd"]
# 5. List with duplicates: ["aa", "aa", "a", "aaa"]
# 6. List with different lengths: ["ab", "a", "aaa", "cd", "efg"]
# 7. List with single element: ["aa"]
# 8. List with single odd element: ["a"]

### STEP 3: CODE
def test_empty_list():
    assert sorted_list_sum([]) == []

def test_odd_length_strings():
    assert sorted_list_sum(["a", "b", "c"]) == []

def test_even_length_strings():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_odd_even_strings():
    assert sorted_list_sum(["aa", "a", "aaa", "cd"]) == ["aa", "cd"]

def test_duplicates():
    assert sorted_list_sum(["aa", "aa", "a", "aaa"]) == ["aa", "aa"]

def test_different_lengths():
    assert sorted_list_sum(["ab", "a", "aaa", "cd", "efg"]) == ["ab", "cd"]

def test_single_element():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_odd_element():
    assert sorted_list_sum(["a"]) == []

def test_complex_list():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape"]) == ["banana", "orange"]