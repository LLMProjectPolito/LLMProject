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
    # Function implementation remains the same

def test_separate_paren_groups_empty_string():
    assert separate_paren_groups('') == []

def test_separate_paren_groups_single_group():
    assert separate_paren_groups('( )') == ['( )']

def test_separate_paren_groups_multiple_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

def test_separate_paren_groups_unbalanced_parentheses():
    with pytest.raises(ValueError):
        separate_paren_groups('( (')

def test_separate_paren_groups_nested_parentheses():
    assert separate_paren_groups('( ( ) )') == ['( ( ) )']

def test_separate_paren_groups_parentheses_with_spaces():
    assert separate_paren_groups('( ) ( ( ) )') == ['( )', '( ( ) )']

def test_separate_paren_groups_parentheses_with_newlines():
    assert separate_paren_groups('( )\n( ( ) )') == ['( )', '( ( ) )']

def test_separate_paren_groups_parentheses_with_tabs():
    assert separate_paren_groups('\t( )\t( ( ) )') == ['( )', '( ( ) )']

def test_separate_paren_groups_parentheses_with_special_chars():
    assert separate_paren_groups('( )!@#$(( )( ))') == ['()', '(())', '(()())']

def test_separate_paren_groups_parentheses_with_numbers():
    assert separate_paren_groups('(1) (2(3))') == ['(1)', '(2(3))']