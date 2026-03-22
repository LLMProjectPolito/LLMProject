import pytest
import math

def test_basic():
    assert solve("ab") == "AB"

def test_empty_string():
    """Test with an empty string."""
    assert solve("") == ""

def test_solve_empty_string():
    assert solve("") == ""