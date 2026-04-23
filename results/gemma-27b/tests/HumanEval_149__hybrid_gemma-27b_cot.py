
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
    assert sorted_list_sum(["a", "aa", "aaa", "aaaa"]) == sorted(["aa", "aaaa"])

def test_duplicates():
    assert sorted_list_sum(["aa", "aa", "bb", "cc", "aa"]) == sorted(["aa", "aa", "aa", "bb", "cc"])

def test_same_length_alphabetical():
    assert sorted_list_sum(["ab", "aa", "ac"]) == sorted(["aa", "ab", "ac"])

def test_example_1():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_example_2():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_long_strings():
    assert sorted_list_sum(["abcdef", "abc", "abcd", "abcde"]) == sorted(["abcd", "abcdef"])

def test_strings_with_spaces():
    assert sorted_list_sum(["aa bb", "a", "aaa"]) == ["aa bb"]

def test_strings_with_special_characters():
    assert sorted_list_sum(["a!", "aa", "aaa"]) == ["aa"]

def test_mixed_case():
    assert sorted_list_sum(["aA", "aa", "AAA"]) == ["aA", "aa"]

def test_numbers_as_strings():
    assert sorted_list_sum(["12", "1", "123"]) == ["12"]

def test_long_list():
    long_list = ["a" * i for i in range(1, 21)]
    expected = sorted([s for s in long_list if len(s) % 2 == 0])
    assert sorted_list_sum(long_list) == expected

def test_mixed_lengths_with_duplicates():
    assert sorted_list_sum(["a", "aa", "aaa", "aa", "bb", "cccc"]) == sorted(["aa", "aa", "bb", "cccc"])

def test_same_length_duplicates():
    assert sorted_list_sum(["aa", "aa", "aa"]) == sorted(["aa", "aa", "aa"])

def test_complex_case():
    assert sorted_list_sum(["abc", "ab", "abcd", "a", "abcde", "abcdf"]) == sorted(["ab", "abcd", "abcdf"])

def test_edge_case_long_strings():
    assert sorted_list_sum(["abcdefgh", "abcdef", "abcde"]) == sorted(["abcdef", "abcdefgh"])

def test_edge_case_short_strings():
    assert sorted_list_sum(["a", "b", "c"]) == []

def test_mixed_case_with_empty_string():
    assert sorted_list_sum(["", "a", "aa", "aaa"]) == sorted(["aa"])

def test_list_with_only_one_even_length_string():
    assert sorted_list_sum(["a", "aa", "b"]) == sorted(["aa"])

def test_list_with_only_one_odd_length_string():
    assert sorted_list_sum(["abc"]) == []

def test_list_with_same_length_strings_different_cases():
    assert sorted_list_sum(["Aa", "aA", "aa"]) == sorted(["Aa", "aA", "aa"])

def test_list_with_special_characters():
    assert sorted_list_sum(["!@#", "abc", "!@"]) == sorted(["!@#"])