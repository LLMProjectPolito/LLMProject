
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
    from main import sorted_list_sum
    assert sorted_list_sum([]) == []

def test_list_with_only_odd_length_strings():
    from main import sorted_list_sum
    assert sorted_list_sum(["a", "bc", "def"]) == []

def test_list_with_only_even_length_strings():
    from main import sorted_list_sum
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_list_odd_and_even():
    from main import sorted_list_sum
    assert sorted_list_sum(["a", "aa", "aaa", "bb", "ccc"]) == ["aa", "bb"]

def test_list_with_duplicates():
    from main import sorted_list_sum
    assert sorted_list_sum(["aa", "aa", "a", "bb", "bb", "ccc"]) == ["aa", "aa", "bb", "bb"]

def test_list_with_same_length_strings():
    from main import sorted_list_sum
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_list_with_same_length_strings_and_duplicates():
    from main import sorted_list_sum
    assert sorted_list_sum(["ab", "cd", "ab", "ef", "cd"]) == ["ab", "ab", "cd", "cd", "ef"]

def test_list_with_different_lengths_and_duplicates():
    from main import sorted_list_sum
    assert sorted_list_sum(["a", "aa", "a", "bb", "aa", "ccc"]) == ["aa", "aa", "bb"]

def test_list_with_long_strings():
    from main import sorted_list_sum
    assert sorted_list_sum(["abcdef", "abc", "ab", "a"]) == ["ab", "abc"]

def test_list_with_special_characters():
    from main import sorted_list_sum
    assert sorted_list_sum(["a!", "aa?", "aaa#"]) == ["aa?"]

def test_list_with_numbers_as_strings():
    from main import sorted_list_sum
    assert sorted_list_sum(["1", "12", "123"]) == ["12"]

def test_list_with_mixed_characters():
    from main import sorted_list_sum
    assert sorted_list_sum(["a1", "a", "aa"]) == ["aa"]

def test_list_with_empty_string():
    from main import sorted_list_sum
    assert sorted_list_sum(["", "a", "aa"]) == ["aa"]

def test_list_with_all_same_length_and_alphabetical_order():
    from main import sorted_list_sum
    assert sorted_list_sum(["abc", "abd", "abe"]) == ["abc", "abd", "abe"]

def test_list_with_all_same_length_and_duplicates_alphabetical_order():
    from main import sorted_list_sum
    assert sorted_list_sum(["abc", "abc", "abd"]) == ["abc", "abc", "abd"]