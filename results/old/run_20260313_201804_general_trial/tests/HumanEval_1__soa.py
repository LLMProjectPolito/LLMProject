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

def test_separate_paren_groups_no_groups():
    assert separate_paren_groups('hello world') == []

def test_separate_paren_groups_no_parentheses():
    assert separate_paren_groups('hello world (hello world)') == ['(hello world)']

def test_separate_paren_groups_nested_groups():
    assert separate_paren_groups('( ) (( )) (( )( )( ))') == ['()', '(())', '(()())']

def test_separate_paren_groups_invalid_parentheses():
    with pytest.raises(ValueError):
        separate_paren_groups('(( ))')

def test_separate_paren_groups_invalid_input():
    with pytest.raises(TypeError):
        separate_paren_groups(123)

def test_separate_paren_groups_invalid_input_type():
    with pytest.raises(TypeError):
        separate_paren_groups([1, 2, 3])