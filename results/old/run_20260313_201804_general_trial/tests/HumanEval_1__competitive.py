import pytest
from typing import List

def test_separate_paren_groups_empty_string():
    assert separate_paren_groups('') == []

def test_separate_paren_groups_single_group():
    assert separate_paren_groups('( )') == ['( )']

def test_separate_paren_groups_multiple_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

def test_separate_paren_groups_no_parentheses():
    assert separate_paren_groups('hello world') == []

def test_separate_paren_groups_parentheses_not_balanced():
    with pytest.raises(ValueError):
        separate_paren_groups('( (')

def test_separate_paren_groups_parentheses_nested():
    assert separate_paren_groups('( ( ) )') == ['( ( ) )']

def test_separate_paren_groups_parentheses_with_spaces():
    assert separate_paren_groups('(  ) (  (  )  )') == ['( )', '( ( ) )']

def test_separate_paren_groups_parentheses_with_newlines():
    assert separate_paren_groups('( \n ) ( \n ( \n ) \n )') == ['( )', '( ( ) )']

def test_separate_paren_groups_parentheses_with_tabs():
    assert separate_paren_groups('( \t ) ( \t ( \t ) \t )') == ['( )', '( ( ) )']