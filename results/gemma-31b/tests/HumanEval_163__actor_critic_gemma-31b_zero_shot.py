
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
    start = min(a, b)
    end = max(a, b)
    
    # Even digits are 0, 2, 4, 6, 8. 
    # We filter for numbers in the range [start, end] that are both < 10 and even.
    return [i for i in range(start, end + 1) if i < 10 and i % 2 == 0]

@pytest.mark.parametrize("a, b, expected", [
    # Standard cases from problem description
    (2, 8, [2, 4, 6, 8]),
    (8, 2, [2, 4, 6, 8]),
    (10, 14, []),
    
    # Range with a single even digit
    (1, 3, [2]),
    (3, 1, [2]),
    
    # Range with no even digits
    (1, 1, []),
    (3, 3, []),
    (11, 13, []),
    
    # Range where a == b and it is an even digit
    (4, 4, [4]),
    
    # Range partially overlapping the digit range (0-9)
    (5, 12, [6, 8]),
    (12, 5, [6, 8]),
    (0, 5, [0, 2, 4]), # Including 0 if treated as a positive/non-negative integer
    
    # Range covering all even digits
    (0, 9, [0, 2, 4, 6, 8]),
    (9, 0, [0, 2, 4, 6, 8]),
    
    # Range completely above digits
    (100, 200, []),
    
    # Large range including all digits
    (1, 100, [2, 4, 6, 8]),
])
def test_generate_integers(a, b, expected):
    assert generate_integers(a, b) == expected

def test_generate_integers_type():
    """Ensure the function returns a list."""
    result = generate_integers(2, 8)
    assert isinstance(result, list)

def test_generate_integers_ascending():
    """Ensure the output is always in ascending order regardless of input order."""
    assert generate_integers(8, 2) == [2, 4, 6, 8]
    assert generate_integers(2, 8) == [2, 4, 6, 8]