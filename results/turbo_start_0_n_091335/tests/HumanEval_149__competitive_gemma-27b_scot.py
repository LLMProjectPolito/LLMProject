import pytest

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_all_odd_lengths():
    assert sorted_list_sum(["a", "abc", "def"]) == []

def test_all_even_lengths():
    assert sorted_list_sum(["aa", "bb", "cc"]) == sorted(["aa", "bb", "cc"])

def test_mixed_lengths():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_mixed_lengths_2():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == sorted(["ab", "cd"])

def test_duplicates():
    assert sorted_list_sum(["aa", "aa", "bb", "cc", "a"]) == sorted(["aa", "aa", "bb", "cc"])

def test_same_length_alphabetical():
    assert sorted_list_sum(["cb", "ab", "cd", "ad"]) == sorted(["ab", "ad", "cb", "cd"])

def test_longer_list():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape"]) == sorted(["apple", "grape", "kiwi", "orange"])

def test_list_with_empty_string():
    assert sorted_list_sum(["", "a", "aa"]) == ["aa"]

def test_list_with_only_empty_string():
    assert sorted_list_sum([""]) == []

def test_list_with_odd_and_even_and_duplicates():
    assert sorted_list_sum(["abc", "ab", "a", "cd", "ef", "ab"]) == sorted(["ab", "ab", "cd", "ef"])