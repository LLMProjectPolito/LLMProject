
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

class TestSortedListSum:
    def test_empty_list(self):
        assert sorted_list_sum([]) == []

    def test_all_odd_length(self):
        assert sorted_list_sum(["a", "bbb", "dddddddd"]) == []

    def test_all_even_length(self):
        assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

    def test_mixed_lengths(self):
        assert sorted_list_sum(["aa", "a", "aaa", "cd"]) == ["aa", "cd"]

    def test_mixed_lengths_with_duplicates(self):
        assert sorted_list_sum(["aa", "a", "aaa", "cd", "aa"]) == ["aa", "aa", "cd"]

    def test_same_length_different_alphabetical(self):
        assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

    def test_same_length_same_alphabetical(self):
        assert sorted_list_sum(["ab", "ab", "cd"]) == ["ab", "ab", "cd"]

    def test_complex_case(self):
        assert sorted_list_sum(["abc", "ab", "a", "abcd", "abcde", "abcdef"]) == ["ab", "abc", "abcd"]

    def test_unicode_strings(self):
        assert sorted_list_sum(["你好", "世界", "你好世界"]) == ["你好", "世界", "你好世界"]

    def test_strings_with_spaces(self):
        assert sorted_list_sum(["a b", "c", "d e f"]) == ["a b"]

    def test_long_strings(self):
        long_string1 = "a" * 100
        long_string2 = "b" * 50
        assert sorted_list_sum([long_string1, long_string2]) == [long_string2]

    def test_edge_case_one_element(self):
        assert sorted_list_sum(["aa"]) == ["aa"]

    def test_edge_case_one_odd_element(self):
        assert sorted_list_sum(["a"]) == []

    def test_duplicates(self):
        assert sorted_list_sum(["aa", "aa", "bb", "cc", "cc"]) == ["aa", "aa", "bb", "cc", "cc"]

    def test_single_even_string(self):
        assert sorted_list_sum(["aa"]) == ["aa"]

    def test_single_odd_string(self):
        assert sorted_list_sum(["a"]) == []

    def test_mixed_case_alphabetical(self):
        assert sorted_list_sum(["Aa", "aa", "BB", "bb"]) == ["Aa", "aa", "BB", "bb"]