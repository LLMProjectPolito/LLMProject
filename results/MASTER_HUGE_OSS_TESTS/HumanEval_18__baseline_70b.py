import pytest

def test_empty_string():
    assert how_many_times('', 'a') == 0

def test_no_substring():
    assert how_many_times('abc', 'd') == 0

def test_single_character_substring():
    assert how_many_times('aaa', 'a') == 3

def test_overlapping_substring():
    assert how_many_times('aaaa', 'aa') == 3

def test_non_overlapping_substring():
    assert how_many_times('abcabc', 'abc') == 2

def test_substring_longer_than_string():
    assert how_many_times('abc', 'abcd') == 0

def test_empty_substring():
    assert how_many_times('abc', '') == 0

def test_string_and_substring_are_equal():
    assert how_many_times('abc', 'abc') == 1

def test_string_and_substring_are_equal_with_overlapping():
    assert how_many_times('aaa', 'aaa') == 1

def test_substring_appears_at_start_and_end():
    assert how_many_times('abca', 'a') == 2

def test_substring_appears_only_at_start():
    assert how_many_times('abc', 'a') == 1

def test_substring_appears_only_at_end():
    assert how_many_times('abc', 'c') == 1