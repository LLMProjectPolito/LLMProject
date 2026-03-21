import pytest
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

@pytest.mark.parametrize("strings, substring, expected", [
    ([], 'a', []),
    (['abc', 'bacd', 'cde', 'array'], 'a', ['abc', 'bacd', 'array']),
    (['hello', 'world'], 'hello', ['hello']),
    (['hello', 'world'], 'world', ['world']),
    (['hello', 'world'], 'foo', []),
    (['hello', 'hello', 'hello'], 'hello', ['hello', 'hello', 'hello']),
    (['hello', 'world', ''], '', ['hello', 'world', '']),
    (['', '', ''], 'a', []),
])
def test_filter_by_substring(strings, substring, expected):
    assert filter_by_substring(strings, substring) == expected

def test_filter_by_substring_empty_string():
    assert filter_by_substring(['hello', 'world'], '') == ['hello', 'world', '']

def test_filter_by_substring_single_element():
    assert filter_by_substring(['hello'], 'hello') == ['hello']

def test_filter_by_substring_no_match():
    assert filter_by_substring(['hello', 'world'], 'foo') == []

def test_filter_by_substring_multiple_matches():
    assert filter_by_substring(['hello', 'hello', 'hello'], 'hello') == ['hello', 'hello', 'hello']

def test_filter_by_substring_substring_not_in_string():
    assert filter_by_substring(['hello', 'world'], 'foo') == []