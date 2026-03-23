import pytest

def test_empty_list():
    assert sorted_list_sum([]) == []

def test_no_odd_length_strings():
    assert sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

def test_all_odd_length_strings():
    assert sorted_list_sum(["a", "aaa", "aaaaa"]) == []

def test_mixed_length_strings():
    assert sorted_list_sum(["a", "aa", "aaa", "aaaa"]) == ["aa", "aaaa"]

def test_duplicates():
    assert sorted_list_sum(["aa", "aa", "a", "aaa"]) == ["aa", "aa"]

def test_alphabetical_sorting():
    assert sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

def test_length_sorting():
    assert sorted_list_sum(["a", "aa", "aaa", "aaaa"]) == ["aa", "aaaa"]

def test_large_input():
    large_input = ["a" * i for i in range(1, 100)]
    expected_output = ["a" * i for i in range(2, 100, 2)]
    assert sorted_list_sum(large_input) == expected_output

def test_input_with_duplicates_and_odd_length_strings():
    input_list = ["a", "aa", "aa", "aaa", "aaaa"]
    expected_output = ["aa", "aa", "aaaa"]
    assert sorted_list_sum(input_list) == expected_output