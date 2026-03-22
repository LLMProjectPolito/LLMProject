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

def test_duplicate_even_lengths():
    assert sorted_list_sum(["aa", "bb", "aa", "cc"]) == ["aa", "aa", "bb", "cc"]

def test_duplicate_even_lengths_same_word():
    assert sorted_list_sum(["aa", "aa", "aa"]) == ["aa", "aa", "aa"]

def test_same_length_alphabetical():
    assert sorted_list_sum(["ab", "cd", "ac"]) == ["ab", "ac", "cd"]

def test_mixed_lengths_and_duplicates():
    assert sorted_list_sum(["ab", "a", "abc", "cd", "ab"]) == ["ab", "ab", "cd"]

def test_long_strings():
    assert sorted_list_sum(["abcdef", "abc", "defghi", "abcd"]) == ["abcd", "abcdef"]

def test_strings_with_spaces():
    assert sorted_list_sum(["aa bb", "a", "cc dd"]) == ["aa bb", "cc dd"]

def test_strings_with_special_characters():
    assert sorted_list_sum(["a!b", "c@d", "e#f"]) == ["a!b", "c@d", "e#f"]

def test_single_even_length_string():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_odd_length_string():
    assert sorted_list_sum(["a"]) == []

def test_edge_case_even_length_zero():
    assert sorted_list_sum([""]) == [""]

def test_edge_case_mixed_empty_string():
    assert sorted_list_sum(["", "a", "aa"]) == ["aa"]

def test_example_1():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_example_2():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]