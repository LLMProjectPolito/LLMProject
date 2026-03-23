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

def test_sorted_list_sum_mixed():
    assert sorted_list_sum(["aa", "a", "bb", "b", "ccc", "c"]) == ["aa", "bb", "ccc"]

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "aa", "a", "aaa"]) == ["aa", "aa"]

def test_sorted_list_sum_same_length_alphabetical():
    assert sorted_list_sum(["ab", "ac", "ad"]) == ["ab", "ac", "ad"]

def test_sorted_list_sum_same_length_alphabetical_mixed():
    assert sorted_list_sum(["ab", "a", "ac", "ad", "b"]) == ["ab", "ac", "ad"]

def test_sorted_list_sum_long_list():
    assert sorted_list_sum(["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa"]) == ["aa", "aaaa", "aaaaa", "aaaaaa"]

def test_sorted_list_sum_with_empty_string():
    assert sorted_list_sum(["", "a", "aa"]) == ["", "aa"]