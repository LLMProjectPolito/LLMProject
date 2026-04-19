
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

@pytest.mark.parametrize("num, expected", [
    (0, (1, 0)),           # Zero is even
    (1, (0, 1)),           # Single odd
    (2, (1, 0)),           # Single even
    (3, (0, 1)),           # Single odd
    (7, (0, 1)),           # Single odd
    (8, (1, 0)),           # Single even
    (-7, (0, 1)),          # Single negative odd
    (-8, (1, 0)),          # Single negative even
    (123, (1, 2)),         # Mixed positive
    (-12, (1, 1)),         # Mixed negative
    (246, (3, 0)),         # All even
    (135, (0, 3)),         # All odd
    (-444, (3, 0)),        # Negative all even
    (-135, (0, 3)),        # Negative all odd
    (10, (1, 1)),          # 0 is even, 1 is odd
    (100, (2, 1)),         # 0, 0 are even, 1 is odd
    (101, (1, 2)),         # Middle zero
    (1000, (3, 1)),        # Multiple zeros (even)
    (-1000, (3, 1)),       # Multiple zeros negative
    (2468, (4, 0)),        # All even
    (1357, (0, 4)),        # All odd
    (13579, (0, 5)),       # All odd
    (-2468, (4, 0)),       # All even negative
    (-1357, (0, 4)),       # All odd negative
    (-246, (3, 0)),        # Negative all even
    (-2048, (4, 0)),       # Negative with zero
    (123456789, (4, 5)),   # Large mixed positive
    (-123456789, (4, 5)),  # Large mixed negative
    (1234567890, (5, 5)),  # Balanced large number
    (204060, (6, 0)),      # Alternating zeros and evens
])
def test_even_odd_count(num, expected):
    assert even_odd_count(num) == expected

def test_even_odd_count_type():
    """Ensure the return type is always a tuple."""
    result = even_odd_count(123)
    assert isinstance(result, tuple)
    assert len(result) == 2

def test_even_odd_count_large_integer():
    """Test with a very large integer to ensure stability."""
    num = 22222222221111111111
    assert even_odd_count(num) == (10, 10)