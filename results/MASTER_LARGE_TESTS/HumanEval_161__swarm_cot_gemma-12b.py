import pytest
import math

def test_solve_empty_string():
    """Test case for an empty string input."""
    from solution import solve
    assert solve("") == ""