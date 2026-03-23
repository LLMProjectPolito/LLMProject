import pytest
import math

def test_x_or_y_n_is_one():
    assert x_or_y(1, 5, 10) == 10

def test_x_or_y_edge_case_n_equals_one():
    """Test when n is 1, which is not a prime number."""
    assert x_or_y(1, 34, 12) == 12