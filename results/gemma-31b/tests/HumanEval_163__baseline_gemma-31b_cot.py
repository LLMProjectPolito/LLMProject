
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
    
    # Edge cases: Single values
    (2, 2, [2]),
    (3, 3, []),
    (8, 8, [8]),
    (9, 9, []),
    
    # Edge cases: Ranges partially overlapping digits (1-9)
    (5, 12, [6, 8]),
    (12, 5, [6, 8]),
    (0, 3, [0, 2]), # Testing 0 if treated as a positive integer or boundary
    (-2, 4, [0, 2, 4]), # Testing negative boundaries just in case
    
    # Edge cases: Ranges covering all or no even digits
    (1, 9, [2, 4, 6, 8]),
    (1, 1, []),
    (3, 5, [4]),
    (7, 9, [8]),
    
    # Edge cases: Large numbers
    (100, 200, []),
    (1, 100, [2, 4, 6, 8]),
])
def test_generate_integers(a, b, expected):
    """
    Tests the generate_integers function with various ranges to ensure
    it only returns even single-digit integers in ascending order.
    """
    assert generate_integers(a, b) == expected

def test_generate_integers_type():
    """
    Ensure the return type is always a list.
    """
    result = generate_integers(2, 8)
    assert isinstance(result, list)

def test_generate_integers_ascending():
    """
    Ensure the output is always in ascending order regardless of input order.
    """
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(2, 8) == [2, 4, 6, 8]