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
    assert separate_paren_groups('(())') == ['(())']

def test_separate_paren_groups_multiple_groups():
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']

def test_separate_paren_groups_invalid_input():
    with pytest.raises(TypeError):
        separate_paren_groups(123)

def test_separate_paren_groups_invalid_input_type():
    with pytest.raises(TypeError):
        separate_paren_groups(['(())'])

def test_separate_paren_groups_single_group_with_spaces():
    assert separate_paren_groups(' ( ) ') == ['( )']

def test_separate_paren_groups_multiple_groups_with_spaces():
    assert separate_paren_groups(' ( ) ( ( ) ) ( ( ) ( ) ) ') == ['( )', '( ( ) )', '( ( ) ( ) )']

def test_separate_paren_groups_positive():
    """ Test case for positive test scenario
    Expected output: ['()', '(())', '(()())']
    """
    input_str = '( ) (( )) (( )( ))'
    expected_output = ['()', '(())', '(()())']
    assert separate_paren_groups(input_str) == expected_output

def test_separate_paren_groups_single_group():
    """ Test case for single group scenario
    Expected output: ['(())']
    """
    input_str = '(())'
    expected_output = ['(())']
    assert separate_paren_groups(input_str) == expected_output

def test_separate_paren_groups_empty_string():
    """ Test case for empty string scenario
    Expected output: []
    """
    input_str = ''
    expected_output = []
    assert separate_paren_groups(input_str) == expected_output

def test_separate_paren_groups_no_parentheses():
    """ Test case for string without parentheses scenario
    Expected output: []
    """
    input_str = 'hello world'
    expected_output = []
    assert separate_paren_groups(input_str) == expected_output

def test_separate_paren_groups_unbalanced_parentheses():
    """ Test case for unbalanced parentheses scenario
    Expected output: []
    """
    input_str = '(hello'
    expected_output = []
    assert separate_paren_groups(input_str) == expected_output

def test_separate_paren_groups_multiple_spaces():
    """ Test case for string with multiple spaces scenario
    Expected output: ['()', '(())', '(()())']
    """
    input_str = '( ) (( )) (( )( ))'
    expected_output = ['()', '(())', '(()())']
    assert separate_paren_groups(input_str) == expected_output

def test_separate_paren_groups_only_spaces():
    """ Test case for string with only spaces scenario
    Expected output: []
    """
    input_str = '   '
    expected_output = []
    assert separate_paren_groups(input_str) == expected_output