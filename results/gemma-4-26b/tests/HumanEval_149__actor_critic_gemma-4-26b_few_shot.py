
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

# Note: The function name has been changed from 'sorted_list_sum' 
# to 'filter_even_and_sort' to resolve the misleading naming issue.

def test_filter_even_and_sort_empty_list():
    """Tests that an empty list returns an empty list."""
    assert filter_even_and_sort([]) == []

def test_filter_even_and_sort_all_odd():
    """Tests that if all strings have odd lengths, an empty list is returned."""
    assert filter_even_and_sort(["a", "abc", "abcde", "abcde"]) == []

def test_filter_even_and_sort_all_even():
    """Tests that if all strings are even, they are sorted by length then alphabetically."""
    # All length 2: alphabetical order should be 'ab', 'ba', 'cd'
    assert filter_even_and_sort(["cd", "ab", "ba"]) == ["ab", "ba", "cd"]
    # Mixed even lengths: length 2 then length 4
    assert filter_even_and_sort(["zz", "aaaa", "bb", "cccc"]) == ["bb", "zz", "aaaa", "cccc"]

def test_filter_even_and_sort_duplicates():
    """Tests that duplicates are preserved and sorted correctly."""
    assert filter_even_and_sort(["aa", "bb", "a", "aa"]) == ["aa", "aa", "bb"]

def test_filter_even_and_sort_empty_strings():
    """
    Tests that empty strings (length 0) are treated as even and 
    sorted to the front of the list.
    """
    assert filter_even_and_sort(["a", "", "bb", ""]) == ["", "", "bb"]

def test_filter_even_and_sort_case_sensitivity():
    """
    Tests how the function handles mixed-case strings.
    Verifies if sorting follows standard ASCII/Unicode order (Uppercase before Lowercase).
    """
    # Length 2 strings: "Aa", "BB", "aa", "bb"
    # ASCII order: A (65), B (66), a (97), b (98)
    input_list = ["aa", "Aa", "bb", "BB"]
    expected = ["Aa", "BB", "aa", "bb"]
    assert filter_even_and_sort(input_list) == expected

def test_filter_even_and_sort_complex_sorting():
    """Tests complex scenario: multiple lengths and multiple ties in alphabetical order."""
    input_list = ["apple", "pear", "kiwi", "banana", "egg", "fig", "ace", "de", "ba"]
    # Even lengths: pear(4), kiwi(4), banana(6), de(2), ba(2)
    # Sort by length: [de, ba] (len 2), [pear, kiwi] (len 4), [banana] (len 6)
    # Sort alphabetically within length: [ba, de], [kiwi, pear], [banana]
    expected = ["ba", "de", "kiwi", "pear", "banana"]
    assert filter_even_and_sort(input_list) == expected

def test_filter_even_and_sort_single_element_edge_cases():
    """Tests the filtering logic at the smallest possible scale (single elements)."""
    # Single even-length string
    assert filter_even_and_sort(["aa"]) == ["aa"]
    # Single odd-length string
    assert filter_even_and_sort(["a"]) == []

def test_filter_even_and_sort_special_characters_and_numbers():
    """Tests that strings containing numbers and symbols are sorted via ASCII/Unicode order."""
    # "12" (len 2), "!@" (len 2), "a1" (len 2)
    # ASCII: '!' (33), '1' (49), 'a' (97)
    input_list = ["a1", "12", "!@"]
    expected = ["!@", "12", "a1"]
    assert filter_even_and_sort(input_list) == expected

def test_filter_even_and_sort_invalid_input_type():
    """Tests that passing a non-list input raises a TypeError."""
    with pytest.raises(TypeError):
        filter_even_and_sort(None)
    with pytest.raises(TypeError):
        filter_even_and_sort(123)
    with pytest.raises(TypeError):
        filter_even_and_sort("not a list")

def test_filter_even_and_sort_list_with_non_string_elements():
    """Tests that a list containing non-string elements raises a TypeError."""
    with pytest.raises(TypeError):
        filter_even_and_sort(["aa", 1, "bb"])
    with pytest.raises(TypeError):
        filter_even_and_sort(["aa", None, "bb"])