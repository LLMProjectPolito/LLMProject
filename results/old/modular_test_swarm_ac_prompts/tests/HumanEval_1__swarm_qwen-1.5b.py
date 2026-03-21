import pytest
from typing import List

def test_empty_string():
    """ Test an edge case where input string is empty """
    assert separate_paren_groups('') == []

def test_separate_paren_groups_single_group_with_leading_space():
    """Check that a single group with leading spaces is correctly separated."""
    result = separate_paren_groups(" ()")
    assert result == ["()"]

def test_separate_paren_groups_empty_string():
    """ Test that an empty string is properly handled as a single group """  
    result = separate_paren_groups("")
    assert result == [""]  # expected result