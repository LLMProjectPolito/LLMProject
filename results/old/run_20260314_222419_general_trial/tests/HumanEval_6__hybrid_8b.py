import pytest
from typing import List

@pytest.mark.parametrize("input_string, expected_output", [
    ('(()()) ((())) () ((())()())', [2, 3, 1, 3]),
    ('()', [1]),
    ('() ()', [1, 1]),
    ('((()))', [3]),
    ('(((())()()()()()()()()()()()()()()()()()))', [6]),
    ('', []),
    (' ', []),
    ('() () ()', [1, 1, 1]),
    ('()()()()', [1, 1, 1, 1]),
    ('(((())))', [4]),
])
def test_parse_nested_parens(input_string: str, expected_output: List[int]):
    assert parse_nested_parens(input_string) == expected_output

def test_parse_nested_parens_empty_groups():
    assert parse_nested_parens('() ()') == [1, 1]

def test_parse_nested_parens_single_group():
    assert parse_nested_parens('()') == [1]

def test_parse_nested_parens_no_groups():
    assert parse_nested_parens('') == []

def test_parse_nested_parens_only_spaces():
    assert parse_nested_parens('   ') == []

def test_parse_nested_parens_large_input():
    large_input = '() ' * 1000
    expected_output = [1] * 1000
    assert parse_nested_parens(large_input) == expected_output

def test_parse_nested_parens_invalid_input():
    with pytest.raises(TypeError):
        parse_nested_parens(123)

def test_parse_nested_parens_empty_string():
    assert parse_nested_parens('') == []

def test_parse_nested_parens_multiple_groups():
    assert parse_nested_parens('() () ()') == [1, 1, 1]

def test_parse_nested_parens_deep_nesting():
    assert parse_nested_parens('(((())))') == [4]