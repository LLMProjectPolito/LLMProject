
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
    """Test with an empty list."""
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    """Test where all strings have odd lengths."""
    assert sorted_list_sum(["a", "aaa", "abcde", "z"]) == []
    assert sorted_list_sum(["hello", "world", "pythonic"]) == []

def test_all_even_lengths_same_size():
    """Test where all strings have the same even length (checks alphabetical sort)."""
    assert sorted_list_sum(["cc", "aa", "bb"]) == ["aa", "bb", "cc"]
    assert sorted_list_sum(["dc", "ba", "ca", "ad"]) == ["ad", "ba", "ca", "dc"]
    assert sorted_list_sum(["zzzz", "aaaa", "bbbb"]) == ["aaaa", "bbbb", "zzzz"]

def test_all_even_lengths_different_size():
    """Test where strings have different even lengths (checks length sort)."""
    assert sorted_list_sum(["abcd", "ab", "abcdef", "ef"]) == ["ab", "ef", "abcd", "abcdef"]
    assert sorted_list_sum(["abcdefgh", "ab", "abcd"]) == ["ab", "abcd", "abcdefgh"]

def test_mixed_lengths_filtering():
    """Test filtering out odd lengths and keeping even lengths."""
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_complex_sorting():
    """Test sorting by length first, then alphabetically."""
    # Case 1: banana(6), apple(5), cherry(6), date(4), fig(3)
    # Evens: date(4), banana(6), cherry(6)
    assert sorted_list_sum(["banana", "apple", "cherry", "date", "fig"]) == ["date", "banana", "cherry"]
    
    # Case 2: apple(5), pear(4), banana(6), kiwi(4), plum(4), orange(6), fig(3)
    # Evens: kiwi(4), pear(4), plum(4), banana(6), orange(6)
    input_list = ["apple", "pear", "banana", "kiwi", "plum", "orange", "fig"]
    expected = ["kiwi", "pear", "plum", "banana", "orange"]
    assert sorted_list_sum(input_list) == expected

def test_duplicates():
    """Test that duplicate strings are preserved and sorted."""
    assert sorted_list_sum(["aa", "aa", "b", "bb"]) == ["aa", "aa", "bb"]
    assert sorted_list_sum(["aa", "bb", "aa", "b", "ccc"]) == ["aa", "aa", "bb"]

def test_case_sensitivity():
    """Test alphabetical sorting with mixed cases (ASCII order: Uppercase before Lowercase)."""
    assert sorted_list_sum(["bb", "AA", "aa"]) == ["AA", "aa", "bb"]
    assert sorted_list_sum(["aa", "Ba"]) == ["Ba", "aa"]
    assert sorted_list_sum(["aa", "Aa"]) == ["Aa", "aa"]

def test_single_element():
    """Test lists with a single element."""
    assert sorted_list_sum(["test"]) == ["test"]
    assert sorted_list_sum(["tes"]) == []

@pytest.mark.parametrize("input_lst, expected", [
    (["", "a", "bb", "ccc", "dddd"], ["", "bb", "dddd"]), # empty string is length 0 (even)
    (["ab", "cd", "ef"], ["ab", "cd", "ef"]),
    (["abc", "def", "ghi"], []),
    (["zz", "aa", "bb"], ["aa", "bb", "zz"]),
])
def test_sorted_list_sum_parametrized(input_lst, expected):
    """Parametrized tests for various edge cases."""
    assert sorted_list_sum(input_lst) == expected