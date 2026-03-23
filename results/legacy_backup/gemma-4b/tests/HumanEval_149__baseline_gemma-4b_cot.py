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

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_length_strings():
    assert sorted_list_sum(["a", "b", "c"]) == []

def test_all_even_length_strings():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_odd_even_strings():
    assert sorted_list_sum(["aa", "a", "aaa", "cd"]) == ["aa", "cd"]

def test_duplicate_strings():
    assert sorted_list_sum(["aa", "aa", "a"]) == ["aa", "aa"]

def test_longer_strings_first():
    assert sorted_list_sum(["aaa", "aa", "ab", "cd"]) == ["aa", "cd"]

def test_alphabetical_sort_same_length():
    assert sorted_list_sum(["ab", "ac", "ba", "bc"]) == ["ab", "ac", "ba", "bc"]

def test_single_element_list():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_complex_list():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape"]) == ["banana", "orange"]