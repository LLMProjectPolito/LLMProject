
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
    If the input is not a list of strings, a TypeError is raised.
    For example:
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    """
    if not isinstance(lst, list):
        raise TypeError("Input must be a list.")
    for item in lst:
        if not isinstance(item, str):
            raise TypeError("Input must be a list of strings.")

    even_length_strings = [s for s in lst if len(s) % 2 == 0]
    even_length_strings.sort(key=lambda s: (len(s), s))
    return even_length_strings

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "abc", "def"]) == []

def test_mixed_lengths():
    assert sorted_list_sum(["aa", "a", "aaa", "bb"]) == ["aa", "bb"]

def test_mixed_lengths_with_duplicates():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "aa"]) == ["aa", "aa", "bb"]

def test_same_length_alphabetical():
    assert sorted_list_sum(["cb", "ab", "db"]) == ["ab", "cb", "db"]

def test_single_even_length():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_odd_length():
    assert sorted_list_sum(["a"]) == []

def test_longer_strings():
    assert sorted_list_sum(["abcdef", "abc", "defgh"]) == ["abcdef", "defgh"]

def test_edge_case_empty_string():
    assert sorted_list_sum(["", "a", "aa"]) == ["aa"]

def test_empty_strings_with_even_lengths():
    assert sorted_list_sum(["", "", "aa", "bb"]) == ["aa", "bb"]

def test_unicode_strings():
    assert sorted_list_sum(["你好", "世界", "你好世界"]) == ["你好", "世界"]

def test_large_list():
    large_list = ["aa" for _ in range(100)] + ["a" for _ in range(50)]
    assert sorted_list_sum(large_list) == ["aa" for _ in range(100)]

def test_non_string_input():
    with pytest.raises(TypeError) as excinfo:
        sorted_list_sum([1, "aa", 3.14])
    assert str(excinfo.value) == "Input must be a list of strings."

def test_mixed_even_odd_duplicates():
    assert sorted_list_sum(["aa", "a", "bb", "ccc", "aa", "dd"]) == ["aa", "aa", "bb", "dd"]

def test_unicode_same_length():
    assert sorted_list_sum(["你好", "世界", "你好"]) == ["你好", "你好", "世界"]