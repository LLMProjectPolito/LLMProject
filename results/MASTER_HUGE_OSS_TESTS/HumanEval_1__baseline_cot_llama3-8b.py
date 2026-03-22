import pytest
from typing import List

def test_empty_string():
    assert separate_paren_groups('') == []

def test_single_group():
    assert separate_paren_groups('( )') == ['()']

def test_multiple_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

def test_balanced_groups():
    assert separate_paren_groups('(()) (()())') == ['(())', '(()())']

def test_unbalanced_groups():
    with pytest.raises(ValueError):
        separate_paren_groups('( ( )')

def test_nested_groups():
    assert separate_paren_groups('(( )) (( )( ))') == ['(( ))', '(( )( ))']

def test_leading_trailing_spaces():
    assert separate_paren_groups('( )  (( ))  (( )( ))') == ['()', '(())', '(()())']

def test_duplicate_groups():
    assert separate_paren_groups('( ) ( ) (( )) (( )( ))') == ['()', '()', '(())', '(()())']

def test_invalid_input():
    with pytest.raises(TypeError):
        separate_paren_groups(123)