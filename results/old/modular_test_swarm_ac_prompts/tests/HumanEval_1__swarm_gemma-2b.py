import pytest
from typing import List
from your_module import separate_paren_groups  # replace 'your_module' with the actual module name

def test_separate_paren_groups_single_empty_group():
    """Test separating a string with a single empty group of parentheses."""
    result = separate_paren_groups('() () ()')
    assert result == ['()', '()', '()']

def test_separate_paren_groups_single_char_group():
    """Test separating a string with multiple groups of parentheses."""
    result = separate_paren_groups('()()()')
    assert len(result) == 3
    assert all(group in ('()',) for group in result)

def test_separate_paren_groups_multiple_groups():
    """Test that a single empty group is still treated as a valid group."""
    result = separate_paren_groups('()()() ()(()())')
    assert '()' in result and '(()())' in result and '' in result