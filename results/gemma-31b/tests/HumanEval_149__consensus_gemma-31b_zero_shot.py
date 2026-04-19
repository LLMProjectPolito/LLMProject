
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
    """Test basic functionality with mixed odd and even lengths."""
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_empty():
    """Test with an empty list."""
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd():
    """Test when all strings have odd lengths."""
    assert sorted_list_sum(["a", "aaa", "abcde", "fghij"]) == []

def test_sorted_list_sum_all_even_same_length():
    """Test when all strings have the same even length, checking alphabetical sort."""
    assert sorted_list_sum(["cc", "aa", "bb"]) == ["aa", "bb", "cc"]
    assert sorted_list_sum(["zz", "aa", "bb"]) == ["aa", "bb", "zz"]

def test_sorted_list_sum_different_even_lengths():
    """Test when strings have different even lengths, checking length-based sort."""
    assert sorted_list_sum(["aaaa", "aa", "bbbbbb", "bb"]) == ["aa", "bb", "aaaa", "bbbbbb"]

def test_sorted_list_sum_mixed_criteria():
    """Test combination of length sorting and alphabetical sorting."""
    # "aa" and "bb" are length 2 (alphabetical), "cccc" is length 4
    assert sorted_list_sum(["cccc", "bb", "aa", "a", "bbb"]) == ["aa", "bb", "cccc"]
    # "ab" and "aa" are length 2 (alphabetical), "dddd" is length 4
    assert sorted_list_sum(["dddd", "ab", "aa"]) == ["aa", "ab", "dddd"]

def test_sorted_list_sum_duplicates():
    """Test that duplicates are handled and preserved."""
    assert sorted_list_sum(["aa", "aa", "bb", "bb"]) == ["aa", "aa", "bb", "bb"]
    assert sorted_list_sum(["aa", "a", "aa"]) == ["aa", "aa"]
    assert sorted_list_sum(["aa", "aa", "b", "bb", "aa"]) == ["aa", "aa", "aa", "bb"]

def test_sorted_list_sum_case_sensitivity():
    """Test that sorting follows standard Python string comparison (ASCII)."""
    # 'A' < 'a'
    assert sorted_list_sum(["aa", "AA"]) == ["AA", "aa"]
    # ASCII: A=65, B=66, a=97, b=98
    assert sorted_list_sum(["Bb", "Aa", "aa", "BB"]) == ["Aa", "BB", "Bb", "aa"]

def test_sorted_list_sum_special_characters():
    """Test strings with spaces and special characters."""
    # "  " (len 2, space=32), "!!" (len 2, !=33)
    assert sorted_list_sum(["!!", "!!!", "  ", " a "]) == ["  ", "!!"]

def test_sorted_list_sum_complex_scenario():
    """Comprehensive test for all rules."""
    input_data = ["banana", "apple", "pear", "kiwi", "plum", "orange", "fig"]
    # Lengths: banana(6), apple(5), pear(4), kiwi(4), plum(4), orange(6), fig(3)
    # Even lengths: banana, pear, kiwi, plum, orange
    # Sort by length:
    # Len 4: kiwi, pear, plum (alphabetical: k < pe < pl)
    # Len 6: banana, orange (alphabetical: b < o)
    assert sorted_list_sum(input_data) == ["kiwi", "pear", "plum", "banana", "orange"]

@pytest.mark.parametrize("input_lst, expected", [
    (["a", "b", "c"], []),
    (["aa", "bb", "cc"], ["aa", "bb", "cc"]),
    (["zz", "aa"], ["aa", "zz"]),
    (["abcd", "ab"], ["ab", "abcd"]),
    (["", "a"], [""]), # Empty string has length 0, which is even
    (["", ""], ["", ""]),
])
def test_sorted_list_sum_parametrized(input_lst, expected):
    assert sorted_list_sum(input_lst) == expected