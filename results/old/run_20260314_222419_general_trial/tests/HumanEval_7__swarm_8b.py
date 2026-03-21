import pytest
import math

def test_filter_by_substring_empty_substring():
    """ Testing filtering with an empty substring """
    strings = ['abc', 'bacd', 'cde', 'array']
    substring = ''
    result = filter_by_substring(strings, substring)
    assert result == strings, "Expected all strings to be filtered"

def test_filter_by_substring_empty_string_substring():
    """Test filtering with an empty substring."""
    assert filter_by_substring(["hello", "world"], "") == ["hello", "world"]