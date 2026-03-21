import pytest

def test_all_prefixes_empty_string():
    assert all_prefixes("") == []

def test_all_prefixes_single_character():
    assert all_prefixes("a") == ["a"]

def test_all_prefixes_multiple_characters():
    assert all_prefixes("abc") == ["a", "ab", "abc"]

def test_all_prefixes_long_string():
    assert all_prefixes("abcdefghijklmnopqrstuvwxyz") == [char for i in range(1, 27) for char in ["abcdefghijklmnopqrstuvwxyz"[:i]]]

def test_all_prefixes_repeated_characters():
    assert all_prefixes("aaa") == ["a", "aa", "aaa"]

def test_all_prefixes_special_characters():
    assert all_prefixes("!@#") == ["!", "!@", "!@#"]

def test_all_prefixes_numbers():
    assert all_prefixes("123") == ["1", "12", "123"]