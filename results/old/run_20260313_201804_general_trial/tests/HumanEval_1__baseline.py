import pytest
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

def test_separate_paren_groups_empty_string():
    assert separate_paren_groups('') == []

def test_separate_paren_groups_single_group():
    assert separate_paren_groups('( )') == ['( )']

def test_separate_paren_groups_multiple_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

def test_separate_paren_groups_nested_groups():
    assert separate_paren_groups('( ) (( )( ))') == ['()', '(())']

def test_separate_paren_groups_unbalanced_group():
    with pytest.raises(ValueError):
        separate_paren_groups('( ')

def test_separate_paren_groups_group_with_spaces():
    assert separate_paren_groups('( ) ( ( ) )') == ['( )', '( ( ) )']

def test_separate_paren_groups_group_with_leading_trailing_spaces():
    assert separate_paren_groups('( ) ') == ['( )']

def test_separate_paren_groups_group_with_leading_trailing_parentheses():
    assert separate_paren_groups('( )') == ['( )']

def test_separate_paren_groups_group_with_multiple_leading_trailing_parentheses():
    assert separate_paren_groups('(( ) )') == ['( )']

def test_separate_paren_groups_group_with_multiple_leading_trailing_parentheses_and_spaces():
    assert separate_paren_groups('(( ) )') == ['( )']

def test_separate_paren_groups_group_with_multiple_leading_trailing_parentheses_and_spaces_and_group():
    assert separate_paren_groups('(( ) )(( )( ))') == ['( )', '(())']