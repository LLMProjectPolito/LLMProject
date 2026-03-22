import pytest

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_odd_lengths_only():
    assert sorted_list_sum(["a", "bc", "def"]) == []

def test_sorted_list_sum_even_lengths_only():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_sorted_list_sum_mixed_lengths():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "ccc"]) == ["aa", "bb"]

def test_sorted_list_sum_same_length_different_alphabetical():
    assert sorted_list_sum(["ab", "cd", "ef"]) == ["ab", "cd", "ef"]

def test_sorted_list_sum_same_length_same_alphabetical():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "aa", "bb", "cc"]) == ["aa", "aa", "bb", "cc"]

def test_sorted_list_sum_complex():
    assert sorted_list_sum(["abc", "a", "ab", "abcd", "bc", "c"]) == ["ab", "bc"]

def test_sorted_list_sum_all_same_length():
    assert sorted_list_sum(["apple", "banana", "cherry"]) == ["apple", "banana", "cherry"]

def test_sorted_list_sum_with_empty_string():
    assert sorted_list_sum(["", "a", "aa"]) == ["", "aa"]

def test_sorted_list_sum_all_odd():
    assert sorted_list_sum(["a", "b", "c", "d"]) == []

def test_sorted_list_sum_all_even():
    assert sorted_list_sum(["aa", "bb", "cc", "dd"]) == ["aa", "bb", "cc", "dd"]

def test_sorted_list_sum_mixed_with_duplicates():
    assert sorted_list_sum(["aa", "a", "bb", "aa", "ccc", "bb"]) == ["aa", "aa", "bb", "bb"]