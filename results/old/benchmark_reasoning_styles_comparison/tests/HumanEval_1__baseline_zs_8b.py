import pytest

def test_separate_paren_groups_empty_string():
    assert separate_paren_groups("") == []

def test_separate_paren_groups_single_group():
    assert separate_paren_groups("( )") == ["()"]

def test_separate_paren_groups_multiple_groups():
    assert separate_paren_groups("( ) (( )) (( )( ))") == ["()", "(())", "(()())"]

def test_separate_paren_groups_nested_groups():
    assert separate_paren_groups("( ( ) )") == ["(( ))"]

def test_separate_paren_groups_unbalanced_groups():
    with pytest.raises(Exception):
        separate_paren_groups("( ) (")

def test_separate_paren_groups_ignores_spaces():
    assert separate_paren_groups("( ) (( )) (( )( ))") == ["()", "(())", "(()())"]

def test_separate_paren_groups_consecutive_groups():
    assert separate_paren_groups("( )( )") == ["()", "()"]

def test_separate_paren_groups_large_input():
    large_input = "( ) (( )) (( )( ))" * 100
    expected_output = ["()", "(())", "(()())"] * 100
    assert separate_paren_groups(large_input) == expected_output