import pytest
import math

def solve(s):
    """
    This is a placeholder function.  It's assumed to be defined elsewhere.
    It reverses a string.
    """
    return s[::-1]

def test_solve_no_letters():
    assert solve("1234") == "4321"