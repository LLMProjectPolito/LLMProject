import pytest

def is_palindrome(s: str) -> bool:
    """ Checks if a string is a palindrome """
    s = s.lower()
    return s == s[::-1]

def get_max(arr: list[int]) -> int:
    """ Returns the maximum element in a list, or None if empty """
    if not arr:
        return None
    return max(arr)

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
    new_list = [s for s in lst if len(s) % 2 == 0]
    new_list.sort(key=lambda x: (len(x), x))
    return new_list

def test_is_palindrome_basic():
    assert is_palindrome('radar') == True
    assert is_palindrome('hello') == False

def test_is_palindrome_empty():
    assert is_palindrome('') == True

def test_get_max_positive():
    assert get_max([1, 2, 3]) == 3

def test_get_max_empty():
    assert get_max([]) == None

def test_sorted_list_sum_basic():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_sorted_list_sum_example1():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "ab", "aa", "cd"]) == ["aa", "aa", "ab", "cd"]

def test_sorted_list_sum_same_length():
    assert sorted_list_sum(["abc", "def", "ghi"]) == ["abc", "def", "ghi"]

def test_sorted_list_sum_mixed():
    assert sorted_list_sum(["a", "aa", "b", "bb", "c", "cc"]) == ["a", "b", "c"]

def test_sorted_list_sum_long():
    assert sorted_list_sum(["apple", "banana", "orange", "grape"]) == ["apple", "banana", "orange", "grape"]