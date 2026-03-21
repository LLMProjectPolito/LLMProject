import pytest
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    # implementation of the function
    pass

def test_empty_string():
    assert parse_nested_parens("") == []

def test_single_group():
    assert parse_nested_parens("()") == [1]

def test_multiple_groups():
    assert parse_nested_parens("() ()") == [1, 1]

def test_nested_parens():
    assert parse_nested_parens("(()())") == [2]

def test_deeper_nesting():
    assert parse_nested_parens("((()))") == [3]

def test_multiple_groups_with_nesting():
    assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]

def test_invalid_input():
    with pytest.raises(TypeError):
        parse_nested_parens(123)

def test_input_with_non_parenthesis_chars():
    with pytest.raises(ValueError):
        parse_nested_parens("hello world")

def test_input_with_unbalanced_parens():
    with pytest.raises(ValueError):
        parse_nested_parens("(())())")

def test_large_input():
    large_input = " ".join(["()"] * 1000)
    assert parse_nested_parens(large_input) == [1] * 1000