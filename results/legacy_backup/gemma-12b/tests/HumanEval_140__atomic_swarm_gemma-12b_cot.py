import pytest
import math

def test_fix_spaces_typical():
    assert fix_spaces("Example 1") == "Example_1"

def test_empty_string():
    """Test with an empty string as input."""
    assert fix_spaces("") == ""

def test_fix_spaces_invalid_input_type():
    """Test with a non-string input."""
    try:
        fix_spaces(123)
        assert False, "Should have raised a TypeError"
    except TypeError:
        assert True