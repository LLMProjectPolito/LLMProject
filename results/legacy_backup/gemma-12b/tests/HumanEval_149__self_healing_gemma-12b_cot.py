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

def test_list_with_only_odd_length_strings():
    assert sorted_list_sum(["a", "bc", "def"]) == []

def test_list_with_only_even_length_strings():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_even_and_odd_length_strings():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "c"]) == ["aa", "bb"]

def test_duplicate_strings():
    assert sorted_list_sum(["aa", "aa", "a", "aaa"]) == ["aa", "aa"]

def test_strings_with_same_length():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_strings_with_same_length_and_different_alphabetical_order():
    assert sorted_list_sum(["cd", "ab", "ef"]) == ["ab", "cd", "ef"]

def test_complex_list():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "c", "cc", "ddd", "ee"]) == ["aa", "bb", "cc", "ee"]

def test_list_with_empty_string():
    assert sorted_list_sum(["", "a", "aa"]) == ["", "aa"]

def test_list_with_special_characters():
    assert sorted_list_sum(["!a", "!!", "!!!"]) == ["!a", "!!"]