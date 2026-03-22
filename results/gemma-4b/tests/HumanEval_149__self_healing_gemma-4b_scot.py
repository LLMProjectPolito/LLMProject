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
    new_list = []
    for s in lst:
        if len(s) % 2 == 0:
            new_list.append(s)
    new_list.sort(key=lambda x: (len(x), x))
    return new_list

### SCoT Steps:
# STEP 1: REASONING - The function needs to filter even-length strings from the input list, then sort the remaining strings based on length (ascending) and alphabetically (ascending) if lengths are equal.
# STEP 2: PLAN -
#   - Test case 1: Empty list - Should return an empty list.
#   - Test case 2: List with only odd-length strings - Should return an empty list.
#   - Test case 3: List with only even-length strings - Should return the list itself.
#   - Test case 4: List with mixed odd and even-length strings - Should return the even-length strings sorted by length and then alphabetically.
#   - Test case 5: List with duplicate strings - Should return the duplicates sorted correctly.
# STEP 3: CODE -
###
def test_empty_list():
    assert sorted_list_sum([]) == []

def test_odd_length_strings():
    assert sorted_list_sum(["a", "b", "c"]) == []

def test_even_length_strings():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_strings():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_duplicate_strings():
    assert sorted_list_sum(["aa", "a", "aaa", "aa"]) == ["aa", "aa"]

def test_single_even_length_string():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_odd_length_string():
    assert sorted_list_sum(["a"]) == []

def test_longer_strings():
    assert sorted_list_sum(["abcdef", "abc", "abcd"]) == ["abcd", "abcdef"]

def test_strings_with_same_length():
    assert sorted_list_sum(["abc", "def", "ghi"]) == ["abc", "def", "ghi"]