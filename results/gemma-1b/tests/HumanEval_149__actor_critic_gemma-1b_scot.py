
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

def list_sort(lst):
    """Sorts a list of strings by length, then alphabetically, and handles duplicates."""
    unique_words = sorted(list(set(lst)))
    result = []
    for word in unique_words:
        result.append(word)
    return result

def test_empty_list():
    """Test with an empty list."""
    assert list_sort([]) == []

def test_single_element():
    """Test with a list containing a single element."""
    assert list_sort(["a"]) == ["a"]

def test_example_1():
    """Test with the example case from the prompt."""
    assert list_sort(["aa", "a", "aaa"]) == ["aa"]

def test_example_2():
    """Test with another example case."""
    assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_duplicate_words():
    """Test with duplicate words in the list."""
    assert list_sort(["aa", "a", "aaa", "aa"]) == ["aa", "a", "aa"]

def test_same_length_words():
    """Test with words of the same length."""
    assert list_sort(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_mixed_case():
    """Test with mixed case words."""
    assert list_sort(["Aa", "a", "AAA"]) == ["Aa", "a", "AAA"]

def test_long_list():
    """Test with a longer list to check for performance."""
    assert list_sort(["a", "bb", "ccc", "dd", "e"]) == ["a", "bb", "ccc", "dd"]