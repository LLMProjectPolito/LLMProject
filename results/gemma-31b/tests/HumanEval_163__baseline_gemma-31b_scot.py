
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
    # Standard cases from docstring
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
    
    # Range with odd numbers
    (1, 5, [2, 4]),
    (3, 7, [4, 6]),
    
    # Single value ranges
    (4, 4, [4]),
    (5, 5, []),
    
    # Ranges containing no even digits
    (1, 1, []),
    (3, 3, []),
    (7, 9, [8]),
    
    # Boundary cases for digits (0-9)
    (0, 9, [0, 2, 4, 6, 8]),
    (0, 0, [0]),
    
    # Large numbers (completely outside digit range)
    (100, 200, []),
    (10, 10, []),
    
    # Overlapping digit and non-digit range
    (5, 12, [6, 8]),
    (12, 5, [6, 8]),
])
def test_generate_integers(a, b, expected):
    """
    Tests generate_integers with various ranges to ensure only even 
    single-digits are returned in ascending order.
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
    Explicitly verify that the output is always sorted ascending 
    regardless of input order.
    """
    res1 = generate_integers(2, 8)
    res2 = generate_integers(8, 2)
    assert res1 == res2
    assert res1 == sorted(res1)