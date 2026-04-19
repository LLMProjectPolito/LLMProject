
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
    # Basic cases from problem description
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
    
    # Boundary cases for single digits
    (0, 0, [0]),           # Single even digit (zero)
    (1, 1, []),           # Single odd digit
    (2, 2, [2]),          # Single even digit
    (3, 3, []),           # Single odd digit
    (9, 9, []),           # Single odd digit boundary
    (1, 2, [2]),          # Range [1, 2]
    (2, 1, [2]),          # Range [1, 2] reversed
    (1, 9, [2, 4, 6, 8]), # Full span of positive single digits
    (9, 1, [2, 4, 6, 8]), # Full span reversed
    
    # Partial overlap with single digits
    (0, 4, [0, 2, 4]),    # Including 0
    (0, 5, [0, 2, 4]),    # Including 0, ending odd
    (7, 12, [8]),         # Range [7...12], only 8 is an even digit
    (12, 7, [8]),         # Range [7...12] reversed
    (8, 11, [8]),         # Range [8...11], only 8 is an even digit
    (11, 8, [8]),         # Range [8...11] reversed
    (5, 12, [6, 8]),      # Range [5...12]
    (12, 5, [6, 8]),      # Range [5...12] reversed
    (8, 15, [8]),         # Range [8...15]
    (15, 8, [8]),         # Range [8...15] reversed
    
    # Small ranges with odd numbers
    (1, 3, [2]),          # [1, 2, 3]
    (3, 5, [4]),          # [3, 4, 5]
    (5, 3, [4]),          # [3, 4, 5] reversed
    (5, 7, [6]),          # [5, 6, 7]
    (7, 5, [6]),          # [5, 6, 7] reversed
    
    # Range entirely outside single digits
    (10, 10, []),         # Exactly 10
    (11, 20, []),         # Above 9
    (15, 20, []),         # Above 9
    (20, 15, []),         # Above 9 reversed
    (100, 200, []),       # Far above 9
    
    # Large ranges spanning all digits
    (1, 100, [2, 4, 6, 8]),
    (100, 1, [2, 4, 6, 8]),
    (1, 1000, [2, 4, 6, 8]),
    (1000, 1, [2, 4, 6, 8]),
])
def test_generate_integers(a, b, expected):
    """
    Tests generate_integers with a comprehensive set of ranges including:
    - Standard positive ranges and reversed ranges
    - Boundary cases for single digits (0-9)
    - Partial and no overlap with the single-digit range
    - Large ranges to ensure only single digits are captured
    """
    assert generate_integers(a, b) == expected

def test_generate_integers_type_consistency():
    """
    Ensure the return type is always a list, regardless of whether digits are found.
    """
    assert isinstance(generate_integers(10, 20), list)
    assert isinstance(generate_integers(2, 4), list)

def test_generate_integers_ascending_order():
    """
    Ensure the output is always in ascending order regardless of input order.
    """
    res1 = generate_integers(2, 8)
    res2 = generate_integers(8, 2)
    assert res1 == res2
    assert res1 == sorted(res1)