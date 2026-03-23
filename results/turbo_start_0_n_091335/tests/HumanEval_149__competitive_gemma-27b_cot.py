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

def test_long_strings():
    assert sorted_list_sum(["abcdef", "abc", "abcd", "abcde"]) == sorted(["abcd", "abcde", "abcdef"])

def test_single_even_length():
    assert sorted_list_sum(["aa"]) == ["aa"]

def test_single_odd_length():
    assert sorted_list_sum(["a"]) == []

def test_mixed_case():
    assert sorted_list_sum(["aA", "bb", "c"]) == sorted(["aA", "bb"])

def test_special_characters():
    assert sorted_list_sum(["!@#", "abc", "123"]) == sorted(["!@#", "123"])

def test_numbers_as_strings():
    assert sorted_list_sum(["12", "1", "123"]) == ["12"]