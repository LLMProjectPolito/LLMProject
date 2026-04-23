
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
    result.sort(key=lambda s: (len(s), s))
    return result

class TestSortedListSum:
    def test_empty_list(self):
        assert sorted_list_sum([]) == []

    def test_list_with_even_length_strings(self):
        assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

    def test_list_with_odd_length_strings(self):
        assert sorted_list_sum(["a", "b", "c"]) == []

    def test_mixed_list(self):
        assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

    def test_mixed_list_2(self):
        assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

    def test_duplicates(self):
        assert sorted_list_sum(["aa", "aa", "bb"]) == ["aa", "aa", "bb"]

    def test_same_length_strings(self):
        assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

    def test_different_lengths_and_same_length(self):
        assert sorted_list_sum(["a", "aa", "b", "bb"]) == ["aa", "bb"]

    def test_longer_strings(self):
        assert sorted_list_sum(["hello", "world", "python"]) == []

    def test_mixed_case(self):
        assert sorted_list_sum(["Aa", "bb", "CC"]) == ["Aa", "bb", "CC"]

    def test_empty_string(self):
        assert sorted_list_sum([""]) == []

    def test_list_with_empty_string_and_other_strings(self):
        assert sorted_list_sum(["", "aa", "bb"]) == ["aa", "bb"]