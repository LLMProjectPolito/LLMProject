
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

@pytest.mark.parametrize("num, expected", [
    (123, (1, 2)),        # Standard positive
    (-12, (1, 1)),        # Standard negative
    (0, (1, 0)),          # Zero (even)
    (1, (0, 1)),          # Single odd
    (2, (1, 0)),          # Single even
    (13579, (0, 5)),      # All odd
    (24680, (5, 0)),      # All even
    (-13579, (0, 5)),     # All odd negative
    (-24680, (5, 0)),     # All even negative
    (101, (1, 2)),        # Mixed with zeros
    (100, (2, 1)),        # Mixed with zeros
    (1234567890, (5, 5)), # Large number
    (-101010, (3, 3)),    # Negative mixed
])
def test_even_odd_count(num, expected):
    assert even_odd_count(num) == expected