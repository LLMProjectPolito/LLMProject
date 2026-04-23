
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
    result = [s for s in lst if len(s) % 2 == 0]
    result.sort(key=lambda x: (len(x), x))
    return result

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_even_length():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_all_odd_length():
    assert sorted_list_sum(["a", "c", "e"]) == []

def test_mixed_even_odd():
    assert sorted_list_sum(["aa", "a", "aaa", "cd"]) == ["aa", "cd"]

def test_duplicate_strings():
    assert sorted_list_sum(["aa", "a", "aaa", "aa", "cd"]) == ["aa", "aa", "cd"]

def test_single_string():
    assert sorted_list_sum(["a"]) == []

def test_longer_strings():
    assert sorted_list_sum(["abcdef", "abc", "defgh"]) == ["abcdef", "defgh"]

def test_strings_with_spaces():
    assert sorted_list_sum(["hello world", "hello", "world"]) == ["hello world", "world"]

def test_empty_string():
    assert sorted_list_sum(["", "a", "aa"]) == ["aa"]

def test_complex_list():
    assert sorted_list_sum(["ab", "cd", "ef", "gh", "ij", "kl"]) == ["ab", "cd", "ef", "gh", "ij", "kl"]

def test_large_list():
    large_list = ["aa", "a", "aaa", "ab", "cd", "ef", "gh", "ij", "kl", "mn", "op", "qr", "st", "uv", "wx", "yz"]
    expected = ["aa", "ab", "cd", "ef", "gh", "ij", "kl", "mn", "op", "qr", "st", "uv", "wx", "yz"]
    assert sorted_list_sum(large_list) == expected

def test_strings_with_special_characters():
    assert sorted_list_sum(["!@#", "$%^", "&*()"]) == ["!@#", "$%^", "&*()"]

def test_long_strings_same_length():
    assert sorted_list_sum(["abcdefgh", "ijklmnop", "qrstuvw"]) == ["abcdefgh", "ijklmnop", "qrstuvw"]