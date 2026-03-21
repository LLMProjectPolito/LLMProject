import pytest

def test_parse_nested_parens_empty_string():
    assert parse_nested_parens('') == []

def test_parse_nested_parens_single_group():
    assert parse_nested_parens('(()())') == [2]

def test_parse_nested_parens_multiple_groups():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]

def test_parse_nested_parens_no_parens():
    assert parse_nested_parens('a b c') == []

def test_parse_nested_parens_unbalanced_parens():
    with pytest.raises(Exception):
        parse_nested_parens('(()')

def test_parse_nested_parens_large_input():
    large_input = '(()()) ' * 100
    expected_output = [2] * 100
    assert parse_nested_parens(large_input) == expected_output

def test_parse_nested_parens_deep_nesting():
    deep_nesting = '(' * 100 + ')' * 100
    assert parse_nested_parens(deep_nesting) == [100]

def test_parse_nested_parens_multiple_deep_nesting():
    multiple_deep_nesting = '(' * 100 + ')' * 100 + ' ' + '(' * 50 + ')' * 50
    assert parse_nested_parens(multiple_deep_nesting) == [100, 50]