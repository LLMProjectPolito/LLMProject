import pytest
import math

def test_fix_spaces_typical():
    """Test with a string containing multiple spaces and consecutive spaces."""
    text = " Example   3"
    expected = "_Example-3"
    assert fix_spaces(text) == expected

def test_empty_string():
    """Test with an empty string as input."""
    assert fix_spaces("") == ""

import pytest

def test_fix_spaces_empty_string():
    """Test with an empty string."""
    assert fix_spaces("") == ""

def test_fix_spaces_no_spaces():
    """Test with a string containing no spaces."""
    assert fix_spaces("Example") == "Example"

def test_fix_spaces_single_space():
    """Test with a string containing a single space."""
    assert fix_spaces("Example 1") == "Example_1"

def test_fix_spaces_leading_space():
    """Test with a string containing a leading space."""
    assert fix_spaces(" Example 2") == "_Example_2"

def test_fix_spaces_multiple_consecutive_spaces():
    """Test with a string containing multiple consecutive spaces."""
    assert fix_spaces(" Example   3") == "_Example-3"

def test_fix_spaces_multiple_consecutive_spaces_at_start():
    """Test with multiple consecutive spaces at the beginning."""
    assert fix_spaces("   Example 4") == "-Example_4"

def test_fix_spaces_multiple_consecutive_spaces_at_end():
    """Test with multiple consecutive spaces at the end."""
    assert fix_spaces("Example 5   ") == "Example_5-"

def test_fix_spaces_mixed_spaces():
    """Test with a mix of single and multiple spaces."""
    assert fix_spaces("Example  1  2   3") == "Example__1_2-3"