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

def test_basic_case():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "abc", "def"]) == []

def test_all_even_lengths():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_duplicate_strings():
    assert sorted_list_sum(["aa", "aa", "a", "aaa"]) == ["aa", "aa"]

def test_same_length_strings():
    assert sorted_list_sum(["ab", "cd", "ac"]) == ["ab", "ac", "cd"]

def test_mixed_lengths_and_alphabetical_order():
    assert sorted_list_sum(["ab", "a", "aaa", "cd", "efg", "ce"]) == ["ab", "cd", "ce"]

def test_long_strings():
    assert sorted_list_sum(["abcdef", "abc", "abcdefgh", "a"]) == ["abcdef", "abcdefgh"]

def test_single_character_strings():
    assert sorted_list_sum(["a", "b", "c"]) == []

def test_mixed_case():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange"]) == ["apple", "banana", "orange"]

def test_with_empty_string():
    assert sorted_list_sum(["", "a", "aa"]) == ["aa"]