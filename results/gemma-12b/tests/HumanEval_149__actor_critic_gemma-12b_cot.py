
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

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_only_odd_length_strings():
    assert sorted_list_sum(["a", "bbb", "ccccc"]) == []

def test_only_even_length_strings():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_list():
    assert sorted_list_sum(["aa", "a", "aaa", "cd"]) == ["aa", "cd"]

def test_duplicates():
    assert sorted_list_sum(["aa", "aa", "a", "aaa", "bb", "bb"]) == ["aa", "aa", "bb", "bb"]

def test_same_length_alphabetical():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_mixed_lengths_and_duplicates():
    assert sorted_list_sum(["aa", "a", "aaa", "cd", "aa", "bb"]) == ["aa", "aa", "bb", "cd"]

def test_long_strings():
    assert sorted_list_sum(["abcdef", "abcde", "abcdefg"]) == ["abcdef"]

def test_special_characters():
    assert sorted_list_sum(["a!", "aa?", "a!!"]) == ["aa?"]

def test_empty_string():
    assert sorted_list_sum([""]) == [""]

def test_single_string_odd():
    assert sorted_list_sum(["a"]) == []

def test_single_string_even():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_complex_sorting():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape", "pear", "apricot"]) == ["kiwi", "pear", "apple", "grape", "orange", "banana", "apricot"]

def test_case_sensitivity():
    assert sorted_list_sum(["Aa", "aa"]) == ["aa", "Aa"]

def test_list_with_one_element():
    assert sorted_list_sum(["abc"]) == []

def test_large_list():
    large_list = ["a" * i for i in range(1, 100, 2)] + ["b" * i for i in range(2, 100, 2)]
    result = sorted_list_sum(large_list)
    expected = ["b" * i for i in range(2, 100, 2)]
    assert result == expected

def test_very_long_strings():
    long_string = "x" * 200
    assert sorted_list_sum([long_string]) == [long_string]

def test_unicode_characters():
    assert sorted_list_sum(["你好", "世界", "你好世界"]) == ["你好世界", "你好", "世界"]