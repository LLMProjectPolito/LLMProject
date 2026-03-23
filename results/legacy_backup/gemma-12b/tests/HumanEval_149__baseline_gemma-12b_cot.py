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

    def test_list_with_only_odd_length_strings(self):
        assert sorted_list_sum(["a", "bbb", "dddddddddd"]) == []

    def test_list_with_only_even_length_strings(self):
        assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

    def test_mixed_list(self):
        assert sorted_list_sum(["aa", "a", "aaa", "cd"]) == ["aa", "cd"]

    def test_list_with_duplicates(self):
        assert sorted_list_sum(["aa", "aa", "bb", "cc", "cc"]) == ["aa", "aa", "bb", "cc", "cc"]

    def test_list_with_same_length_strings(self):
        assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

    def test_list_with_same_length_strings_different_order(self):
        assert sorted_list_sum(["cd", "ab", "ef"]) == ["ab", "cd", "ef"]

    def test_list_with_same_length_strings_and_duplicates(self):
        assert sorted_list_sum(["ab", "ab", "cd", "ef"]) == ["ab", "ab", "cd", "ef"]

    def test_list_with_various_lengths(self):
        assert sorted_list_sum(["a", "aa", "aaa", "aaaa", "aaaaa"]) == ["aa", "aaaa"]

    def test_list_with_special_characters(self):
        assert sorted_list_sum(["!a", "!!", "!!!"]) == ["!a", "!!"]

    def test_list_with_numbers_as_strings(self):
        assert sorted_list_sum(["12", "1", "123"]) == ["12"]

    def test_list_with_empty_string(self):
        assert sorted_list_sum(["", "a", "aa"]) == ["", "aa"]

    def test_long_list(self):
        long_list = ["a" * i for i in range(1, 21)]
        expected = [s for i, s in enumerate(long_list) if i % 2 == 0]
        assert sorted_list_sum(long_list) == expected