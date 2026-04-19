
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest
from solution import even_odd_count

@pytest.mark.parametrize("num, expected", [
    (0, (1, 0)),           # Zero is even
    (1, (0, 1)),           # Single odd digit
    (2, (1, 0)),           # Single even digit
    (123, (1, 2)),         # Mixed positive
    (-12, (1, 1)),         # Mixed negative
    (2468, (4, 0)),        # All even
    (1357, (0, 4)),        # All odd
    (-135, (0, 3)),        # All odd negative
    (100, (2, 1)),         # Multiple zeros (even)
    (-100, (2, 1)),        # Multiple zeros negative
    (10203, (3, 2)),       # Large mixed
    (-24680, (5, 0)),      # Large even negative
    (99999, (0, 5)),       # Large odd
])
def test_even_odd_count(num, expected):
    """Test that even_odd_count correctly counts even and odd digits for various integers."""
    assert even_odd_count(num) == expected

def test_even_odd_count_type():
    """Test that the return type is always a tuple of two integers."""
    result = even_odd_count(123)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], int)
    assert isinstance(result[1], int)