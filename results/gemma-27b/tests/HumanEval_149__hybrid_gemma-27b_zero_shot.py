
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

    def test_all_odd_lengths(self):
        assert sorted_list_sum(["a", "aaa", "abcde"]) == []

    def test_all_even_lengths(self):
        assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

    def test_mixed_lengths(self):
        assert sorted_list_sum(["aa", "a", "aaa", "bb"]) == ["aa", "bb"]

    def test_mixed_lengths_with_duplicates(self):
        assert sorted_list_sum(["aa", "a", "aaa", "bb", "aa"]) == ["aa", "aa", "bb"]

    def test_same_length_alphabetical(self):
        assert sorted_list_sum(["ab", "ac", "aa"]) == ["aa", "ab", "ac"]

    def test_longer_strings(self):
        assert sorted_list_sum(["abcdef", "abc", "abcd", "abcde"]) == ["abcd"]

    def test_complex_case(self):
        assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape"]) == ["kiwi", "grape"]

    def test_case_sensitivity(self):
        assert sorted_list_sum(["AA", "aa", "Bb", "bb"]) == ["AA", "aa", "Bb", "bb"]

    def test_numbers_as_strings(self):
        assert sorted_list_sum(["12", "1", "123", "1234"]) == ["12", "1234"]

    def test_special_characters(self):
        assert sorted_list_sum(["!@#$", "abc", "!@"]) == ["!@#$"]

    def test_empty_string(self):
        assert sorted_list_sum(["", "a", "aa"]) == ["aa"]

    def test_only_empty_string(self):
        assert sorted_list_sum([""]) == []

    def test_multiple_empty_strings(self):
        assert sorted_list_sum(["", "", "aa", "bb"]) == ["aa", "bb"]

    def test_long_list(self):
        long_list = [str(i) for i in range(100)]
        expected_result = [s for s in long_list if len(s) % 2 == 0]
        expected_result.sort(key=lambda s: (len(s), s))
        assert sorted_list_sum(long_list) == expected_result

    def test_strings_with_spaces(self):
        assert sorted_list_sum(["aa bb", "a", "aaa", "bb cc"]) == ["aa bb", "bb cc"]

    def test_strings_with_special_characters(self):
        assert sorted_list_sum(["a!", "aa", "aaa", "bb@"]) == ["aa", "bb@"]

    def test_large_list(self):
        large_list = ["a" * i for i in range(1, 21)]
        expected_result = ["a" * i for i in range(2, 21, 2)]
        assert sorted_list_sum(large_list) == expected_result

    def test_list_with_empty_string(self):
        assert sorted_list_sum(["", "a", "aa"]) == ["aa"]

    def test_list_with_only_empty_string(self):
        assert sorted_list_sum([""]) == []