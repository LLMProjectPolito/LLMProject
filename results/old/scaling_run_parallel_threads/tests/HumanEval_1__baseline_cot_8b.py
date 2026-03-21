import pytest

def test_separate_paren_groups_empty_string():
    assert separate_paren_groups('') == []

def test_separate_paren_groups_single_group():
    assert separate_paren_groups('( )') == ['()']

def test_separate_paren_groups_multiple_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

def test_separate_paren_groups_nested_groups():
    assert separate_paren_groups('( ( ) )') == ['(())']

def test_separate_paren_groups_ignores_spaces():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
    assert separate_paren_groups(' ( )  ( ( ) ) ') == ['()', '(())']

def test_separate_paren_groups_unbalanced_groups():
    with pytest.raises(ValueError):
        separate_paren_groups('( ) (( )')

def test_separate_paren_groups_invalid_input():
    with pytest.raises(TypeError):
        separate_paren_groups(123)

def test_separate_paren_groups_large_input():
    large_input = '( ) ' * 1000
    expected_output = ['()'] * 1000
    assert separate_paren_groups(large_input) == expected_output