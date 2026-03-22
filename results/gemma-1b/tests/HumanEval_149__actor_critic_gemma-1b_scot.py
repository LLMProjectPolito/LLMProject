import pytest

def list_sort(lst):
    """Sorts a list of strings by length, then alphabetically, and removes strings with odd lengths."""
    filtered_list = [s for s in lst if len(s) % 2 == 0]
    filtered_list.sort(key=lambda x: (len(x), x))
    return filtered_list

def test_empty_list():
    assert list_sort([]) == []

def test_single_element():
    assert list_sort(["a"]) == ["a"]

def test_even_length_strings():
    assert list_sort(["aa", "a", "aaa"]) == ["aa"]

def test_odd_length_strings():
    assert list_sort(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_duplicate_strings():
    assert list_sort(["aa", "a", "aaa", "aa"]) == ["aa", "aa", "a", "aaa"]

def test_mixed_length_strings():
    assert list_sort(["ab", "a", "aaa", "cd", "aa"]) == ["aa", "ab", "a", "cd", "aaa"]

def test_long_list():
    assert list_sort(["aa", "aaa", "aaaa", "aaaaa"]) == ["aa", "aaa", "aaaa", "aaaaa"]

def test_list_with_duplicates():
    assert list_sort(["aa", "a", "aaa", "aa"]) == ["aa", "aa", "a", "aaa"]