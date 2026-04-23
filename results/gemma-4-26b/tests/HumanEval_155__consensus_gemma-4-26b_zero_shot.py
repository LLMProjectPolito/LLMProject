
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

@pytest.mark.parametrize("num, expected", [
    (0, (1, 0)),               # Zero case (0 is even)
    (1, (0, 1)),               # Single odd digit
    (2, (1, 0)),               # Single even digit
    (7, (0, 1)),               # Single odd digit
    (-5, (0, 1)),              # Negative single odd
    (-8, (1, 0)),              # Negative single even
    (11, (0, 2)),              # All odd digits
    (22, (2, 0)),              # All even digits
    (12, (1, 1)),              # Mixed digits
    (123, (1, 2)),             # Mixed digits
    (-12, (1, 1)),             # Negative mixed digits
    (-123, (1, 2)),            # Negative mixed digits
    (246, (3, 0)),             # Multiple even digits
    (135, (0, 3)),             # Multiple odd digits
    (10, (1, 1)),              # Mixed with zero
    (102, (2, 1)),             # Mixed digits with zero
    (1000, (3, 1)),            # Multiple zeros
    (2468, (4, 0)),            # All even digits
    (1357, (0, 4)),            # All odd digits
    (11111, (0, 5)),           # Large odd
    (22222, (5, 0)),           # Large even
    (101010, (3, 3)),          # Alternating digits
    (123456789, (4, 5)),       # Large positive mixed
    (987654321, (4, 5)),       # Large positive mixed
    (9876543210, (5, 5)),      # Large mixed
])
def test_even_odd_count(num, expected):
    """Test various integer inputs to ensure correct even and odd digit counts."""
    assert even_odd_count(num) == expected

def test_even_odd_count_types():
    """Ensures the output is always a tuple of two integers."""
    result = even_odd_count(123)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)