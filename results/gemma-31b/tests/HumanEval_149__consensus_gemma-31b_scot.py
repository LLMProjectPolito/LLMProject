
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

def test_sorted_list_sum_empty_list():
    """Test with an empty input list."""
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd():
    """Test where all strings have odd lengths."""
    assert sorted_list_sum(["a", "abc", "abcde", "123"]) == []

def test_sorted_list_sum_basic_filtering():
    """Test that odd length strings are removed and even length ones are kept."""
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_length_sorting():
    """Test that strings are sorted primarily by length (ascending)."""
    assert sorted_list_sum(["abcdef", "aa", "bbbb", "cc"]) == ["aa", "cc", "bbbb", "abcdef"]

def test_sorted_list_sum_alphabetical_order():
    """Test that strings of the same length are sorted alphabetically."""
    assert sorted_list_sum(["dc", "ba", "ca", "ad"]) == ["ad", "ba", "ca", "dc"]
    assert sorted_list_sum(["zz", "aa", "bb"]) == ["aa", "bb", "zz"]

def test_sorted_list_sum_combined_sorting():
    """Test both length and alphabetical sorting combined."""
    # "aa" (2), "bb" (2), "cccc" (4), "dddd" (4), "eeeeee" (6)
    input_list = ["dddd", "bb", "eeeeee", "aa", "cccc"]
    expected = ["aa", "bb", "cccc", "dddd", "eeeeee"]
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_complex_mix():
    """Test a mix of odd/even lengths, varying lengths, and alphabetical requirements."""
    # Evens: pear(4), banana(6), kiwi(4), plum(4), orange(6)
    # Sorted by length: [kiwi, pear, plum], [banana, orange]
    input_list = ["apple", "pear", "banana", "kiwi", "plum", "orange"]
    expected = ["kiwi", "pear", "plum", "banana", "orange"]
    assert sorted_list_sum(input_list) == expected

def test_sorted_list_sum_duplicates():
    """Test that duplicates are preserved and sorted correctly."""
    assert sorted_list_sum(["aa", "bb", "aa", "bb"]) == ["aa", "aa", "bb", "bb"]
    assert sorted_list_sum(["aaaa", "aa", "aa", "aaaa"]) == ["aa", "aa", "aaaa", "aaaa"]

def test_sorted_list_sum_case_sensitivity():
    """Test that sorting follows standard Python alphabetical (ASCII) order."""
    # 'B' comes before 'a' in ASCII
    assert sorted_list_sum(["ba", "Ba"]) == ["Ba", "ba"]
    assert sorted_list_sum(["Bb", "aa", "AA"]) == ["AA", "Bb", "aa"]

def test_sorted_list_sum_numeric_and_special_characters():
    """Test that strings containing numbers or symbols are handled as strings."""
    assert sorted_list_sum(["12", "1", "123", "10"]) == ["10", "12"]
    # ASCII: space(32), !(33), 1(49)
    assert sorted_list_sum(["12", "!!", "  "]) == ["  ", "!!", "12"]