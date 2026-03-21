import pytest
from typing import List

def test_separate_paren_groups_empty_string():
    assert separate_paren_groups('') == []

def test_separate_paren_groups_single_group():
    assert separate_paren_groups('(())') == ['(())']

def test_separate_paren_groups_multiple_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

def test_separate_paren_groups_invalid_input():
    with pytest.raises(ValueError):
        separate_paren_groups('(((')

def test_separate_paren_groups_invalid_input_2():
    with pytest.raises(ValueError):
        separate_paren_groups(')(')

def test_separate_paren_groups_single_open_parenthesis():
    with pytest.raises(ValueError):
        separate_paren_groups('(')

def test_separate_paren_groups_single_close_parenthesis():
    with pytest.raises(ValueError):
        separate_paren_groups(')')

def test_separate_paren_groups_multiple_open_parentheses():
    with pytest.raises(ValueError):
        separate_paren_groups('(((')

def test_separate_paren_groups_multiple_close_parentheses():
    with pytest.raises(ValueError):
        separate_paren_groups('))')

def test_separate_paren_groups_no_parentheses():
    assert separate_paren_groups('hello world') == []

def test_separate_paren_groups_parentheses_with_spaces():
    assert separate_paren_groups('( ) (( ) ) (( )( ))') == ['()', '(())', '(()())']

def test_separate_paren_groups_group_with_spaces():
    assert separate_paren_groups(' ( ) ') == ['()']

def test_separate_paren_groups_mixed_parentheses():
    assert separate_paren_groups('( ) (( ) ) (( )( )) (hello world)') == ['()', '(())', '(()())']

def test_separate_paren_groups_invalid_mixed_parentheses():
    with pytest.raises(ValueError):
        separate_paren_groups('( ) (( ) ) (( )( )) (hello world (')