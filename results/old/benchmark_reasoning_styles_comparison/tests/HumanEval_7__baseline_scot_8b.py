import pytest

def test_filter_by_substring_empty_list():
    assert filter_by_substring([], 'a') == []

def test_filter_by_substring_no_matches():
    assert filter_by_substring(['bcd', 'cde', 'efg'], 'a') == []

def test_filter_by_substring_single_match():
    assert filter_by_substring(['abc', 'bcd', 'cde'], 'a') == ['abc']

def test_filter_by_substring_multiple_matches():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

def test_filter_by_substring_substring_at_end():
    assert filter_by_substring(['abc', 'bacd', 'cdea'], 'a') == ['abc', 'bacd', 'cdea']

def test_filter_by_substring_substring_at_start():
    assert filter_by_substring(['abc', 'bacd', 'abcd'], 'ab') == ['abc', 'abcd']

def test_filter_by_substring_substring_in_middle():
    assert filter_by_substring(['abc', 'bacd', 'abce'], 'bc') == ['abc', 'bacd']

def test_filter_by_substring_empty_substring():
    assert filter_by_substring(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']

def test_filter_by_substring_single_character_substring():
    assert filter_by_substring(['abc', 'bcd', 'cde'], 'b') == ['abc', 'bcd']

def test_filter_by_substring_long_substring():
    assert filter_by_substring(['abc', 'abcd', 'abcde'], 'abcd') == ['abcd', 'abcde']