import pytest

def list_sort(lst):
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
    new_lst = []
    for s in lst:
        if len(s) % 2 == 0:
            new_lst.append(s)
        else:
            new_lst.append(s)
    new_lst.sort(key=lambda x: (len(x), x))
    return new_lst

def test_list_sort():
    assert list_sort(["aa", "a", "aaa"]) == ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert list_sort(["abc", "ab", "a"]) == ["a", "ab", "abc"]
    assert list_sort(["a", "aa", "aaa"]) == ["a", "aa", "aaa"]
    assert list_sort([]) == []
    assert list_sort([""]) == [""]