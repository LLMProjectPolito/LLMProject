
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

import pytest

@pytest.mark.parametrize("num, expected", [
    (123, (1, 2)),        # Mixed digits
    (-12, (1, 1)),        # Negative mixed digits
    (0, (1, 0)),          # Zero (even)
    (2468, (4, 0)),       # All even
    (1357, (0, 4)),       # All odd
    (-2468, (4, 0)),      # Negative all even
    (-1357, (0, 4)),      # Negative all odd
    (100, (2, 1)),        # Multiple zeros
    (7, (0, 1)),          # Single odd digit
    (8, (1, 0)),          # Single even digit
    (10203, (3, 2)),      # Mixed with zeros
    (123456789, (4, 5)),  # Large range
    (-101, (1, 2)),       # Negative with zeros
])
def test_even_odd_count(num, expected):
    """
    Test the even_odd_count function with various edge cases including:
    - Positive and negative integers
    - Single digit numbers (0, even, odd)
    - Numbers with all even or all odd digits
    - Large integers
    """
    assert even_odd_count(num) == expected