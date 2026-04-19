
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

@pytest.mark.parametrize("input_list, expected", [
    ([], []),                                           # Empty list
    (["a", "aaa", "abcde", "fghij"], []),               # All odd lengths
    (["aa", "a", "aaa"], ["aa"]),                       # Basic example 1
    (["ab", "a", "aaa", "cd"], ["ab", "cd"]),           # Basic example 2
    (["", "a", "bb", "ccc", "dddd"], ["", "bb", "dddd"]), # Empty string (len 0) and mixed
    (["longword", "short", "medium", "tiny"], ["tiny", "medium", "longword"]), # Mixed parity/len
    (["apple", "banana", "cherry", "date", "egg"], ["date", "banana", "cherry"]), # Mixed parity/len
])
def test_sorted_list_sum_parametrized(input_list, expected):
    """Test various combinations of parity and length using parametrization."""
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_sorting_criteria():
    """Test that sorting is primarily by length (ascending) and secondarily alphabetical."""
    # Same length, different alpha: "ad" < "ba" < "ca" < "dc"
    assert sorted_list_sum(["dc", "ba", "ca", "ad"]) == ["ad", "ba", "ca", "dc"]
    
    # Different lengths: 2, 4, 6
    assert sorted_list_sum(["abcdef", "abcd", "ab"]) == ["ab", "abcd", "abcdef"]
    
    # Mixed: length 2 ("aa", "ab"), length 4 ("abcd"), length 6 ("abcdef")
    assert sorted_list_sum(["abcdef", "ab", "abcd", "aa", "a"]) == ["aa", "ab", "abcd", "abcdef"]

def test_sorted_list_sum_duplicates():
    """Test that duplicate strings are preserved and sorted correctly."""
    assert sorted_list_sum(["aa", "bb", "aa", "b"]) == ["aa", "aa", "bb"]
    assert sorted_list_sum(["abcd", "aa", "abcd", "aa"]) == ["aa", "aa", "abcd", "abcd"]
    assert sorted_list_sum(["bb", "aa", "bb", "aa"]) == ["aa", "aa", "bb", "bb"]

def test_sorted_list_sum_case_sensitivity():
    """Test alphabetical sorting with mixed casing (ASCII order: Upper < Lower)."""
    # All length 2. ASCII: 'A'(65), 'B'(66), 'a'(97), 'b'(98)
    assert sorted_list_sum(["bb", "AA", "aa"]) == ["AA", "aa", "bb"]
    assert sorted_list_sum(["bb", "AA", "bb", "BB", "aa"]) == ["AA", "BB", "aa", "bb", "bb"]

def test_sorted_list_sum_special_characters():
    """Test with strings containing numbers or symbols."""
    # "!!"(2), "12"(2), "!!!"(3)
    # "!!" comes before "12" in ASCII
    assert sorted_list_sum(["12", "!!", "!!!"]) == ["!!", "12"]

def test_sorted_list_sum_large_strings():
    """Test with very long strings to ensure length sorting works at scale."""
    s_short = "a" * 10
    s_med = "b" * 20
    s_long = "c" * 30
    assert sorted_list_sum([s_long, s_med, s_short]) == [s_short, s_med, s_long]