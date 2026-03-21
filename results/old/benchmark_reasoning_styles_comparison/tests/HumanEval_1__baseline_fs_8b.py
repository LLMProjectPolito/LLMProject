import pytest

def test_separate_paren_groups_empty_string():
    assert separate_paren_groups('') == []

def test_separate_paren_groups_single_group():
    assert separate_paren_groups('( )') == ['()']

def test_separate_paren_groups_multiple_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

def test_separate_paren_groups_ignores_spaces():
    assert separate_paren_groups('( ) (( )) (( )( )) ') == ['()', '(())', '(()())']

def test_separate_paren_groups_nested_groups():
    assert separate_paren_groups('( ( ) )') == ['(())']

def test_separate_paren_groups_unbalanced_groups():
    with pytest.raises(Exception):
        separate_paren_groups('( ) (( )')

def test_separate_paren_groups_no_parentheses():
    assert separate_paren_groups('hello world') == []

def test_separate_paren_groups_only_open_parentheses():
    with pytest.raises(Exception):
        separate_paren_groups('(((')

def test_separate_paren_groups_only_close_parentheses():
    with pytest.raises(Exception):
        separate_paren_groups(')))')