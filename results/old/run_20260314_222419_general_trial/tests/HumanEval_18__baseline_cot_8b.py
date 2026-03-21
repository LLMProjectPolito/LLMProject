import pytest

def test_how_many_times_empty_string():
    assert how_many_times('', 'a') == 0

def test_how_many_times_no_substring():
    assert how_many_times('abc', 'd') == 0

def test_how_many_times_single_character():
    assert how_many_times('aaa', 'a') == 3

def test_how_many_times_overlapping_substring():
    assert how_many_times('aaaa', 'aa') == 3

def test_how_many_times_non_overlapping_substring():
    assert how_many_times('abcabc', 'abc') == 2

def test_how_many_times_substring_longer_than_string():
    assert how_many_times('abc', 'abcd') == 0

def test_how_many_times_substring_equal_to_string():
    assert how_many_times('abc', 'abc') == 1

def test_how_many_times_string_with_spaces():
    assert how_many_times('a a a', 'a') == 3

def test_how_many_times_substring_with_spaces():
    assert how_many_times('a a a', 'a ') == 2

def test_how_many_times_empty_substring():
    with pytest.raises(ValueError):
        how_many_times('abc', '')

def test_how_many_times_none_string():
    with pytest.raises(TypeError):
        how_many_times(None, 'abc')

def test_how_many_times_none_substring():
    with pytest.raises(TypeError):
        how_many_times('abc', None)