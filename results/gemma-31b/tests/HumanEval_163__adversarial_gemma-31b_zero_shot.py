
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
    # This is the function under test. 
    # The implementation is implied by the problem description.
    low, high = min(a, b), max(a, b)
    return [i for i in range(low, high + 1) if 0 <= i <= 9 and i % 2 == 0]

@pytest.mark.parametrize("a, b, expected", [
    # Provided examples
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
    
    # Edge cases: Single digit ranges
    (2, 2, [2]),
    (3, 3, []),
    (1, 1, []),
    
    # Edge cases: Boundaries of "digits" (0-9)
    (1, 9, [2, 4, 6, 8]),
    (0, 2, [0, 2]), # Testing 0 if the implementation treats it as a digit
    (8, 12, [8]),   # Range overlapping the digit boundary
    (5, 15, [6, 8]), # Range overlapping the digit boundary
    
    # Edge cases: No even digits in range
    (1, 1, []),
    (3, 3, []),
    (11, 13, []),
    
    # Edge cases: Small ranges
    (2, 3, [2]),
    (3, 4, [4]),
    (4, 5, [4]),
    
    # Large numbers
    (100, 200, []),
    (100, 2, [2, 4, 6, 8]),
])
def test_generate_integers(a, b, expected):
    """
    Test generate_integers with various inputs to ensure it correctly identifies
    even digits within the range [min(a, b), max(a, b)].
    """
    assert generate_integers(a, b) == expected

def test_generate_integers_type_consistency():
    """
    Ensure the function always returns a list, even when empty.
    """
    result = generate_integers(11, 15)
    assert isinstance(result, list)

def test_generate_integers_ascending_order():
    """
    Ensure the output is always in ascending order regardless of input order.
    """
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(2, 8) == [2, 4, 6, 8]