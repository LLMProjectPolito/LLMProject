import pytest
from typing import List
import math

def test_empty_string():
    """ Test that an empty string returns an empty list """
    result = separate_paren_groups("")
    assert result == []

def test_separate_paren_groups_empty_string():
    """Test that an empty string is handled correctly."""
    result = separate_paren_groups("")
    assert result == []