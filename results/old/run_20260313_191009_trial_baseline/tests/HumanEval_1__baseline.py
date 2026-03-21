import pytest
from typing import List

def test_separate_paren_groups_empty_string():
    assert separate_paren_groups("") == []

def test_separate_paren_groups_single_group():
    assert separate_paren_groups("( )") == ['()']

def test_separate_paren_groups_multiple_groups():
    assert separate_paren_groups("( ) (( )) (( )( ))") == ['()', '(())', '(()())']

def test_separate_paren_groups_nested_groups():
    assert separate_paren_groups("( ( ) )") == ['(())']

def test_separate_paren_groups_consecutive_groups():
    assert separate_paren_groups("( ) ( )") == ['()', '()']

def test_separate_paren_groups_groups_with_spaces():
    assert separate_paren_groups("( )  ( ( ) )") == ['()', '(())']

def test_separate_paren_groups_empty_groups():
    assert separate_paren_groups("() ()") == ['()', '()']

def test_separate_paren_groups_unbalanced_groups():
    with pytest.raises(Exception):
        separate_paren_groups("( ) (")

def test_separate_paren_groups_invalid_input():
    with pytest.raises(Exception):
        separate_paren_groups("Invalid input")

def test_separate_paren_groups_large_input():
    large_input = "( ) " * 1000
    expected_output = ['()'] * 1000
    assert separate_paren_groups(large_input) == expected_output

def test_separate_paren_groups_edge_case_single_open_paren():
    with pytest.raises(Exception):
        separate_paren_groups("(")

def test_separate_paren_groups_edge_case_single_close_paren():
    with pytest.raises(Exception):
        separate_paren_groups(")")