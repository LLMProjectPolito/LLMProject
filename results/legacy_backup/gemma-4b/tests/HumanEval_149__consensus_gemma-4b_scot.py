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
# STEP 1: REASONING - The function needs to filter strings based on even length, then sort the remaining strings first by length and then alphabetically.
# STEP 2: PLAN -
# - Test case 1: Empty list
# - Test case 2: List with only odd length strings
# - Test case 3: List with only even length strings
# - Test case 4: List with mixed odd and even length strings
# - Test case 5: List with duplicate strings
# - Test case 6: List with strings of same length
# STEP 3: CODE -
def test_empty_list():
    assert sorted_list_sum([]) == []

def test_odd_length_strings():
    assert sorted_list_sum(["a", "b", "c"]) == []

def test_even_length_strings():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_odd_even_strings():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_duplicate_strings():
    assert sorted_list_sum(["aa", "a", "aaa", "aa"]) == ["aa", "aa"]

def test_same_length_strings():
    assert sorted_list_sum(["ab", "ac", "ba", "bc"]) == ["ab", "ac", "ba", "bc"]

def test_mixed_strings():
    assert sorted_list_sum(["aa", "a", "aaa", "ab", "cd"]) == ["aa", "ab", "cd"]

def test_longer_strings():
    assert sorted_list_sum(["abcdef", "abc", "def"]) == ["abcdef", "def"]