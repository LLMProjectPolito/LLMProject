
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
        assert sorted_list_sum(["a", "aaa", "abc"]) == []

    def test_all_even_lengths(self):
        assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

    def test_mixed_lengths(self):
        assert sorted_list_sum(["aa", "a", "aaa", "bb"]) == ["aa", "bb"]

    def test_mixed_lengths_with_duplicates(self):
        assert sorted_list_sum(["aa", "a", "aaa", "bb", "aa"]) == ["aa", "aa", "bb"]

    def test_same_length_alphabetical(self):
        assert sorted_list_sum(["ab", "ac", "aa"]) == ["aa", "ab", "ac"]

    def test_longer_strings(self):
        assert sorted_list_sum(["abcd", "abc", "ab", "a"]) == ["ab", "abcd"]

    def test_longer_strings_with_duplicates(self):
        assert sorted_list_sum(["abcd", "abc", "ab", "a", "abcd"]) == ["ab", "abcd", "abcd"]

    def test_edge_case_empty_string(self):
        assert sorted_list_sum(["", "a", "aa"]) == ["aa"]

    def test_edge_case_empty_string_and_even(self):
        assert sorted_list_sum(["", "aa", "bb"]) == ["", "aa", "bb"]

    def test_complex_case(self):
        assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape"]) == ["kiwi", "grape"]

    def test_complex_case_with_duplicates(self):
        assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape", "kiwi"]) == ["kiwi", "kiwi", "grape"]

    def test_all_same_even_length_alphabetical(self):
        assert sorted_list_sum(["cb", "ba", "ac"]) == ["ac", "ba", "cb"]

    def test_numbers_as_strings(self):
        assert sorted_list_sum(["12", "1", "123", "124"]) == ["12", "124"]

    def test_example_1(self):
        assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

    def test_example_2(self):
        assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

    def test_longer_strings(self):
        assert sorted_list_sum(["abcdef", "abc", "defgh", "a"]) == ["abcdef", "defgh"]

    def test_strings_with_spaces(self):
        assert sorted_list_sum(["aa bb", "a", "ccc dd"]) == ["aa bb"]

    def test_strings_with_special_characters(self):
        assert sorted_list_sum(["a!", "bb@", "c#d"]) == ["bb@"]

    def test_large_list(self):
        large_list = [str(i) * (i % 2 + 1) for i in range(100)]
        expected_result = [s for s in large_list if len(s) % 2 == 0]
        expected_result.sort(key=lambda s: (len(s), s))
        assert sorted_list_sum(large_list) == expected_result