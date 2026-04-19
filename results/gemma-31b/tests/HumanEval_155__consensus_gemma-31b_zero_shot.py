
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

@pytest.mark.parametrize("num, expected", [
    (0, (1, 0)),          # Single even
    (1, (0, 1)),          # Single odd
    (2, (1, 0)),          # Single even
    (7, (0, 1)),          # Single odd
    (8, (1, 0)),          # Single even
    (-7, (0, 1)),         # Single negative odd
    (-8, (1, 0)),         # Single negative even
    (123, (1, 2)),        # Mixed
    (-12, (1, 1)),        # Negative mixed
    (2468, (4, 0)),       # All even
    (1357, (0, 4)),       # All odd
    (13579, (0, 5)),      # All odd
    (-2468, (4, 0)),      # Negative all even
    (-1357, (0, 4)),      # Negative all odd
    (-13579, (0, 5)),     # Negative all odd
    (1000, (3, 1)),       # Mixed with zeros
    (1010, (2, 2)),       # Mixed with zeros
    (102, (2, 1)),        # Mixed with zeros
    (-101, (1, 2)),       # Negative mixed with zeros
    (-100, (2, 1)),       # Negative mixed with zeros
    (2000000000, (10, 0)), # Large all even
    (20406, (5, 0)),      # All even
    (111, (0, 3)),        # All odd
    (123456789, (4, 5)),  # Mixed large
    (-123456789, (4, 5)), # Negative mixed large
    (1234567890, (5, 5)), # Mixed large with zero
])
def test_even_odd_count(num, expected):
    assert even_odd_count(num) == expected