
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

@pytest.mark.parametrize("num, expected", [
    # Basic positive integers (mixed, all even, all odd)
    (123, (1, 2)),
    (1234, (2, 2)),
    (1357, (0, 4)),
    (2468, (4, 0)),
    (468, (3, 0)),
    (135, (0, 3)),
    (24681357, (4, 4)),
    
    # Negative integers (sign should be ignored)
    (-12, (1, 1)),
    (-48, (2, 0)),
    (-135, (0, 3)),
    (-204, (3, 0)),
    (-44, (2, 0)),
    (-77, (0, 2)),
    (-101, (1, 2)),
    (-20468, (5, 0)),
    
    # Edge cases: Zero and Single Digits
    (0, (1, 0)),
    (2, (1, 0)),
    (7, (0, 1)),
    (-8, (1, 0)),
    (-3, (0, 1)),
    
    # Large numbers and specific patterns
    (100, (2, 1)),
    (1000000001, (8, 2)),
    (2222, (4, 0)),
    (1111, (0, 4)),
    (2222222222, (10, 0)),
    (1111111111, (0, 10)),
])
def test_even_odd_count(num, expected):
    """
    Comprehensive test suite for even_odd_count.
    Covers positive/negative integers, zero, single digits, and large numbers.
    """
    assert even_odd_count(num) == expected