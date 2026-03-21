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

def test_parse_nested_parens_single_paren():
    assert parse_nested_parens('(') == []

def test_parse_nested_parens_single_closing_paren():
    with pytest.raises(Exception):
        parse_nested_parens(')')

def test_parse_nested_parens_only_spaces():
    assert parse_nested_parens('   ') == []