
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

def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings

import pytest

def test_sorted_list_sum_basic():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_sorted_list_sum_multiple():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_same_length():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_sorted_list_sum_same_length_alphabetical():
    assert sorted_list_sum(["bc", "ab", "cd"]) == ["ab", "bc", "cd"]

def test_sorted_list_sum_empty_list():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_mixed_lengths():
    assert sorted_list_sum(["a", "aa", "aaa", "aaaa"]) == ["aa", "aaaa"]

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "aa", "a"]) == ["aa", "aa"]

def test_sorted_list_sum_non_string_elements_raises_type_error():
    with pytest.raises(TypeError):
        sorted_list_sum(["aa", 123])

def test_sorted_list_sum_invalid_input_raises_type_error():
    with pytest.raises(TypeError):
        sorted_list_sum("not a list")

def test_sorted_list_sum_odd_length_only():
    assert sorted_list_sum(["a", "aaa", "abc"]) == []

def test_sorted_list_sum_longer_strings():
    assert sorted_list_sum(["abcdef", "abc", "ab", "a"]) == ["ab", "abc", "abcdef"]