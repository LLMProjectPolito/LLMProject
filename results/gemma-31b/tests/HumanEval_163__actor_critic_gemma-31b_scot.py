
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
from your_module import generate_integers  # Replace 'your_module' with actual module name

@pytest.mark.parametrize("a, b, expected", [
    # Standard cases from problem description
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
    
    # Edge Case: Range entirely above single digits (Lean: removed 11, 12)
    (100, 200, []),
    
    # Edge Case: Range entirely below the first even digit (0)
    (-10, -5, []),
    
    # Edge Case: a == b
    (4, 4, [4]),
    (3, 3, []),
    
    # Edge Case: Partial overlap with the 0-9 range
    (5, 15, [6, 8]),
    (0, 3, [0, 2]), 
    (-2, 2, [0, 2]), # Overlap including negative start
    
    # Edge Case: Range containing only odd digits
    (7, 7, []),
    
    # Edge Case: Full range of even digits
    (1, 9, [2, 4, 6, 8]),
    (0, 10, [0, 2, 4, 6, 8]),
    
    # Edge Case: Large gap
    (2, 1000, [2, 4, 6, 8]),
])
def test_generate_integers(a, b, expected):
    """
    Tests generate_integers with various ranges to ensure only even 
    single-digits (0, 2, 4, 6, 8) are returned in ascending order.
    """
    assert generate_integers(a, b) == expected

@pytest.mark.parametrize("a, b", [
    ("2", 8),      # String input
    (2, None),     # None input
    (2.5, 8.5),    # Float input
    ([2], [8]),    # List input
])
def test_generate_integers_invalid_types(a, b):
    """
    Ensure the function raises a TypeError when provided with non-integer inputs.
    """
    with pytest.raises(TypeError):
        generate_integers(a, b)