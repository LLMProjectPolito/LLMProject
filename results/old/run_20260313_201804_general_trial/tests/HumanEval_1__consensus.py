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
    pass

def test_separate_paren_groups_empty_string():
    """ Test that an empty string is correctly returned """
    assert separate_paren_groups('') == []

def test_separate_paren_groups_single_group():
    """ Test that a single group of parentheses is correctly returned """
    assert separate_paren_groups('( )') == ['( )']

def test_separate_paren_groups_multiple_groups():
    """ Test that multiple groups of parentheses are correctly separated """
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

def test_separate_paren_groups_no_parentheses():
    """ Test that an empty string is returned when there are no parentheses """
    assert separate_paren_groups('abc def') == []

def test_separate_paren_groups_unbalanced_parentheses():
    """ Test that an empty string is returned when there are unbalanced parentheses """
    assert separate_paren_groups('( (') == []

def test_separate_paren_groups_nested_parentheses():
    """ Test that an empty string is returned when there are nested parentheses """
    assert separate_paren_groups('(( ))') == []

def test_separate_paren_groups_large_input():
    """ Test that large inputs are correctly processed """
    large_input = '(' * 100 + ')' * 100
    assert separate_paren_groups(large_input) == [large_input]

def test_separate_paren_groups_duplicates():
    """ Test that duplicate groups are correctly handled """
    assert separate_paren_groups('( )( )( )') == ['()', '()', '()']