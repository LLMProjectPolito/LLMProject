import pytest
from your_module import sorted_list_sum  # Replace your_module

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_length():
    assert sorted_list_sum(["a", "bc", "def"]) == []

def test_all_even_length():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_lengths():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "b", "ccc"]) == ["aa", "bb", "ccc"]

def test_mixed_lengths_with_duplicates():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "a", "ccc", "aa"]) == ["aa", "aa", "bb", "ccc"]

def test_same_length_alphabetical():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_same_length_alphabetical_with_duplicates():
    assert sorted_list_sum(["ab", "cd", "ef", "ab"]) == ["ab", "ab", "cd", "ef"]

def test_mixed_lengths_and_alphabetical():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "b", "ccc", "ab"]) == ["aa", "ab", "bb", "ccc"]

def test_long_list():
    lst = ["a", "aa", "aaa", "aaaa", "aaaaa", "b", "bb", "bbb", "bbbb", "bbbbb", "c", "cc", "ccc", "cccc", "ccccc"]
    expected = ["a", "b", "c", "aa", "bb", "cc", "aaa", "bbb", "ccc", "aaaa", "bbbb", "cccc", "aaaaa", "bbbbb", "ccccc"]
    assert sorted_list_sum(lst) == expected

def test_list_with_special_characters():
    assert sorted_list_sum(["a!", "aa?", "aaa#"]) == ["a!", "aa?", "aaa#"]

def test_list_with_numbers_as_strings():
    assert sorted_list_sum(["1", "12", "123"]) == ["1", "12", "123"]

def test_list_with_empty_string():
    assert sorted_list_sum(["", "a", "aa"]) == ["", "aa"]