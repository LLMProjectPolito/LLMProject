import pytest

def test_filter_by_substring_empty_list():
    assert filter_by_substring([], 'a') == []

def test_filter_by_substring_no_matches():
    assert filter_by_substring(['bcd', 'cde', 'efg'], 'a') == []

def test_filter_by_substring_single_match():
    assert filter_by_substring(['abc'], 'a') == ['abc']

def test_filter_by_substring_multiple_matches():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

def test_filter_by_substring_no_substring():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], '') == ['abc', 'bacd', 'cde', 'array']

def test_filter_by_substring_substring_not_in_strings():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'z') == []

def test_filter_by_substring_substring_is_string():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'abc') == ['abc', 'bacd']

def test_filter_by_substring_substring_is_part_of_string():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'bc') == ['abc', 'bacd']

def test_filter_by_substring_case_sensitive():
    assert filter_by_substring(['abc', 'Abc', 'ABC'], 'a') == ['abc']

def test_filter_by_substring_substring_is_empty_string():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], '') == ['abc', 'bacd', 'cde', 'array']