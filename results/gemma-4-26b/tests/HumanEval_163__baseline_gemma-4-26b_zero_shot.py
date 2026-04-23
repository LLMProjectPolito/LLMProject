
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
    
    # Single digit ranges
    (1, 3, [2]),
    (3, 1, [2]),
    (2, 2, [2]),
    (3, 3, []),
    (4, 4, [4]),
    
    # Ranges containing all even digits
    (1, 9, [2, 4, 6, 8]),
    (0, 8, [0, 2, 4, 6, 8]), # Testing 0 if allowed by "positive" context
    
    # Ranges with no even digits (all odd or all > 9)
    (1, 1, []),
    (11, 19, []),
    (11, 11, []),
    (13, 15, []),
    
    # Boundary conditions (even/odd at start/end)
    (2, 3, [2]),
    (3, 4, [4]),
    (1, 2, [2]),
    (2, 1, [2]),
    
    # Large number ranges
    (100, 200, []),
    (1000, 5000, []),
])
def test_generate_integers_parametrized(a, b, expected):
    """Test various ranges including ascending, descending, and edge cases."""
    assert generate_integers(a, b) == expected

def test_generate_integers_ascending_order_guarantee():
    """Ensure the output is always in ascending order regardless of input order."""
    res1 = generate_integers(8, 2)
    res2 = generate_integers(2, 8)
    assert res1 == [2, 4, 6, 8]
    assert res2 == [2, 4, 6, 8]
    assert res1 == res2

def test_generate_integers_type_consistency():
    """Ensure the return type is always a list."""
    assert isinstance(generate_integers(2, 8), list)
    assert isinstance(generate_integers(10, 14), list)

def test_generate_integers_empty_result():
    """Explicitly check that ranges without even digits return an empty list."""
    assert generate_integers(11, 13) == []
    assert generate_integers(15, 17) == []