import pytest

def test_sorted_list_sum_basic():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_sorted_list_sum_multiple():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd():
    assert sorted_list_sum(["a", "b", "c"]) == []

def test_sorted_list_sum_all_even():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_sorted_list_sum_mixed_same_length():
    assert sorted_list_sum(["aa", "bb", "a", "c"]) == ["aa", "bb"]

def test_sorted_list_sum_mixed_different_lengths():
    assert sorted_list_sum(["aa", "b", "ccc", "dd"]) == ["aa", "dd"]

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "aa", "a"]) == ["aa", "aa"]

def test_sorted_list_sum_same_length_alphabetical():
    assert sorted_list_sum(["bb", "aa", "cc"]) == ["aa", "bb", "cc"]

def test_sorted_list_sum_complex():
    assert sorted_list_sum(["abc", "a", "ab", "abcd", "bc"]) == ["ab", "abc", "abcd"]