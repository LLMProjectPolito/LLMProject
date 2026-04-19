
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
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.
    """
    start, end = min(a, b), max(a, b)
    # Even digits are 0, 2, 4, 6, 8. 
    # We check which of these single-digit even numbers fall within the inclusive range [start, end].
    evens = [0, 2, 4, 6, 8]
    return [d for d in evens if start <= d <= end]

@pytest.mark.parametrize("a, b, expected", [
    # Basic cases from problem description
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
    
    # Single digit boundaries and identity ranges
    (0, 0, [0]),
    (1, 1, []),
    (2, 2, [2]),
    (3, 3, []),
    (4, 4, [4]),
    (0, 1, [0]),
    (0, 9, [0, 2, 4, 6, 8]),
    
    # Ranges overlapping the digit boundary (0-9)
    (5, 12, [6, 8]),
    (7, 11, [8]),
    (5, 15, [6, 8]),
    (1, 11, [2, 4, 6, 8]),
    (15, 5, [6, 8]),
    (11, 1, [2, 4, 6, 8]),
    
    # Ranges completely outside the digit range
    (15, 20, []),
    (100, 200, []),
    
    # Odd-numbered ranges
    (1, 3, [2]),
    (3, 5, [4]),
    (5, 7, [6]),
    (7, 9, [8]),
    
    # Large boundaries
    (1, 1000, [2, 4, 6, 8]),
    (1000000, 2000000, []),
    
    # Non-positive integers (testing robustness)
    (-2, 4, [0, 2, 4]),
    (-10, -5, []),
    (0, 2, [0, 2]),
])
def test_generate_integers_parametrized(a, b, expected):
    """Test various ranges to ensure only single-digit even numbers are returned in ascending order."""
    assert generate_integers(a, b) == expected

def test_generate_integers_ascending_order():
    """Explicitly verify that the output is always in ascending order regardless of input order."""
    result_forward = generate_integers(2, 8)
    result_backward = generate_integers(8, 2)
    assert result_forward == sorted(result_forward)
    assert result_backward == sorted(result_backward)
    assert result_forward == result_backward

def test_generate_integers_type_consistency():
    """Ensure the return type is always a list, even when empty."""
    assert isinstance(generate_integers(2, 8), list)
    assert isinstance(generate_integers(10, 14), list)
    assert isinstance(generate_integers(-10, -5), list)

def test_generate_integers_performance_large_range():
    """Ensure the function handles extremely large ranges efficiently (O(1) complexity)."""
    # This should return instantly regardless of the distance between a and b
    assert generate_integers(1, 10**18) == [2, 4, 6, 8]