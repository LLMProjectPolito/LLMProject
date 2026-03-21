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
    # Your implementation here

def test_separate_paren_groups_empty_string():
    assert separate_paren_groups("") == []

def test_separate_paren_groups_single_group():
    assert separate_paren_groups("( )") == ["()"]

def test_separate_paren_groups_multiple_groups():
    assert separate_paren_groups("( ) (( )) (( )( ))") == ["()", "(())", "(()())"]

def test_separate_paren_groups_nested_groups():
    assert separate_paren_groups("( ( ) )") == ["( ( ) )"]

def test_separate_paren_groups_unbalanced_groups():
    with pytest.raises(ValueError):
        separate_paren_groups("( ) (")

def test_separate_paren_groups_ignores_spaces():
    assert separate_paren_groups("( ) (( )) (( )( ))") == ["()", "(())", "(()())"]
    assert separate_paren_groups("( )  ( ( ) )") == ["()", "( ( ) )"]

def test_separate_paren_groups_large_input():
    large_input = "( ) " * 1000
    assert len(separate_paren_groups(large_input)) == 1000

def test_separate_paren_groups_invalid_input():
    with pytest.raises(TypeError):
        separate_paren_groups(123)