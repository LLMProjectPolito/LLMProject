import pytest

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd():
    assert sorted_list_sum(["a", "bb", "ccc"]) == []

def test_sorted_list_sum_all_even():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_sorted_list_sum_mixed():
    assert sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

def test_sorted_list_sum_mixed_2():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "bb", "aa", "cc", "bb"]) == ["aa", "aa", "bb", "bb", "cc"]

def test_sorted_list_sum_same_length():
    assert sorted_list_sum(["bc", "ab", "cd"]) == ["ab", "bc", "cd"]

def test_sorted_list_sum_same_length_different_order():
    assert sorted_list_sum(["cd", "ab", "ef"]) == ["ab", "cd", "ef"]

def test_sorted_list_sum_complex():
    assert sorted_list_sum(["abc", "ab", "abcd", "a", "abcde", "bcd"]) == ["ab", "bcd"]

def test_sorted_list_sum_long_strings():
    assert sorted_list_sum(["abcdef", "abc", "abcd", "abcde"]) == ["abcd"]

def test_sorted_list_sum_with_numbers_as_strings():
    assert sorted_list_sum(["12", "1", "123", "1234"]) == ["12"]

def test_sorted_list_sum_with_odd_and_even_duplicates():
    assert sorted_list_sum(["a", "aa", "a", "aaa", "aa"]) == ["aa", "aa"]