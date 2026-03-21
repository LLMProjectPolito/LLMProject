import pytest
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    # implementation of the function
    pass

def test_parse_nested_parens_empty_string():
    assert parse_nested_parens("") == []

def test_parse_nested_parens_single_group():
    assert parse_nested_parens("(()())") == [2]

def test_parse_nested_parens_multiple_groups():
    assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]

def test_parse_nested_parens_no_parens():
    assert parse_nested_parens("hello world") == []

def test_parse_nested_parens_unbalanced_parens():
    with pytest.raises(Exception):
        parse_nested_parens("(()")

def test_parse_nested_parens_large_input():
    large_input = "(()()) " * 100
    expected_output = [2] * 100
    assert parse_nested_parens(large_input) == expected_output

def test_parse_nested_parens_nested_parens():
    assert parse_nested_parens("((()))") == [3]

def test_parse_nested_parens_multiple_nested_parens():
    assert parse_nested_parens("((())) (((())))") == [3, 4]