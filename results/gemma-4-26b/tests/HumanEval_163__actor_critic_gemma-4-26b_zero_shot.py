
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

def generate_integers(a, b):
    """
    Given two integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
        
    start, end = min(a, b), max(a, b)
    even_digits = [d for d in [0, 2, 4, 6, 8] if start <= d <= end]
    return even_digits

@pytest.mark.parametrize("a, b, expected", [
    # Standard cases
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
    
    # Edge cases: Single digit boundaries and 0
    (0, 2, [0, 2]),
    (1, 9, [2, 4, 6, 8]),
    (2, 2, [2]),
    (3, 3, []),
    (10, 10, []),
    (0, 0, [0]),
    
    # Edge cases: Range overlaps with digit range
    (5, 12, [6, 8]),
    (1, 5, [2, 4]),
    (7, 11, [8]),
    
    # Edge cases: Range entirely outside digit range (0-9)
    (11, 20, []),
    (100, 200, []),
    
    # Edge cases: All odd numbers in range
    (1, 1, []),
    (3, 5, [4]),
    (7, 9, [8]),

    # Boundary cases: Negative integers
    (-2, 2, [0, 2]),
    (-5, -1, []),
    (-4, 4, [0, 2, 4]),
])
def test_generate_integers(a, b, expected):
    """Tests the generate_integers function with various inputs."""
    assert generate_integers(a, b) == expected

def test_input_types():
    """Verify behavior with unexpected types to enforce integer requirement."""
    with pytest.raises(TypeError):
        generate_integers("2", 8)
    with pytest.raises(TypeError):
        generate_integers(2.5, 8)
    with pytest.raises(TypeError):
        generate_integers(2, 8.0)