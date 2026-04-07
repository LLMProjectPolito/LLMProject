
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
    assert sorted_list_sum(["a", "aa", "aaa", "b", "bb"]) == sorted(["aa", "bb"])

def test_duplicates():
    assert sorted_list_sum(["aa", "aa", "bb", "cc", "aa"]) == sorted(["aa", "aa", "bb", "cc", "aa"])

def test_same_length_alphabetical():
    assert sorted_list_sum(["ab", "aa", "ac"]) == sorted(["aa", "ab", "ac"])

def test_single_element_even():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_element_odd():
    assert sorted_list_sum(["a"]) == []

def test_longer_strings():
    assert sorted_list_sum(["abcdef", "abc", "defgh", "hi"]) == sorted(["abcdef", "defgh"])
    assert sorted_list_sum(["hello", "world", "hi", "there"]) == sorted(["hello", "world", "there"])

def test_mixed_case():
    assert sorted_list_sum(["aA", "bb", "cCc"]) == sorted(["aA", "bb", "cCc"])

def test_special_characters():
    assert sorted_list_sum(["!@#", "abc", "$%^"]) == sorted(["!@#", "$%^"])

def test_numbers_as_strings():
    assert sorted_list_sum(["12", "123", "456"]) == sorted(["12", "456"])
    assert sorted_list_sum(["12", "123", "45"]) == sorted(["12", "45"])

def test_empty_strings():
    assert sorted_list_sum(["", "a", ""]) == []

def test_long_list():
    long_list = ["a" * i for i in range(1, 21)]
    expected = sorted([s for s in long_list if len(s) % 2 == 0])
    assert sorted_list_sum(long_list) == expected

def test_single_even_length_string():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_odd_length_string():
    assert sorted_list_sum(["a"]) == []

def test_complex_mix():
    assert sorted_list_sum(["abc", "defg", "hi", "jklm", "nopq", "rs"]) == sorted(["nopq"])

def test_edge_case_long_string():
    long_string = "a" * 100
    assert sorted_list_sum([long_string, "a"]) == [long_string]

def test_multiple_same_length_strings():
    assert sorted_list_sum(["ab", "cd", "ef", "gh"]) == sorted(["ab", "cd", "ef", "gh"])