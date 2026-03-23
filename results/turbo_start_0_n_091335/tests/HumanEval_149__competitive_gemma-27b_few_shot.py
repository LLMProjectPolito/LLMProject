import pytest

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "abc", "def"]) == []

def test_all_even_lengths():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_mixed_lengths():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_mixed_lengths_2():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_duplicates():
    assert sorted_list_sum(["aa", "aa", "bb", "cc", "bb"]) == ["aa", "aa", "bb", "bb", "cc"]

def test_same_length_alphabetical():
    assert sorted_list_sum(["cb", "ab", "db"]) == ["ab", "cb", "db"]

def test_longer_list():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape"]) == ["apple", "grape", "kiwi", "orange"]

def test_list_with_empty_string():
    assert sorted_list_sum(["", "a", "aa"]) == ["aa"]

def test_list_with_only_empty_string():
    assert sorted_list_sum([""]) == []

def test_list_with_odd_and_even_and_empty():
    assert sorted_list_sum(["a", "aa", "aaa", ""]) == ["aa"]

def test_list_with_same_length_and_duplicates():
    assert sorted_list_sum(["ab", "ab", "cd", "cd"]) == ["ab", "ab", "cd", "cd"]