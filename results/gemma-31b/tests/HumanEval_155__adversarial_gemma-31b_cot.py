
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

@pytest.mark.parametrize("num, expected", [
    (123, (1, 2)),          # Standard positive integer
    (-12, (1, 1)),          # Standard negative integer
    (0, (1, 0)),            # Zero is an even digit
    (2468, (4, 0)),         # All even digits
    (1357, (0, 4)),         # All odd digits
    (-2468, (4, 0)),        # Negative all even
    (-1357, (0, 4)),        # Negative all odd
    (102, (2, 1)),          # Mixed with zero
    (1000, (3, 1)),         # Multiple zeros
    (999, (0, 3)),          # All odd digits
    (1234567890, (5, 5)),   # All digits 0-9
    (-101, (1, 2)),         # Negative mixed with zero
    (7, (0, 1)),            # Single odd digit
    (8, (1, 0)),            # Single even digit
])
def test_even_odd_count_logic(num, expected):
    """Test the function with various integer inputs to ensure correct counting of even and odd digits."""
    assert even_odd_count(num) == expected

def test_even_odd_count_large_number():
    """Test with a very large integer to ensure no overflow or performance issues."""
    num = 22222222221111111111
    assert even_odd_count(num) == (10, 10)

def test_even_odd_count_negative_large_number():
    """Test with a very large negative integer."""
    num = -22222222221111111111
    assert even_odd_count(num) == (10, 10)