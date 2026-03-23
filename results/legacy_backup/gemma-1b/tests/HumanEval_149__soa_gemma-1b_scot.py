import pytest

def list_sort(lst):
    """Sorts a list of strings based on length, ascending by length, and alphabetically for duplicates."""
    return sorted(lst, key=lambda x: (len(x), x))

def test_empty_list():
    assert list_sort([]) == []

def test_single_element():
    assert list_sort(["a"]) == ["a"]

def test_example_1():
    assert list_sort(["aa", "a", "aaa"]) == ["aa"]

def test_example_2():
    assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_example_3():
    assert list_sort(["abc", "ab", "a"]) == ["a", "ab", "abc"]

def test_duplicates():
    assert list_sort(["aa", "a", "aaa", "aa"]) == ["aa", "a", "aa", "aaa"]

def test_same_length_duplicates():
    assert list_sort(["ab", "a", "aba", "aa"]) == ["a", "ab", "aba", "aa"]