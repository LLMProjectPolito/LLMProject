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
# STEP 1: REASONING - The function needs to filter strings based on even length, then sort the remaining strings based on length first and then alphabetically.
# STEP 2: PLAN -
# test_empty_list: Test with an empty list.
# test_all_odd_length: Test with a list where all strings have odd lengths.
# test_all_even_length: Test with a list where all strings have even lengths.
# test_mixed_odd_even: Test with a list containing both odd and even length strings.
# test_duplicate_lengths: Test with strings of the same length to verify alphabetical sorting.
# test_single_element: Test with a list containing a single element.
# test_basic_example1: Test the example provided in the prompt.
# test_basic_example2: Test the example provided in the prompt.

### STEP 3: CODE -
def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_length():
    assert sorted_list_sum(["a", "b", "c"]) == []

def test_all_even_length():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_odd_even():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_duplicate_lengths():
    assert sorted_list_sum(["ab", "ac", "ba", "bc"]) == ["ab", "ac", "ba", "bc"]

def test_single_element():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_basic_example1():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_basic_example2():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]