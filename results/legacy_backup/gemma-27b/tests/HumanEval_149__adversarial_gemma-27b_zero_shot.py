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

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "aaa", "abc"]) == []

def test_all_even_lengths():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_lengths():
    assert sorted_list_sum(["aa", "a", "aaa", "bb"]) == ["aa", "bb"]

def test_mixed_lengths_with_duplicates():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "aa"]) == ["aa", "aa", "bb"]

def test_same_length_alphabetical():
    assert sorted_list_sum(["ab", "cd", "aa"]) == ["aa", "ab", "cd"]

def test_example_1():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_example_2():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_long_strings():
    assert sorted_list_sum(["abcdef", "abc", "defghi", "abcd"]) == ["abcd", "abcdef"]

def test_strings_with_spaces():
    assert sorted_list_sum(["aa bb", "a", "ccc dd"]) == ["aa bb"]

def test_strings_with_special_characters():
    assert sorted_list_sum(["a!", "bb@", "c#d"]) == ["a!", "bb@", "c#d"]

def test_large_list():
    large_list = ["a" * i for i in range(1, 21)]
    expected_result = ["a" * i for i in range(2, 21, 2)]
    assert sorted_list_sum(large_list) == expected_result