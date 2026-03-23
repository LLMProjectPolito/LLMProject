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

def test_sorted_list_sum_empty_list():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd_length():
    assert sorted_list_sum(["aa", "a", "aaa"]) == []

def test_sorted_list_sum_all_even_length():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_sorted_list_sum_mixed_lengths():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_with_duplicates():
    assert sorted_list_sum(["aa", "a", "aaa", "aa"]) == ["aa", "aa"]

def test_sorted_list_sum_same_length_alphabetical():
    assert sorted_list_sum(["ab", "ac", "ba", "bc"]) == ["ab", "ac", "ba", "bc"]

def test_sorted_list_sum_single_element():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_sorted_list_sum_single_odd_element():
    assert sorted_list_sum(["a"]) == []

def test_sorted_list_sum_complex_case():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape"]) == ["banana", "orange"]