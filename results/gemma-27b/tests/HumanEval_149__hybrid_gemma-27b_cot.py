
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

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "abc", "def"]) == []

def test_all_even_lengths():
    assert sorted_list_sum(["aa", "bb", "cc"]) == sorted(["aa", "bb", "cc"])

def test_mixed_lengths():
    assert sorted_list_sum(["a", "aa", "aaa", "bb", "ccc"]) == sorted(["aa", "bb"])

def test_duplicate_even_lengths():
    assert sorted_list_sum(["aa", "aa", "bb", "cc"]) == sorted(["aa", "aa", "bb", "cc"])

def test_duplicate_even_lengths_with_odd():
    assert sorted_list_sum(["aa", "aa", "a", "bb", "ccc"]) == sorted(["aa", "aa", "bb"])

def test_same_length_alphabetical():
    assert sorted_list_sum(["ab", "aa", "cd", "ac"]) == sorted(["ab", "ac", "aa", "cd"])

def test_longer_list():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape"]) == sorted(["apple", "grape", "orange"])

def test_list_with_empty_string():
    assert sorted_list_sum(["", "a", "aa", "aaa"]) == sorted(["aa"])

def test_list_with_only_empty_string():
    assert sorted_list_sum([""]) == []

def test_list_with_special_characters():
    assert sorted_list_sum(["!@#", "abc", "$%^"]) == sorted(["!@#", "$%^"])

def test_list_with_numbers_as_strings():
    assert sorted_list_sum(["12", "123", "45", "6"]) == sorted(["12", "45"])

def test_list_with_mixed_case():
    assert sorted_list_sum(["Aa", "BB", "a", "b"]) == sorted(["Aa", "BB"])

def test_list_with_unicode_characters():
    assert sorted_list_sum(["你好", "世界", "a"]) == sorted(["你好", "世界"])

def test_duplicate_odd_lengths():
    assert sorted_list_sum(["a", "a", "abc", "def"]) == []

def test_mixed_with_duplicates():
    assert sorted_list_sum(["a", "aa", "a", "bb", "aa"]) == sorted(["aa", "aa", "bb"])

def test_same_length_with_odd():
    assert sorted_list_sum(["ab", "a", "cd"]) == sorted(["ab", "cd"])

def test_long_strings():
    assert sorted_list_sum(["abcdef", "abc", "abcdefgh", "abcd"]) == sorted(["abcd"])

def test_edge_case_even_length_one_char():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_edge_case_odd_length_one_char():
    assert sorted_list_sum(["a"]) == []

def test_complex_case():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape"]) == sorted(["apple", "grape", "kiwi", "orange"])

def test_numbers_as_strings():
    assert sorted_list_sum(["12", "123", "1234", "1"]) == sorted(["12", "1234"])

def test_special_characters():
    assert sorted_list_sum(["!@#", "abc", "!@"]) == sorted(["!@#"])