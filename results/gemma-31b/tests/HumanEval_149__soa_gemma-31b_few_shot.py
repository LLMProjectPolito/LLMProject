
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

def test_sorted_list_sum_basic():
    """Test basic functionality with provided examples."""
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_empty():
    """Test with an empty list."""
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd():
    """Test where all strings have odd lengths."""
    assert sorted_list_sum(["a", "aaa", "abcde", "123"]) == []

def test_sorted_list_sum_all_even():
    """Test where all strings have even lengths."""
    # Lengths: 2, 4, 2. Sorted by length then alpha: "aa" (2), "bb" (2), "cccc" (4)
    assert sorted_list_sum(["cccc", "aa", "bb"]) == ["aa", "bb", "cccc"]

def test_sorted_list_sum_sorting_logic():
    """Test complex sorting: length first, then alphabetical."""
    # "abcd" (4), "ab" (2), "zz" (2), "abcdef" (6), "aa" (2)
    # Even lengths: "abcd", "ab", "zz", "abcdef", "aa"
    # Sorted by length: ["ab", "zz", "aa"] (len 2), ["abcd"] (len 4), ["abcdef"] (len 6)
    # Sorted by alpha within length 2: ["aa", "ab", "zz"]
    input_list = ["abcd", "ab", "zz", "abcdef", "aa"]
    expected = ["aa", "ab", "zz", "abcd", "abcdef"]
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_duplicates():
    """Test handling of duplicate strings."""
    assert sorted_list_sum(["aa", "aa", "bb", "bb", "a"]) == ["aa", "aa", "bb", "bb"]

def test_sorted_list_sum_case_sensitivity():
    """Test that alphabetical sorting respects case (ASCII order)."""
    # 'A' comes before 'a'
    assert sorted_list_sum(["aa", "Aa"]) == ["Aa", "aa"]

def test_sorted_list_sum_special_chars():
    """Test strings with spaces and special characters."""
    # "  " (len 2), "!!!" (len 3), "@@" (len 2)
    assert sorted_list_sum(["  ", "!!!", "@@"]) == ["  ", "@@"]

@pytest.mark.parametrize("input_lst, expected", [
    (["apple", "pear", "banana", "kiwi"], ["kiwi", "pear", "banana"]), # pear(4), kiwi(4), banana(6) -> kiwi, pear, banana
    (["", "a", "bb", "ccc", "dddd"], ["", "bb", "dddd"]), # empty string len 0 is even
    (["12", "1", "123", "1234"], ["12", "1234"]),
])
def test_sorted_list_sum_parametrized(input_lst, expected):
    """Parametrized tests for various edge cases."""
    assert sorted_list_sum(input_lst) == expected