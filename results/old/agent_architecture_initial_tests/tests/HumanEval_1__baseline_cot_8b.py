import pytest
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    # implementation of the function
    pass

def test_separate_paren_groups_empty_string():
    assert separate_paren_groups("") == []

def test_separate_paren_groups_single_group():
    assert separate_paren_groups("( )") == ['()']

def test_separate_paren_groups_multiple_groups():
    assert separate_paren_groups("( ) (( )) (( )( ))") == ['()', '(())', '(()())']

def test_separate_paren_groups_nested_groups():
    assert separate_paren_groups("( ( ) )") == ['(())']

def test_separate_paren_groups_ignores_spaces():
    assert separate_paren_groups("( )  ( ( ) )") == ['()', '(())']

def test_separate_paren_groups_unbalanced_groups():
    with pytest.raises(Exception):
        separate_paren_groups("( ) (")

def test_separate_paren_groups_empty_groups():
    assert separate_paren_groups("() ()") == ['()', '()']

def test_separate_paren_groups_large_input():
    large_input = "( ) " * 100
    expected_output = ['()'] * 100
    assert separate_paren_groups(large_input) == expected_output

def test_separate_paren_groups_edge_cases():
    assert separate_paren_groups("(( ))") == ['(())']
    assert separate_paren_groups("(( )( ))") == ['(()())']