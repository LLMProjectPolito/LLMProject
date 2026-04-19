
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

import pytest

@pytest.mark.parametrize("a, b, expected", [
    # Basic cases from docstring
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
    
    # Single digit ranges
    (1, 3, [2]),
    (1, 1, []),
    (2, 2, [2]),
    (3, 3, []),
    (5, 7, [6]),
    (0, 9, [0, 2, 4, 6, 8]), # Testing boundary 0 if considered positive/non-negative
    
    # Ranges spanning across the single-digit boundary
    (5, 15, [6, 8]),
    (15, 5, [6, 8]),
    (12, 20, []),
    
    # Large numbers
    (100, 200, []),
    (0, 0, [0]),
    
    # All even digits
    (0, 8, [0, 2, 4, 6, 8]),
    (8, 0, [0, 2, 4, 6, 8]),
])
def test_generate_integers(a, b, expected):
    """
    Tests that generate_integers returns even digits between a and b 
    in ascending order, regardless of the order of a and b.
    """
    assert generate_integers(a, b) == expected

def test_generate_integers_type():
    """
    Ensure the return type is always a list.
    """
    result = generate_integers(2, 8)
    assert isinstance(result, list)

def test_generate_integers_ascending_order():
    """
    Explicitly verify that the output is always sorted ascending.
    """
    # Even if input is descending, output must be ascending
    result = generate_integers(8, 2)
    assert result == sorted(result)