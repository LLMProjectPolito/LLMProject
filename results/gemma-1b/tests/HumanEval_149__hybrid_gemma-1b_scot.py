
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
    result.sort(key=lambda x: (len(x), x))
    return result

def test_empty_list():
    assert list_sort([]) == []

def test_single_element():
    assert list_sort(["a"]) == ["a"]

def test_example_1():
    assert list_sort(["aa", "a", "aaa"]) == ["aa"]

def test_example_2():
    assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_duplicate_words():
    assert list_sort(["aa", "a", "aaa", "aa"]) == ["aa", "aa", "a", "aaa"]

def test_same_length_words():
    assert list_sort(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_mixed_lengths():
    assert list_sort(["abc", "ab", "a", "abcd"]) == ["a", "ab", "abc", "abcd"]

def test_long_list():
    assert list_sort(["a", "bb", "ccc", "dd", "e"]) == ["a", "bb", "ccc", "dd"]

def test_empty_list_with_duplicates():
    assert list_sort(["aa", "a", "aaa", "aa"]) == ["aa", "aa", "a", "aaa"]

def test_single_element_with_duplicates():
    assert list_sort(["a"]) == ["a"]

def test_example_3():
    assert list_sort(["aaa", "aa", "a"]) == ["a", "aa", "aaa"]

def test_example_4():
    assert list_sort(["ab", "a", "abc"]) == ["a", "ab", "abc"]

def test_example_5():
    assert list_sort(["a", "b", "c"]) == ["a", "b", "c"]