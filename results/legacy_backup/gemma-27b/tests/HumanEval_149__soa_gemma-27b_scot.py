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
# The function filters a list of strings, keeping only those with even lengths.
# It then sorts the remaining strings first by length (ascending) and then alphabetically.
# Constraints: Input is always a list of strings.  Handles duplicates.

# STEP 2: PLAN
# Test Cases:
# 1. Empty list: Should return an empty list.
# 2. List with only odd length strings: Should return an empty list.
# 3. List with only even length strings: Should return the sorted list.
# 4. List with mixed odd and even length strings: Should return the sorted list of even length strings.
# 5. List with duplicate strings: Should handle duplicates correctly in the sorted output.
# 6. List with strings of the same length: Should sort alphabetically.
# 7. List with a single even length string: Should return a list containing that string.
# 8. List with a single odd length string: Should return an empty list.
# 9. Larger list with a mix of lengths and duplicates.

# STEP 3: CODE
def test_empty_list():
    assert sorted_list_sum([]) == []

def test_only_odd_length_strings():
    assert sorted_list_sum(["a", "abc", ""]) == []

def test_only_even_length_strings():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_odd_and_even_length_strings():
    assert sorted_list_sum(["aa", "a", "aaa", "cd"]) == ["aa", "cd"]

def test_duplicate_strings():
    assert sorted_list_sum(["aa", "aa", "bb", "a"]) == ["aa", "aa", "bb"]

def test_strings_of_same_length():
    assert sorted_list_sum(["ab", "cd", "ac"]) == ["ab", "ac", "cd"]

def test_single_even_length_string():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_odd_length_string():
    assert sorted_list_sum(["a"]) == []

def test_larger_list():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape", "pear"]) == ["pear", "grape"]

def test_list_with_empty_string():
    assert sorted_list_sum(["", "a", "aa", "aaa", "bb"]) == ["", "bb"]

def test_list_with_multiple_empty_strings():
    assert sorted_list_sum(["", "", "aa", "bb"]) == ["", "", "aa", "bb"]

def test_list_with_same_length_and_duplicates():
    assert sorted_list_sum(["ab", "ab", "cd", "cd", "ac"]) == ["ab", "ab", "ac", "cd", "cd"]