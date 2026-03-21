import pytest

def test_filter_by_substring_empty_list():
    assert filter_by_substring([], 'a') == []

def test_filter_by_substring_no_matches():
    assert filter_by_substring(['bcd', 'cde', 'efg'], 'a') == []

def test_filter_by_substring_multiple_matches():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

def test_filter_by_substring_single_match():
    assert filter_by_substring(['abc', 'bcd', 'cde'], 'a') == ['abc']

def test_filter_by_substring_no_substring():
    assert filter_by_substring(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']

def test_filter_by_substring_substring_not_in_strings():
    assert filter_by_substring(['abc', 'bcd', 'cde'], 'f') == []

def test_filter_by_substring_substring_is_string():
    assert filter_by_substring(['abc', 'bcd', 'cde'], 'bc') == ['abc', 'bcd']

def test_filter_by_substring_input_list_is_none():
    with pytest.raises(TypeError):
        filter_by_substring(None, 'a')

def test_filter_by_substring_substring_is_none():
    with pytest.raises(TypeError):
        filter_by_substring(['abc', 'bcd', 'cde'], None)

def test_filter_by_substring_input_list_is_not_list():
    with pytest.raises(TypeError):
        filter_by_substring('abc', 'a')

def test_filter_by_substring_substring_is_not_string():
    with pytest.raises(TypeError):
        filter_by_substring(['abc', 'bcd', 'cde'], 123)