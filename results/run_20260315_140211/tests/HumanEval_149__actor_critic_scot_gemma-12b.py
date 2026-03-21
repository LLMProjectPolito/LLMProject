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

    def test_mixed_even_and_odd_lengths(self):
        assert sorted_list_sum(["aa", "a", "aaa", "bb", "c"]) == ["aa", "bb"]

    def test_duplicates(self):
        assert sorted_list_sum(["aa", "a", "aa", "bbb", "bb", "ccc", "bb"]) == ["aa", "aa", "bb", "bb"]

    def test_same_length(self):
        assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

    def test_same_length_case_sensitive(self):
        assert sorted_list_sum(["Ab", "ab"]) == ["Ab", "ab"]

    def test_same_length_different_casing(self):
        assert sorted_list_sum(["Ab", "ab", "aB", "ba"]) == ["Ab", "aB", "ab", "ba"]

    def test_unicode_strings(self):
        assert sorted_list_sum(["你好", "世界", "a", "aa"]) == ["aa", "你好", "世界"]

    def test_strings_with_spaces(self):
        assert sorted_list_sum(["a b", "aa", " c "]) == ["aa", "a b", " c "]

    def test_empty_strings(self):
        """
        Test with empty strings. Empty strings should be included in the result
        and sorted based on their length (0) and alphabetically.
        """
        assert sorted_list_sum(["", "aa", "a"]) == [""]

    def test_large_list(self):
        large_list = ["a" * i for i in range(1, 1001)]
        even_length_strings = [s for s in large_list if len(s) % 2 == 0]
        expected_result = sorted(even_length_strings, key=lambda s: (len(s), s))
        assert sorted_list_sum(large_list) == expected_result