
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
    """
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings


def test_sorted_list_sum_basic():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_sorted_list_sum_mixed():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_only_odd():
    assert sorted_list_sum(["a", "aaa", "abcde"]) == []

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "aa", "a", "aaa"]) == ["aa", "aa"]

def test_sorted_list_sum_varying_lengths():
    assert sorted_list_sum(["aa", "b", "ccc", "dddd", "ee"]) == ["aa", "b", "ee", "dddd"]

def test_sorted_list_sum_same_length_alphabetical():
    assert sorted_list_sum(["ab", "ac", "ba", "ca"]) == ["ab", "ac", "ba", "ca"]

def test_sorted_list_sum_complex():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape"]) == ["kiwi", "grape"]

def test_sorted_list_sum_all_even():
    assert sorted_list_sum(["aa", "bb", "cc", "dd"]) == ["aa", "bb", "cc", "dd"]

def test_sorted_list_sum_case_sensitivity():
    assert sorted_list_sum(["Aa", "aa", "a"]) == ["Aa", "aa"]

def test_sorted_list_sum_same_length_alphabetical_extended():
    assert sorted_list_sum(["abc", "abd", "bac", "bad", "cba", "cbd"]) == ["abc", "abd", "bac", "bad", "cba", "cbd"]

def test_sorted_list_sum_with_special_characters():
    assert sorted_list_sum(["a b", "aa", "a!", "abc "]) == ["aa", "a b", "a!", "abc "]

def test_sorted_list_sum_with_unicode_characters():
    assert sorted_list_sum(["你好", "世界", "a", "aa"]) == ["aa", "你好", "世界"]