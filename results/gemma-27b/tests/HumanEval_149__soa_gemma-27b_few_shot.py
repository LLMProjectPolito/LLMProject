import pytest

def test_sorted_list_sum_empty():
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_all_odd():
    assert sorted_list_sum(["a", "bb", "ccc"]) == []

def test_sorted_list_sum_all_even():
    assert sorted_list_sum(["aa", "bb", "cc"]) == sorted(["aa", "bb", "cc"])

def test_sorted_list_sum_mixed():
    assert sorted_list_sum(["aa", "a", "aaa", "bb", "c"]) == sorted(["aa", "bb"])

def test_sorted_list_sum_duplicates():
    assert sorted_list_sum(["aa", "a", "aa", "bb", "c", "bb"]) == sorted(["aa", "aa", "bb", "bb"])

def test_sorted_list_sum_same_length():
    assert sorted_list_sum(["ab", "cd", "ef"]) == sorted(["ab", "cd", "ef"])

def test_sorted_list_sum_complex():
    assert sorted_list_sum(["apple", "banana", "kiwi", "orange", "grape"]) == sorted(["apple", "grape", "orange"])

def test_sorted_list_sum_long_strings():
    assert sorted_list_sum(["abcdef", "abc", "defgh", "hi"]) == sorted(["abcdef", "defgh"])

def test_sorted_list_sum_with_empty_string():
    assert sorted_list_sum(["", "a", "aa"]) == sorted(["aa"])

def test_sorted_list_sum_only_empty_string():
    assert sorted_list_sum([""]) == []