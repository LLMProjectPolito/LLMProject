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
        assert sorted_list_sum(["a", "bbb", "ccccc"]) == []

    def test_all_even_length(self):
        assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

    def test_mixed_lengths(self):
        assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

    def test_mixed_lengths_with_duplicates(self):
        assert sorted_list_sum(["ab", "a", "aaa", "cd", "ab"]) == ["ab", "ab", "cd"]

    def test_same_length_different_alphabetical(self):
        assert sorted_list_sum(["bc", "ab", "cd"]) == ["ab", "bc", "cd"]

    def test_same_length_same_alphabetical(self):
        assert sorted_list_sum(["ab", "ab", "cd", "cd"]) == ["ab", "ab", "cd", "cd"]

    def test_complex_case(self):
        assert sorted_list_sum(["aa", "a", "aaa", "bb", "bbb", "cc", "c", "dd", "ddd", "ee", "eee"]) == ["aa", "bb", "cc", "dd", "ee"]

    def test_single_element_even(self):
        assert sorted_list_sum(["aa"]) == ["aa"]

    def test_single_element_odd(self):
        assert sorted_list_sum(["a"]) == []

    def test_long_strings(self):
        assert sorted_list_sum(["abcdef", "abcde", "abcdefg"]) == ["abcdef"]