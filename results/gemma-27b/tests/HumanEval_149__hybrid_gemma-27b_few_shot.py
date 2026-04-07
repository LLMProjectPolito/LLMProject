
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
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings

# Comprehensive Pytest Suite
def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "abc", "def"]) == []

def test_all_even_lengths():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_lengths():
    assert sorted_list_sum(["aa", "a", "aaa", "bb"]) == ["aa", "bb"]

def test_mixed_lengths_with_duplicates():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "aa"]) == ["aa", "aa", "bb"]

def test_same_length_alphabetical():
    assert sorted_list_sum(["cb", "ab", "db"]) == ["ab", "cb", "db"]

def test_longer_strings():
    assert sorted_list_sum(["abcd", "a", "abcde", "efgh", "ijk"]) == ["abcd", "efgh"]

def test_complex_case():
    assert sorted_list_sum(["abc", "defg", "hi", "jklm", "nopq", "rs"]) == ["hi", "nopq"]

def test_case_sensitivity():
    assert sorted_list_sum(["AA", "aa", "Bb", "bb"]) == ["AA", "aa", "Bb", "bb"]

def test_numbers_and_letters():
    assert sorted_list_sum(["a1", "b2", "c3", "d4"]) == ["a1", "b2", "c3", "d4"]

def test_special_characters():
    assert sorted_list_sum(["!@#", "abc", "$%^"]) == ["!@#", "$%^"]

def test_long_strings():
    assert sorted_list_sum(["abcdefgh", "1234567", "ijklmnop"]) == ["abcdefgh", "ijklmnop"]

def test_single_even_length_string():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_odd_length_string():
    assert sorted_list_sum(["a"]) == []

def test_complex_case_2():
    assert sorted_list_sum(["ab", "cd", "ef", "gh", "ij", "kl"]) == ["ab", "cd", "ef", "gh", "ij", "kl"]

def test_complex_case_3():
    assert sorted_list_sum(["abcde", "ab", "cdef", "ghij", "klmn"]) == ["ab"]

def test_mixed_case_and_numbers():
    assert sorted_list_sum(["aB", "12", "Cd", "34"]) == ["12", "34"]

def test_empty_strings():
    assert sorted_list_sum(["", "aa", ""]) == ["aa"]

def test_only_empty_strings():
    assert sorted_list_sum(["", "", ""]) == []

def test_strings_with_spaces():
    assert sorted_list_sum(["ab ", " cd", "ef"]) == ["ab ", " cd"]