
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
    """ Sorts a list of strings by length of each word, and returns the sorted list. """
    return sorted(lst, key=lambda x: (len(x), x))

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """

def test_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_max_empty():
    assert get_max([]) == None

def test_list_sort_positive():
    assert list_sort(["aa", "a", "aaa"]) == ["aa"]

def test_list_sort_empty():
    assert list_sort([]) == []

def test_list_sort_single_element():
    assert list_sort(["hello"]) == ["hello"]

def test_list_sort_duplicate_elements():
    assert list_sort(["aa", "a", "aaa"]) == ["aa", "a", "aaa"]

def test_list_sort_mixed_lengths():
    assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_list_sort_same_length_words():
    assert list_sort(["aa", "a", "aaa"]) == ["aa", "a", "aaa"]

def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True